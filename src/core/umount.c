/*-*- Mode: C; c-basic-offset: 8; indent-tabs-mode: nil -*-*/

/***
  This file is part of systemd.

  Copyright 2010 ProFUSION embedded systems

  systemd is free software; you can redistribute it and/or modify it
  under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation; either version 2.1 of the License, or
  (at your option) any later version.

  systemd is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with systemd; If not, see <http://www.gnu.org/licenses/>.
***/

#include <errno.h>
#include <fcntl.h>
#include <string.h>
#include <sys/mount.h>
#include <sys/swap.h>
#include <unistd.h>
#include <linux/loop.h>
#include <linux/dm-ioctl.h>

#include "list.h"
#include "mount-setup.h"
#include "umount.h"
#include "path-util.h"
#include "util.h"
#include "virt.h"
#include "libudev.h"
#include "udev-util.h"

typedef struct MountPoint {
        char *path;
        dev_t devnum;
        LIST_FIELDS (struct MountPoint, mount_point);
} MountPoint;

static void mount_point_free(MountPoint **head, MountPoint *m) {
        assert(head);
        assert(m);

        LIST_REMOVE(MountPoint, mount_point, *head, m);

        free(m->path);
        free(m);
}

static void mount_points_list_free(MountPoint **head) {
        assert(head);

        while (*head)
                mount_point_free(head, *head);
}

static int mount_points_list_get(MountPoint **head) {
        FILE *proc_self_mountinfo;
        char *path, *p;
        unsigned int i;
        int r;

        assert(head);

        if (!(proc_self_mountinfo = fopen("/proc/self/mountinfo", "re")))
                return -errno;

        for (i = 1;; i++) {
                int k;
                MountPoint *m;

                path = p = NULL;

                if ((k = fscanf(proc_self_mountinfo,
                                "%*s "       /* (1) mount id */
                                "%*s "       /* (2) parent id */
                                "%*s "       /* (3) major:minor */
                                "%*s "       /* (4) root */
                                "%ms "       /* (5) mount point */
                                "%*s"        /* (6) mount options */
                                "%*[^-]"     /* (7) optional fields */
                                "- "         /* (8) separator */
                                "%*s "       /* (9) file system type */
                                "%*s"        /* (10) mount source */
                                "%*s"        /* (11) mount options 2 */
                                "%*[^\n]",   /* some rubbish at the end */
                                &path)) != 1) {
                        if (k == EOF)
                                break;

                        log_warning("Failed to parse /proc/self/mountinfo:%u.", i);

                        free(path);
                        continue;
                }

                p = cunescape(path);
                free(path);

                if (!p) {
                        r = -ENOMEM;
                        goto finish;
                }

                /* Ignore mount points we can't unmount because they
                 * are API or because we are keeping them open (like
                 * /dev/console) */
                if (mount_point_is_api(p) ||
                    mount_point_ignore(p) ||
                    path_equal(p, "/dev/console")) {
                        free(p);
                        continue;
                }

                if (!(m = new0(MountPoint, 1))) {
                        free(p);
                        r = -ENOMEM;
                        goto finish;
                }

                m->path = p;
                LIST_PREPEND(MountPoint, mount_point, *head, m);
        }

        r = 0;

finish:
        fclose(proc_self_mountinfo);

        return r;
}

static int swap_list_get(MountPoint **head) {
        FILE *proc_swaps;
        unsigned int i;
        int r;

        assert(head);

        if (!(proc_swaps = fopen("/proc/swaps", "re")))
                return (errno == ENOENT) ? 0 : -errno;

        (void) fscanf(proc_swaps, "%*s %*s %*s %*s %*s\n");

        for (i = 2;; i++) {
                MountPoint *swap;
                char *dev = NULL, *d;
                int k;

                if ((k = fscanf(proc_swaps,
                                "%ms " /* device/file */
                                "%*s " /* type of swap */
                                "%*s " /* swap size */
                                "%*s " /* used */
                                "%*s\n", /* priority */
                                &dev)) != 1) {

                        if (k == EOF)
                                break;

                        log_warning("Failed to parse /proc/swaps:%u.", i);

                        free(dev);
                        continue;
                }

                if (endswith(dev, "(deleted)")) {
                        free(dev);
                        continue;
                }

                d = cunescape(dev);
                free(dev);

                if (!d) {
                        r = -ENOMEM;
                        goto finish;
                }

                if (!(swap = new0(MountPoint, 1))) {
                        free(d);
                        r = -ENOMEM;
                        goto finish;
                }

                swap->path = d;
                LIST_PREPEND(MountPoint, mount_point, *head, swap);
        }

        r = 0;

finish:
        fclose(proc_swaps);

        return r;
}

static int loopback_list_get(MountPoint **head) {
        _cleanup_udev_unref_ struct udev *udev;
        _cleanup_udev_enumerate_unref_ struct udev_enumerate *e = NULL;
        struct udev_list_entry *item = NULL, *first = NULL;

        assert(head);

        udev = udev_new();
        if (!udev)
                return -ENOMEM;

        e = udev_enumerate_new(udev);
        if (!e)
                return -ENOMEM;

        if (udev_enumerate_add_match_subsystem(e, "block") < 0 ||
            udev_enumerate_add_match_sysname(e, "loop*") < 0 ||
            udev_enumerate_add_match_sysattr(e, "loop/backing_file", NULL) < 0)
                return -EIO;

        if (udev_enumerate_scan_devices(e) < 0)
                return -EIO;

        first = udev_enumerate_get_list_entry(e);
        udev_list_entry_foreach(item, first) {
                MountPoint *lb;
                _cleanup_udev_device_unref_ struct udev_device *d;
                char *loop;
                const char *dn;

                d = udev_device_new_from_syspath(udev, udev_list_entry_get_name(item));
                if (!d)
                        return -ENOMEM;

                dn = udev_device_get_devnode(d);
                if (!dn)
                        continue;

                loop = strdup(dn);
                if (!loop)
                        return -ENOMEM;

                lb = new0(MountPoint, 1);
                if (!lb) {
                        free(loop);
                        return -ENOMEM;
                }

                lb->path = loop;
                LIST_PREPEND(MountPoint, mount_point, *head, lb);
        }

        return 0;
}

static int dm_list_get(MountPoint **head) {
        _cleanup_udev_unref_ struct udev *udev;
        _cleanup_udev_enumerate_unref_ struct udev_enumerate *e = NULL;
        struct udev_list_entry *item = NULL, *first = NULL;

        assert(head);

        udev = udev_new();
        if (!udev)
                return -ENOMEM;

        e = udev_enumerate_new(udev);
        if (!e)
                return -ENOMEM;

        if (udev_enumerate_add_match_subsystem(e, "block") < 0 ||
            udev_enumerate_add_match_sysname(e, "dm-*") < 0)
                return -EIO;

        if (udev_enumerate_scan_devices(e) < 0)
                return -EIO;

        first = udev_enumerate_get_list_entry(e);

        udev_list_entry_foreach(item, first) {
                MountPoint *m;
                _cleanup_udev_device_unref_ struct udev_device *d;
                dev_t devnum;
                char *node;
                const char *dn;

                d = udev_device_new_from_syspath(udev, udev_list_entry_get_name(item));
                if (!d)
                        return -ENOMEM;

                devnum = udev_device_get_devnum(d);
                dn = udev_device_get_devnode(d);
                if (major(devnum) == 0 || !dn)
                        continue;

                node = strdup(dn);
                if (!node)
                        return -ENOMEM;

                m = new(MountPoint, 1);
                if (!m) {
                        free(node);
                        return -ENOMEM;
                }

                m->path = node;
                m->devnum = devnum;
                LIST_PREPEND(MountPoint, mount_point, *head, m);
        }

        return 0;
}

static int delete_loopback(const char *device) {
        int fd, r;

        if ((fd = open(device, O_RDONLY|O_CLOEXEC)) < 0)
                return errno == ENOENT ? 0 : -errno;

        r = ioctl(fd, LOOP_CLR_FD, 0);
        close_nointr_nofail(fd);

        if (r >= 0)
                return 1;

        /* ENXIO: not bound, so no error */
        if (errno == ENXIO)
                return 0;

        return -errno;
}

static int delete_dm(dev_t devnum) {
        _cleanup_close_ int fd = -1;
        int r;
        struct dm_ioctl dm = {
                .version = {DM_VERSION_MAJOR,
                            DM_VERSION_MINOR,
                            DM_VERSION_PATCHLEVEL},
                .data_size = sizeof(dm),
                .dev = devnum,
        };

        assert(major(devnum) != 0);

        fd = open("/dev/mapper/control", O_RDWR|O_CLOEXEC);
        if (fd < 0)
                return -errno;

        r = ioctl(fd, DM_DEV_REMOVE, &dm);
        return r >= 0 ? 0 : -errno;
}

static int mount_points_list_umount(MountPoint **head, bool *changed, bool log_error) {
        MountPoint *m, *n;
        int n_failed = 0;

        assert(head);

        LIST_FOREACH_SAFE(mount_point, m, n, *head) {

                /* If we are in a container, don't attempt to
                   read-only mount anything as that brings no real
                   benefits, but might confuse the host, as we remount
                   the superblock here, not the bind mound. */
                if (detect_container(NULL) <= 0)  {
                        /* We always try to remount directories
                         * read-only first, before we go on and umount
                         * them.
                         *
                         * Mount points can be stacked. If a mount
                         * point is stacked below / or /usr, we
                         * cannot umount or remount it directly,
                         * since there is no way to refer to the
                         * underlying mount. There's nothing we can do
                         * about it for the general case, but we can
                         * do something about it if it is aliased
                         * somehwere else via a bind mount. If we
                         * explicitly remount the super block of that
                         * alias read-only we hence should be
                         * relatively safe regarding keeping the fs we
                         * can otherwise not see dirty. */
                        mount(NULL, m->path, NULL, MS_REMOUNT|MS_RDONLY, NULL);
                }

                /* Skip / and /usr since we cannot unmount that
                 * anyway, since we are running from it. They have
                 * already been remounted ro. */
                if (path_equal(m->path, "/")
#ifndef HAVE_SPLIT_USR
                    || path_equal(m->path, "/usr")
#endif
                )
                        continue;

                /* Trying to umount. We don't force here since we rely
                 * on busy NFS and FUSE file systems to return EBUSY
                 * until we closed everything on top of them. */
                log_info("Unmounting %s.", m->path);
                if (umount2(m->path, 0) == 0) {
                        if (changed)
                                *changed = true;

                        mount_point_free(head, m);
                } else if (log_error) {
                        log_warning("Could not unmount %s: %m", m->path);
                        n_failed++;
                }
        }

        return n_failed;
}

static int swap_points_list_off(MountPoint **head, bool *changed) {
        MountPoint *m, *n;
        int n_failed = 0;

        assert(head);

        LIST_FOREACH_SAFE(mount_point, m, n, *head) {
                log_info("Deactivating swap %s.", m->path);
                if (swapoff(m->path) == 0) {
                        if (changed)
                                *changed = true;

                        mount_point_free(head, m);
                } else {
                        log_warning("Could not deactivate swap %s: %m", m->path);
                        n_failed++;
                }
        }

        return n_failed;
}

static int loopback_points_list_detach(MountPoint **head, bool *changed) {
        MountPoint *m, *n;
        int n_failed = 0, k;
        struct stat root_st;

        assert(head);

        k = lstat("/", &root_st);

        LIST_FOREACH_SAFE(mount_point, m, n, *head) {
                int r;
                struct stat loopback_st;

                if (k >= 0 &&
                    major(root_st.st_dev) != 0 &&
                    lstat(m->path, &loopback_st) >= 0 &&
                    root_st.st_dev == loopback_st.st_rdev) {
                        n_failed ++;
                        continue;
                }

                log_info("Detaching loopback %s.", m->path);
                r = delete_loopback(m->path);
                if (r >= 0) {
                        if (r > 0 && changed)
                                *changed = true;

                        mount_point_free(head, m);
                } else {
                        log_warning("Could not detach loopback %s: %m", m->path);
                        n_failed++;
                }
        }

        return n_failed;
}

static int dm_points_list_detach(MountPoint **head, bool *changed) {
        MountPoint *m, *n;
        int n_failed = 0, k;
        struct stat root_st;

        assert(head);

        k = lstat("/", &root_st);

        LIST_FOREACH_SAFE(mount_point, m, n, *head) {
                int r;

                if (k >= 0 &&
                    major(root_st.st_dev) != 0 &&
                    root_st.st_dev == m->devnum) {
                        n_failed ++;
                        continue;
                }

                log_info("Detaching DM %u:%u.", major(m->devnum), minor(m->devnum));
                r = delete_dm(m->devnum);
                if (r >= 0) {
                        if (changed)
                                *changed = true;

                        mount_point_free(head, m);
                } else {
                        log_warning("Could not detach DM %s: %m", m->path);
                        n_failed++;
                }
        }

        return n_failed;
}

int umount_all(bool *changed) {
        int r;
        bool umount_changed;
        LIST_HEAD(MountPoint, mp_list_head);

        LIST_HEAD_INIT(MountPoint, mp_list_head);
        r = mount_points_list_get(&mp_list_head);
        if (r < 0)
                goto end;

        /* retry umount, until nothing can be umounted anymore */
        do {
                umount_changed = false;

                mount_points_list_umount(&mp_list_head, &umount_changed, false);
                if (umount_changed)
                        *changed = true;

        } while (umount_changed);

        /* umount one more time with logging enabled */
        r = mount_points_list_umount(&mp_list_head, &umount_changed, true);
        if (r <= 0)
                goto end;

  end:
        mount_points_list_free(&mp_list_head);

        return r;
}

int swapoff_all(bool *changed) {
        int r;
        LIST_HEAD(MountPoint, swap_list_head);

        LIST_HEAD_INIT(MountPoint, swap_list_head);

        r = swap_list_get(&swap_list_head);
        if (r < 0)
                goto end;

        r = swap_points_list_off(&swap_list_head, changed);

  end:
        mount_points_list_free(&swap_list_head);

        return r;
}

int loopback_detach_all(bool *changed) {
        int r;
        LIST_HEAD(MountPoint, loopback_list_head);

        LIST_HEAD_INIT(MountPoint, loopback_list_head);

        r = loopback_list_get(&loopback_list_head);
        if (r < 0)
                goto end;

        r = loopback_points_list_detach(&loopback_list_head, changed);

  end:
        mount_points_list_free(&loopback_list_head);

        return r;
}

int dm_detach_all(bool *changed) {
        int r;
        LIST_HEAD(MountPoint, dm_list_head);

        LIST_HEAD_INIT(MountPoint, dm_list_head);

        r = dm_list_get(&dm_list_head);
        if (r < 0)
                goto end;

        r = dm_points_list_detach(&dm_list_head, changed);

  end:
        mount_points_list_free(&dm_list_head);

        return r;
}
