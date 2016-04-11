# We ship a .pc file but don't want to have a dep on pkg-config. We
# strip the automatically generated dep here and instead co-own the
# directory.
%global __requires_exclude pkg-config
%global _hardened_build 1

Name:           systemd
Url:            http://www.freedesktop.org/wiki/Software/systemd
Version:        219
Release:        19%{?dist}
# For a breakdown of the licensing, see README
License:        LGPLv2+ and MIT and GPLv2+
Summary:        A System and Service Manager

Source0:        http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz
# Preset policy is in rhel-release package
# we are just disabling everything
Source1:        99-default-disable.preset
# Prevent accidental removal of the systemd package
Source2:        yum-protect-systemd.conf
# SysV convert script.
Source3:        systemd-sysv-convert
# ship /etc/rc.d/rc.local https://bugzilla.redhat.com/show_bug.cgi?id=968401
Source4:        rc.local
#https://bugzilla.redhat.com/show_bug.cgi?id=1032711
Source5:        60-alias-kmsg.rules
# Stop-gap, just to ensure things work fine with rsyslog without having to change the package right-away
Source6:        listen.conf

# RHEL-specific
Patch0001: 0001-kernel-install-add-fedora-specific-callouts-to-new-k.patch
Patch0002: 0002-Revert-fsck-re-enable-fsck-l.patch
Patch0003: 0003-sysctl-bring-back-etc-sysctl.conf.patch
Patch0004: 0004-remove-user-.service.patch
Patch0005: 0005-logind-session-save-stopping-flag.patch
Patch0006: 0006-man-mention-System-Administrator-s-Guide-in-systemct.patch
Patch0007: 0007-rules-automatically-online-hot-added-CPUs.patch
Patch0008: 0008-Revert-remove-references-of-readahead.patch
Patch0009: 0009-Revert-missing-remove-fanotify.patch
Patch0010: 0010-Revert-readahead-wipe-out-readahead.patch
Patch0011: 0011-rules-add-rule-for-naming-Dell-iDRAC-USB-Virtual-NIC.patch
Patch0012: 0012-udev-net_id-correctly-name-netdevs-based-on-dev_port.patch
Patch0013: 0013-Revert-blkid-Warn-when-rejecting-a-superblock-with-a.patch
Patch0014: 0014-journald-audit-exit-gracefully-in-the-case-we-can-t-.patch
Patch0015: 0015-fedora-disable-resolv.conf-symlink.patch
Patch0016: 0016-Revert-timedated-manage-systemd-timesyncd-directly-i.patch
Patch0017: 0017-journal-remote-fix-certificate-status-memory-leak.patch
Patch0018: 0018-journal-remote-fix-client_cert-memory-leak.patch
Patch0019: 0019-tmpfiles-Fix-parse_acl-error-message.patch
Patch0020: 0020-test-utf8-fix-utf16-tests-on-BE-machines.patch
Patch0021: 0021-tmpfiles-avoid-creating-duplicate-acl-entries.patch
Patch0022: 0022-shared-time-util-fix-gcc5-warning.patch
Patch0023: 0023-test-time-test-infinity-parsing-in-nanoseconds.patch
Patch0024: 0024-bootchart-fix-default-init-path.patch
Patch0025: 0025-systemctl-bump-NOFILE-only-for-systemctl_main.patch
Patch0026: 0026-acl-util-avoid-freeing-uninitialized-pointer.patch
Patch0027: 0027-bootchart-svg-fix-checking-of-list-end.patch
Patch0028: 0028-systemd-add-getrandom-syscall-numbers-for-MIPS.patch
Patch0029: 0029-unit-use-weaker-dependencies-between-mount-and-devic.patch
Patch0030: 0030-unit-When-stopping-due-to-BindsTo-log-which-unit-cau.patch
Patch0031: 0031-sysctl-downgrade-message-about-sysctl-overrides-to-d.patch
Patch0032: 0032-sysctl-add-some-hints-how-to-override-settings.patch
Patch0033: 0033-core-rework-device-state-logic.patch
Patch0034: 0034-core-fix-return-value-on-OOM.patch
Patch0035: 0035-machined-use-x-machine-unix-prefix-for-the-container.patch
Patch0036: 0036-shared-AFS-is-also-a-network-filesystem.patch
Patch0037: 0037-core-downgrade-unit-type-not-supported-message.patch
Patch0038: 0038-journal-remote-fix-saving-of-binary-fields.patch
Patch0039: 0039-journal-fix-Inappropriate-ioctl-for-device-on-ext4.patch
Patch0040: 0040-sd-daemon-replace-VLA-with-alloca-to-make-llvm-happy.patch
Patch0041: 0041-tmpfiles-quietly-ignore-ACLs-on-unsupported-filesyst.patch
Patch0042: 0042-shared-util-assume-ac-when-sys-class-power_supply-is.patch
Patch0043: 0043-import-remove-unused-variable.patch
Patch0044: 0044-hwdb-fix-ThinkPad-X-Tablet-special-keys.patch
Patch0045: 0045-man-add-newlines-to-the-pull-raw-example-in-machinec.patch
Patch0046: 0046-core-shared-in-deserializing-match-same-files-reache.patch
Patch0047: 0047-shared-use-SocketAddress-in-socket_address_matches_f.patch
Patch0048: 0048-shared-avoid-semi-duplicating-socket_address_equal.patch
Patch0049: 0049-shared-handle-unnamed-sockets-in-socket_address_equa.patch
Patch0050: 0050-man-make-bootup-graph-consistent.patch
Patch0051: 0051-nspawn-fix-whitespace-and-typo-in-partition-table-bl.patch
Patch0052: 0052-man-explain-time-units-in-tmpfiles.patch
Patch0053: 0053-systemctl-check-validity-of-PID-we-received.patch
Patch0054: 0054-systemctl-support-auditd.service-better.patch
Patch0055: 0055-shared-unit-name-fix-gcc5-warning.patch
Patch0056: 0056-test-hashmap-fix-gcc5-warning.patch
Patch0057: 0057-shared-fix-wrong-assertion-in-barrier_set_role.patch
Patch0058: 0058-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch0059: 0059-journal-make-skipping-of-exhausted-journal-files-eff.patch
Patch0060: 0060-shared-condition-fix-gcc5-warning.patch
Patch0061: 0061-man-correct-description-of-systemd-user-sessions.patch
Patch0062: 0062-build-sys-allow-lto-and-FORTIFY_SOURCE-with-O-sz.patch
Patch0063: 0063-man-fix-typo.patch
Patch0064: 0064-bus-proxyd-avoid-logging-oom-twice.patch
Patch0065: 0065-Do-not-run-sysv-generator-test-when-sysv-compat-is-d.patch
Patch0066: 0066-README-mention-ACLs-more.patch
Patch0067: 0067-Do-not-advertise-.d-snippets-over-main-config-file.patch
Patch0068: 0068-hwdb-add-pnpid-for-the-T450s-touchpad.patch
Patch0069: 0069-networkd-netdev-inform-when-we-take-over-an-existing.patch
Patch0070: 0070-man-replace-obsolete-wiki-link-with-man-page.patch
Patch0071: 0071-Use-correct-uname-identifiers-in-arch_map-for-SuperH.patch
Patch0072: 0072-hwdb-fix-Dell-XPS12-9Q33-key-name.patch
Patch0073: 0073-Remove-the-cap-on-epoll-events.patch
Patch0074: 0074-Allow-up-to-4096-simultaneous-connections.patch
Patch0075: 0075-hwdb-add-Logitech-G5-Laser-Mouse.patch
Patch0076: 0076-tmpfiles-Fix-handling-of-duplicate-lines.patch
Patch0077: 0077-hwdb-add-Lenovo-W451-to-TOUCHPAD_HAS_TRACKPOINT_BUTT.patch
Patch0078: 0078-vconsole-match-on-vtcon-events-not-fbcon-ones.patch
Patch0079: 0079-core-do-not-spawn-jobs-or-touch-other-units-during-c.patch
Patch0080: 0080-firstboot-set-all-spwd-fields-to-1-for-consistency-w.patch
Patch0081: 0081-sysusers-do-not-reject-users-with-already-present-et.patch
Patch0082: 0082-nspawn-fix-use-after-free-and-leak-in-error-paths.patch
Patch0083: 0083-login-fix-copy-pasto-in-error-path.patch
Patch0084: 0084-journalctl-update-hint-now-that-we-set-ACL-everywher.patch
Patch0085: 0085-sd-journal-return-error-when-we-cannot-open-a-file.patch
Patch0086: 0086-missing.h-add-NDA_.patch
Patch0087: 0087-udevd-close-race-in-udev-settle.patch
Patch0088: 0088-man-document-that-ExecStartPre-is-not-the-place-to-s.patch
Patch0089: 0089-journal-fix-return-code.patch
Patch0090: 0090-console-fix-error-code-inversion.patch
Patch0091: 0091-bus-proxy-complain-only-once-about-queue-overflows.patch
Patch0092: 0092-cgtop-fix-assert-when-not-on-tty.patch
Patch0093: 0093-man-split-paragraph.patch
Patch0094: 0094-hwdb-update.patch
Patch0095: 0095-networkd-Begin-with-serial-number-1-for-netlink-requ.patch
Patch0096: 0096-journal-remote-downgrade-routine-messages-to-debug.patch
Patch0097: 0097-journal-remote-process-events-without-delay.patch
Patch0098: 0098-man-update-example-2-in-systemd.network-5.patch
Patch0099: 0099-gpt-auto-generator-fix-detection-of-srv.patch
Patch0100: 0100-sd-rtnl-never-set-serial-to-0.patch
Patch0101: 0101-gpt-auto-generator-allow-type-check-to-fail.patch
Patch0102: 0102-man-fix-a-bunch-of-links.patch
Patch0103: 0103-man-link-to-fd.o-for-dbus-stuff.patch
Patch0104: 0104-man-fix-name-of-systemd.resource-control-5.patch
Patch0105: 0105-selinux-fix-SEGV-during-switch-root-if-SELinux-polic.patch
Patch0106: 0106-service-don-t-add-After-dependencies-on-.busname-uni.patch
Patch0107: 0107-libudev-monitor-fix-error-path-in-send_device.patch
Patch0108: 0108-core-remove-left-over-debug-message.patch
Patch0109: 0109-units-there-is-no-systemd-udev-hwdb-update.service.patch
Patch0110: 0110-util-remove-redundant-debug-message.patch
Patch0111: 0111-tmpfiles-remove-redundant-debug-message.patch
Patch0112: 0112-sysv-generator-initialize-LookupPaths-just-once.patch
Patch0113: 0113-core-do-not-use-quotes-around-virt-and-arch.patch
Patch0114: 0114-udev-downgrade-has-devpath-and-filled-with-db-file-m.patch
Patch0115: 0115-cryptsetup-generator-remove-warning-about-crypttab-a.patch
Patch0116: 0116-sysctl-tweak-debug-message.patch
Patch0117: 0117-journald-add-syslog-fields-for-audit-messages.patch
Patch0118: 0118-core-remove-useless-debug-message.patch
Patch0119: 0119-man-standard-conf-change-directory-reference-to-wild.patch
Patch0120: 0120-core-don-t-change-removed-devices-to-state-tentative.patch
Patch0121: 0121-fstab-generator-ignore-invalid-swap-priority.patch
Patch0122: 0122-missing.h-add-more-btrfs-types-and-defines.patch
Patch0123: 0123-build-sys-add-configure-option-to-disableLTO-gold.patch
Patch0124: 0124-rules-bring-back-80-net-name-slot.rules.patch
Patch0125: 0125-Revert-journald-allow-restarting-journald-without-lo.patch
Patch0126: 0126-Revert-man-switch-yum-to-dnf-for-Fedora.patch
Patch0127: 0127-journal-remove-audit-socket-unit-files.patch
Patch0128: 0128-factory-we-don-t-want-that.patch
Patch0129: 0129-timedated-flip-internal-status-after-executing-opera.patch
Patch0130: 0130-timedated-fix-enable-disable-reversal.patch
Patch0131: 0131-core-make-SELinux-enable-disable-check-symmetric.patch
Patch0132: 0132-shared-add-path_compare-an-ordering-path-comparison.patch
Patch0133: 0133-core-namespace-fix-path-sorting.patch
Patch0134: 0134-machine-do-not-rely-on-asprintf-setting-arg-on-error.patch
Patch0135: 0135-some-compilators-don-t-support-__INCLUDE_LEVEL__.patch
Patch0136: 0136-udev-net_id-support-multi-port-enpo-device-names.patch
Patch0137: 0137-udev-net_id-improve-comments.patch
Patch0138: 0138-udev-restore-udevadm-settle-timeout.patch
Patch0139: 0139-udev-settle-should-return-immediately-when-timeout-i.patch
Patch0140: 0140-udev-Fix-ping-timeout-when-settle-timeout-is-0.patch
Patch0141: 0141-detect-virt-use-proc-device-tree.patch
Patch0142: 0142-ARM-detect-virt-detect-Xen.patch
Patch0143: 0143-ARM-detect-virt-detect-QEMU-KVM.patch
Patch0144: 0144-Persistent-by_path-links-for-ata-devices.patch
Patch0145: 0145-man-document-forwarding-to-syslog-better.patch
Patch0146: 0146-man-fix-typos-in-previous-comimt.patch
Patch0147: 0147-LSB-always-add-network-online.target-to-services-wit.patch
Patch0148: 0148-rules-enable-memory-hotplug.patch
Patch0149: 0149-rules-reload-sysctl-settings-when-the-bridge-module-.patch
Patch0150: 0150-console-getty.service-don-t-start-when-dev-console-i.patch
Patch0151: 0151-resolved-Do-not-add-.busname-dependencies-when-compi.patch
Patch0152: 0152-man-add-journal-remote.conf-5.patch
Patch0153: 0153-mount-don-t-run-quotaon-only-for-network-filesystems.patch
Patch0154: 0154-mount-fix-up-wording-in-the-comment.patch
Patch0155: 0155-udev-net_id-fix-copy-paste-error.patch
Patch0156: 0156-man-don-t-mention-journalctl-dev-sda.patch
Patch0157: 0157-units-move-After-systemd-hwdb-update.service-depende.patch
Patch0158: 0158-units-explicitly-order-systemd-user-sessions.service.patch
Patch0159: 0159-zsh-completion-update-loginctl.patch
Patch0160: 0160-zsh-completion-add-missing-M-completion-for-journalc.patch
Patch0161: 0161-zsh-completion-update-hostnamectl.patch
Patch0162: 0162-shell-completion-systemctl-switch-root-verb.patch
Patch0163: 0163-core-automount-beef-up-error-message.patch
Patch0164: 0164-man-remove-fs-from-rootfsflags.patch
Patch0165: 0165-shared-fix-memleak.patch
Patch0166: 0166-udevd-fix-synchronization-with-settle-when-handling-.patch
Patch0167: 0167-python-systemd-fix-is_socket_inet-to-cope-with-ports.patch
Patch0168: 0168-man-fix-examples-indentation-in-tmpfiles.d-5.patch
Patch0169: 0169-systemctl-avoid-bumping-NOFILE-rlimit-unless-needed.patch
Patch0170: 0170-exit-status-Fix-NOTINSSTALLED-typo.patch
Patch0171: 0171-tmpfiles-there-s-no-systemd-forbid-user-logins.servi.patch
Patch0172: 0172-kmod-setup-load-ip_tables-kmod-at-boot.patch
Patch0173: 0173-util-Fix-assertion-in-split-on-missing.patch
Patch0174: 0174-units-set-KillMode-mixed-for-our-daemons-that-fork-w.patch
Patch0175: 0175-unit-don-t-add-automatic-dependencies-on-device-unit.patch
Patch0176: 0176-update-done-ignore-nanosecond-file-timestamp-compone.patch
Patch0177: 0177-sd-daemon-simplify-sd_pid_notify_with_fds.patch
Patch0178: 0178-fstab-generator-add-x-systemd.requires-and-x-systemd.patch
Patch0179: 0179-core-Fix-assertion-with-empty-Exec-paths.patch
Patch0180: 0180-rules-load-sg-module.patch
Patch0181: 0181-util-add-shell_maybe_quote-call-for-preparing-a-stri.patch
Patch0182: 0182-bus-util-be-more-verbose-if-dbus-job-fails.patch
Patch0183: 0183-notify-fix-badly-backported-help-message.patch
Patch0184: 0184-cryptsetup-craft-a-unique-ID-with-the-source-device.patch
Patch0185: 0185-systemctl-introduce-now-for-enable-disable-and-mask.patch
Patch0186: 0186-udev-also-create-old-sas-paths.patch
Patch0187: 0187-journald-do-not-strip-leading-whitespace-from-messag.patch
Patch0188: 0188-Revert-core-one-step-back-again-for-nspawn-we-actual.patch
Patch0189: 0189-bus-creds-always-set-SD_BUS_CREDS_PID-when-we-set-pi.patch
Patch0190: 0190-sd-bus-do-not-use-per-datagram-auxiliary-information.patch
Patch0191: 0191-sd-bus-store-selinux-context-at-connection-time.patch
Patch0192: 0192-journald-simplify-context-handling.patch
Patch0193: 0193-bash-completion-add-verb-set-property.patch
Patch0194: 0194-sd-bus-don-t-inherit-connection-creds-into-message-c.patch
Patch0195: 0195-udev-fix-crash-in-path_id-builtin.patch
Patch0196: 0196-sysv-generator-test-Fix-assertion.patch
Patch0197: 0197-man-avoid-line-break-in-url.patch
Patch0198: 0198-Add-VARIANT-as-a-standard-value-for-etc-os-release.patch
Patch0199: 0199-Fix-permissions-on-run-systemd-nspawn-locks.patch
Patch0200: 0200-generators-rename-add_-root-usr-_mount-to-add_-sysro.patch
Patch0201: 0201-Generate-systemd-fsck-root.service-in-the-initramfs.patch
Patch0202: 0202-units-fix-typo-in-systemd-resolved.service.patch
Patch0203: 0203-core-don-t-consider-umask-for-SocketMode.patch
Patch0204: 0204-timedate-fix-memory-leak-in-timedated.patch
Patch0205: 0205-coredump-make-sure-we-vacuum-by-default.patch
Patch0206: 0206-tmpfiles-don-t-fail-if-we-cannot-create-a-subvolume-.patch
Patch0207: 0207-resolved-fix-crash-when-shutting-down.patch
Patch0208: 0208-resolved-allow-DnsAnswer-objects-with-no-space-for-R.patch
Patch0209: 0209-id128-add-new-sd_id128_is_null-call.patch
Patch0210: 0210-journalctl-Improve-boot-ID-lookup.patch
Patch0211: 0211-test-hashmap-fix-an-assert.patch
Patch0212: 0212-units-make-sure-systemd-nspawn-.slice-instances-are-.patch
Patch0213: 0213-Revert-journald-audit-exit-gracefully-in-the-case-we.patch
Patch0214: 0214-journald-handle-more-gracefully-when-bind-fails-on-a.patch
Patch0215: 0215-udev-link-config-fix-corruption.patch
Patch0216: 0216-udev-net_id-Only-read-the-first-64-bytes-of-PCI-conf.patch
Patch0217: 0217-shared-generator-correct-path-to-systemd-fsck.patch
Patch0218: 0218-logind-Save-the-user-s-state-when-a-session-enters-S.patch
Patch0219: 0219-small-fix-ru-translation.patch
Patch0220: 0220-kmod-setup-don-t-warn-when-ipv6-can-t-be-loaded.patch
Patch0221: 0221-Partially-revert-ma-setup-simplify.patch
Patch0222: 0222-ima-setup-write-policy-one-line-at-a-time.patch
Patch0223: 0223-ata_id-unbotch-format-specifier.patch
Patch0224: 0224-install-explicitly-return-0-on-success.patch
Patch0225: 0225-systemd.service.xml-document-that-systemd-removes-th.patch
Patch0226: 0226-core-handle-log-target-null-when-calling-systemd-shu.patch
Patch0227: 0227-man-ProtectHome-protects-root-as-well.patch
Patch0228: 0228-timedatectl-trim-non-local-RTC-warning-to-80-chars-w.patch
Patch0229: 0229-escape-fix-exit-code.patch
Patch0230: 0230-man-information-about-available-properties.patch
Patch0231: 0231-journal-in-persistent-mode-create-var-log-journal-wi.patch
Patch0232: 0232-sysv-generator-fix-wrong-Overwriting-existing-symlin.patch
Patch0233: 0233-mount-don-t-claim-a-device-is-gone-from-proc-self-mo.patch
Patch0234: 0234-mount-properly-check-for-mounts-currently-in-proc-se.patch
Patch0235: 0235-units-add-Install-section-to-tmp.mount.patch
Patch0236: 0236-bus-util-add-articles-to-explanation-messages.patch
Patch0237: 0237-bus-util-print-correct-warnings-for-units-that-fail-.patch
Patch0238: 0238-Revert-journald-move-dev-log-socket-to-run.patch
Patch0239: 0239-journald-server-don-t-read-audit-events.patch
Patch0240: 0240-everything-remove-traces-of-user.patch
Patch0241: 0241-selinux-fix-check-for-transient-units.patch
Patch0242: 0242-socket-fix-setsockopt-call.-SOL_SOCKET-changed-to-SO.patch
Patch0243: 0243-selinux-fix-missing-SELinux-unit-access-check.patch
Patch0244: 0244-selinux-always-use-_raw-API-from-libselinux.patch
Patch0245: 0245-udev-net_id-support-predictable-ifnames-on-virtio-bu.patch
Patch0246: 0246-Revert-sysctl.d-default-to-fq_codel-fight-bufferbloa.patch
Patch0247: 0247-loginctl-print-nontrivial-properties-in-logictl-show.patch
Patch0248: 0248-login-fix-label-on-run-nologin.patch
Patch0249: 0249-udev-rules-prandom-character-device-node-permissions.patch
Patch0250: 0250-login-fix-gcc-warning-include-missing-header-file.patch
Patch0251: 0251-shutdown-make-sure-run-nologin-has-correct-label.patch
Patch0252: 0252-sd-event-fix-prepare-priority-queue-comparison-funct.patch
Patch0253: 0253-units-run-ldconfig-also-when-cache-is-unpopulated.patch
Patch0254: 0254-selinux-fix-regression-of-systemctl-subcommands-when.patch
Patch0255: 0255-tmpfiles.d-don-t-clean-SAP-lockfiles-and-logs.patch
Patch0256: 0256-udev-make-naming-for-virtio-devices-opt-in.patch
Patch0257: 0257-tmpfiles.d-don-t-clean-SAP-sockets-either.patch


%global num_patches %{lua: c=0; for i,p in ipairs(patches) do c=c+1; end; print(c);}

BuildRequires:  libcap-devel
BuildRequires:  tcp_wrappers-devel
BuildRequires:  pam-devel
BuildRequires:  libselinux-devel
BuildRequires:  audit-libs-devel
BuildRequires:  cryptsetup-devel
BuildRequires:  dbus-devel
BuildRequires:  libacl-devel
BuildRequires:  pciutils-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libblkid-devel
BuildRequires:  xz-devel
BuildRequires:  libidn-devel
BuildRequires:  libcurl-devel
BuildRequires:  kmod-devel
BuildRequires:  elfutils-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  gnutls-devel
BuildRequires:  qrencode-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  pkgconfig
BuildRequires:  intltool
BuildRequires:  gperf
BuildRequires:  gawk
BuildRequires:  gtk-doc
BuildRequires:  python2-devel
BuildRequires:  python-lxml
%ifarch x86_64 i686
#BuildRequires:  libseccomp-devel
%endif
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  git
BuildRequires:  libmount-devel

Requires(post): coreutils
Requires(post): gawk
Requires(post): sed
Requires(post): acl
Requires(pre):  coreutils
Requires(pre):  /usr/bin/getent
Requires(pre):  /usr/sbin/groupadd
Requires:       dbus
Requires:       %{name}-libs = %{version}-%{release}
Requires:       kmod >= 18-4
Requires:       redhat-release >= 7.0
Requires:       diffutils
Provides:       /bin/systemctl
Provides:       /sbin/shutdown
Provides:       syslog
Provides:       systemd-units = %{version}-%{release}
Provides:       udev = %{version}
Obsoletes:      udev < 183
Obsoletes:      system-setup-keyboard < 0.9
Provides:       system-setup-keyboard = 0.9
Obsoletes:      nss-myhostname < 0.4
Provides:       nss-myhostname = 0.4
# systemd-analyze got merged in F19, drop at F21
Obsoletes:      systemd-analyze < 198
Provides:       systemd-analyze = 198
Obsoletes:      upstart < 1.2-3
Obsoletes:      upstart-sysvinit < 1.2-3
Conflicts:      upstart-sysvinit
Obsoletes:      hal
Obsoletes:      ConsoleKit
Conflicts:      dracut < 033-243
Conflicts:      initscripts < 9.49.28-1

%description
systemd is a system and service manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

%package libs
Summary:        systemd libraries
License:        LGPLv2+ and MIT
Obsoletes:      libudev < 183
Obsoletes:      systemd < 185-4
Conflicts:      systemd < 185-4

%description libs
Libraries for systemd and udev, as well as the systemd PAM module.

%package devel
Summary:        Development headers for systemd
License:        LGPLv2+ and MIT
Requires:       %{name} = %{version}-%{release}
Provides:       libudev-devel = %{version}
Obsoletes:      libudev-devel < 183

%description devel
Development headers and auxiliary files for developing applications for systemd.

%package sysv
Summary:        SysV tools for systemd
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}

%description sysv
SysV compatibility tools for systemd

%package python
Summary:        Python 2 bindings for systemd
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}

%description python
This package contains bindings which allow Python 2 programs to use
systemd APIs

%package -n libgudev1
Summary:        Libraries for adding libudev support to applications that use glib
Conflicts:      filesystem < 3
License:        LGPLv2+
Requires:       %{name}-libs = %{version}-%{release}

%description -n libgudev1
This package contains the libraries that make it easier to use libudev
functionality from applications that use glib.

%package -n libgudev1-devel
Summary:        Header files for adding libudev support to applications that use glib
Requires:       libgudev1 = %{version}-%{release}
License:        LGPLv2+

%description -n libgudev1-devel
This package contains the header and pkg-config files for developing
glib-based applications using libudev functionality.

%package journal-gateway
Summary:        Gateway for serving journal events over the network using HTTP
Requires:       %{name} = %{version}-%{release}
License:        LGPLv2+
Requires(pre):    /usr/bin/getent
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description journal-gateway
systemd-journal-gatewayd serves journal events over the network using HTTP.

%package networkd
Summary:        System service that manages networks.
Requires:       %{name} = %{version}-%{release}
License:        LGPLv2+
Requires(pre):    /usr/bin/getent
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description networkd
systemd-networkd is a system service that manages networks.
It detects and configures network devices as they appear, as well as creating virtual network devices.

%package resolved
Summary:        Network Name Resolution manager.
Requires:       %{name} = %{version}-%{release}
License:        LGPLv2+
Requires(pre):    /usr/bin/getent
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description resolved
systemd-resolved is a system service that manages network name resolution.
It implements a caching DNS stub resolver and an LLMNR resolver and responder.

%prep
%setup -q

%if %{num_patches}
git init
git config user.email "systemd-maint@redhat.com"
git config user.name "systemd team"
git add .
git commit -a -q -m "%{version} baseline."

# Apply all the patches.
git am \
--exclude .gitignore \
--exclude docs/.gitignore \
--exclude docs/gudev/.gitignore \
--exclude docs/libudev/.gitignore \
--exclude docs/sysvinit/.gitignore \
--exclude docs/var-log/.gitignore \
--exclude hwdb/.gitignore \
--exclude m4/.gitignore \
--exclude man/.gitignore \
--exclude po/.gitignore \
--exclude rules/.gitignore \
--exclude src/.gitignore \
--exclude src/analyze/.gitignore \
--exclude src/core/.gitignore \
--exclude src/gudev/.gitignore \
--exclude src/hostname/.gitignore \
--exclude src/journal/.gitignore \
--exclude src/libsystemd-daemon/.gitignore \
--exclude src/libsystemd-id128/.gitignore \
--exclude src/libudev/.gitignore \
--exclude src/locale/.gitignore \
--exclude src/login/.gitignore \
--exclude src/python-systemd/.gitignore \
--exclude tmpfiles.d/systemd.conf.m4 \
--exclude src/python-systemd/docs/.gitignore \
--exclude src/timedate/.gitignore \
--exclude src/udev/.gitignore \
--exclude src/udev/scsi_id/.gitignore \
--exclude sysctl.d/.gitignore \
--exclude test/.gitignore \
--exclude units/.gitignore \
--exclude units/user/.gitignore \
--exclude src/libsystemd/sd-bus/PORTING-DBUS1 \
--exclude CODING_STYLE \
--exclude src/readahead/Makefile \
--exclude src/libsystemd-terminal/unifont-def.h \
--exclude hwdb/sdio.ids \
%{patches}
%endif

%build
autoreconf -i

CONFIGURE_OPTS=(
--libexecdir=%{_prefix}/lib
--with-sysvinit-path=/etc/rc.d/init.d
--with-rc-local-script-path-start=/etc/rc.d/rc.local
--disable-timesyncd
--disable-kdbus
--disable-terminal
--disable-importd
--enable-gtk-doc
--enable-compat-libs
--disable-sysusers
%ifarch s390 s390x ppc %{power64} aarch64
--disable-lto
%endif
)


%configure "${CONFIGURE_OPTS[@]}"
make %{?_smp_mflags} GCC_COLORS="" V=1

%install
%make_install

find %{buildroot} \( -name '*.a' -o -name '*.la' \) -delete
sed -i 's/L+/#/' %{buildroot}/usr/lib/tmpfiles.d/etc.conf

# udev links
mkdir -p %{buildroot}/%{_sbindir}
ln -sf ../bin/udevadm %{buildroot}%{_sbindir}/udevadm

# Create SysV compatibility symlinks. systemctl/systemd are smart
# enough to detect in which way they are called.
ln -s ../lib/systemd/systemd %{buildroot}%{_sbindir}/init
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/reboot
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/halt
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/poweroff
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/shutdown
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/telinit
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/runlevel

# legacy links
ln -s loginctl %{buildroot}%{_bindir}/systemd-loginctl
ln -s coredumpctl %{buildroot}%{_bindir}/systemd-coredumpctl

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the user deleted
# them.
rm -r %{buildroot}%{_sysconfdir}/systemd/system/*.target.wants

# Make sure the ghost-ing below works
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel2.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel3.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel4.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel5.target

# Make sure these directories are properly owned
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/basic.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/default.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/dbus.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/syslog.target.wants

# Temporary workaround for #1002806
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/poweroff.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/rescue.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/multi-user.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/graphical.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/reboot.target.wants
ln -s ../systemd-update-utmp-runlevel.service %{buildroot}%{_prefix}/lib/systemd/system/poweroff.target.wants/
ln -s ../systemd-update-utmp-runlevel.service %{buildroot}%{_prefix}/lib/systemd/system/rescue.target.wants/
ln -s ../systemd-update-utmp-runlevel.service %{buildroot}%{_prefix}/lib/systemd/system/multi-user.target.wants/
ln -s ../systemd-update-utmp-runlevel.service %{buildroot}%{_prefix}/lib/systemd/system/graphical.target.wants/
ln -s ../systemd-update-utmp-runlevel.service %{buildroot}%{_prefix}/lib/systemd/system/reboot.target.wants/

mkdir -p %{buildroot}%{_localstatedir}/{run,log}/
touch %{buildroot}%{_localstatedir}/run/utmp
touch %{buildroot}%{_localstatedir}/log/{w,b}tmp

# Make sure the user generators dir exists too
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-generators
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user-generators

# Create new-style configuration files so that we can ghost-own them
touch %{buildroot}%{_sysconfdir}/hostname
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/machine-id
touch %{buildroot}%{_sysconfdir}/machine-info
touch %{buildroot}%{_sysconfdir}/localtime
mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d
touch %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf

# Install default preset policy
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset/
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user-preset/
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/systemd/system-preset/

# Make sure the shutdown/sleep drop-in dirs exist
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-shutdown/
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-sleep/

# Make sure the NTP units dir exists
mkdir -p %{buildroot}%{_prefix}/lib/systemd/ntp-units.d/

# Make sure directories in /var exist
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/coredump
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/catalog
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/backlight
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/rfkill
touch %{buildroot}%{_localstatedir}/lib/systemd/catalog/database
touch %{buildroot}%{_sysconfdir}/udev/hwdb.bin
touch %{buildroot}%{_localstatedir}/lib/systemd/random-seed
touch %{buildroot}%{_localstatedir}/lib/systemd/clock


# Install SysV conversion tool for systemd
install -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/

# Install yum protection fragment
mkdir -p %{buildroot}%{_sysconfdir}/yum/protected.d/
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/yum/protected.d/systemd.conf

# Install rc.local
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/rc.d/rc.local
ln -s rc.d/rc.local %{buildroot}%{_sysconfdir}/rc.local

# Install rsyslog fragment
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d/
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/rsyslog.d/

# Delete LICENSE files from _docdir (we'll get them in as %%license)
rm -rf %{buildroot}%{_docdir}/LICENSE*

%find_lang %{name}

# To avoid making life hard for Rawhide-using developers, don't package the
# kernel.core_pattern setting until systemd-coredump is a part of an actual
# systemd release and it's made clear how to get the core dumps out of the
# journal.
rm -f %{buildroot}%{_prefix}/lib/sysctl.d/50-coredump.conf

# For now remove /var/log/README since we are not enabling persistant
# logging yet.
rm -f %{buildroot}%{_localstatedir}/log/README

# No tmp-on-tmpfs by default in RHEL7. bz#876122
rm -f %{buildroot}%{_prefix}/lib/systemd/system/local-fs.target.wants/tmp.mount

# No gpt-auto-generator in RHEL7
rm -f %{buildroot}%{_prefix}/lib/systemd/system-generators/systemd-gpt-auto-generator

# 50-bridge.conf rules are in intscripts
rm -f %{buildroot}%{_prefix}/lib/sysctl.d/50-bridge.conf

# no networkd in rhel7
rm -f %{buildroot}%{_prefix}/lib/systemd/network/*

install -m 0644 %{SOURCE5} $RPM_BUILD_ROOT/%{_udevrulesdir}/

%pre
getent group cdrom >/dev/null 2>&1 || groupadd -r -g 11 cdrom >/dev/null 2>&1 || :
getent group utmp >/dev/null 2>&1 || groupadd -r -g 22 utmp >/dev/null 2>&1 || :
getent group tape >/dev/null 2>&1 || groupadd -r -g 33 tape >/dev/null 2>&1 || :
getent group dialout >/dev/null 2>&1 || groupadd -r -g 18 dialout >/dev/null 2>&1 || :
getent group input >/dev/null 2>&1 || groupadd -r input >/dev/null 2>&1 || :
getent group floppy >/dev/null 2>&1 || groupadd -r -g 19 floppy >/dev/null 2>&1 || :
getent group systemd-journal >/dev/null 2>&1 || groupadd -r -g 190 systemd-journal 2>&1 || :
getent group systemd-bus-proxy >/dev/null 2>&1 || groupadd -r systemd-bus-proxy 2>&1 || :
getent passwd systemd-bus-proxy >/dev/null 2>&1 || useradd -r -l -g systemd-bus-proxy -d / -s /sbin/nologin -c "systemd Bus Proxy" systemd-bus-proxy >/dev/null 2>&1 || :
getent group systemd-network >/dev/null 2>&1 || groupadd -r systemd-network 2>&1 || :
getent passwd systemd-network >/dev/null 2>&1 || useradd -r -l -g systemd-network -d / -s /sbin/nologin -c "systemd Network Management" systemd-network >/dev/null 2>&1 || :

systemctl stop systemd-udevd-control.socket systemd-udevd-kernel.socket systemd-udevd.service >/dev/null 2>&1 || :

%post
systemd-machine-id-setup >/dev/null 2>&1 || :
/usr/lib/systemd/systemd-random-seed save >/dev/null 2>&1 || :
systemctl daemon-reexec >/dev/null 2>&1 || :
systemctl start systemd-udevd.service >/dev/null 2>&1 || :
udevadm hwdb --update >/dev/null 2>&1 || :
journalctl --update-catalog >/dev/null 2>&1 || :
systemd-tmpfiles --create >/dev/null 2>&1 || :

# Make sure new journal files will be owned by the "systemd-journal" group
chgrp systemd-journal /run/log/journal/ /run/log/journal/`cat /etc/machine-id 2> /dev/null` /var/log/journal/ /var/log/journal/`cat /etc/machine-id 2> /dev/null` >/dev/null 2>&1 || :
chmod g+s /run/log/journal/ /run/log/journal/`cat /etc/machine-id 2> /dev/null` /var/log/journal/ /var/log/journal/`cat /etc/machine-id 2> /dev/null` >/dev/null 2>&1 || :

if [ $1 -eq 1 ] ; then
# Try to read default runlevel from the old inittab if it exists
runlevel=$(awk -F ':' '$3 == "initdefault" && $1 !~ "^#" { print $2 }' /etc/inittab 2> /dev/null)
if [ -z "$runlevel" ] ; then
target="/usr/lib/systemd/system/graphical.target"
else
target="/usr/lib/systemd/system/runlevel$runlevel.target"
fi

# And symlink what we found to the new-style default.target
ln -sf "$target" /etc/systemd/system/default.target >/dev/null 2>&1 || :

# Services we install by default, and which are controlled by presets.
systemctl preset \
remote-fs.target \
getty@.service \
serial-getty@.service \
console-getty.service \
console-shell.service \
debug-shell.service \
systemd-readahead-replay.service \
systemd-readahead-collect.service \
>/dev/null 2>&1 || :
else
# This systemd service does not exist anymore, we now do it
# internally in PID 1
rm -f /etc/systemd/system/sysinit.target.wants/hwclock-load.service >/dev/null 2>&1 || :

# This systemd target does not exist anymore. It's been replaced
# by ntp-units.d.
rm -f /etc/systemd/system/multi-user.target.wants/systemd-timedated-ntp.target >/dev/null 2>&1 || :

# Enable the units recorded by %%pretrans
if [ -e /var/lib/rpm-state/systemd/ntp-units ] ; then
while read service; do
systemctl enable "$service" >/dev/null 2>&1 || :
done < /var/lib/rpm-state/systemd/ntp-units
rm -r /var/lib/rpm-state/systemd/ntp-units >/dev/null 2>&1 || :
fi
fi

# Move old stuff around in /var/lib
mv %{_localstatedir}/lib/random-seed %{_localstatedir}/lib/systemd/random-seed >/dev/null 2>&1 || :
mv %{_localstatedir}/lib/backlight %{_localstatedir}/lib/systemd/backlight >/dev/null 2>&1 || :

# Migrate /etc/sysconfig/clock
if [ ! -L /etc/localtime -a -e /etc/sysconfig/clock ] ; then
. /etc/sysconfig/clock >/dev/null 2>&1 || :
if [ -n "$ZONE" -a -e "/usr/share/zoneinfo/$ZONE" ] ; then
ln -sf "../usr/share/zoneinfo/$ZONE" /etc/localtime >/dev/null 2>&1 || :
fi
fi
rm -f /etc/sysconfig/clock >/dev/null 2>&1 || :

# Migrate /etc/sysconfig/i18n
if [ -e /etc/sysconfig/i18n -a ! -e /etc/locale.conf ]; then
unset LANG
unset LC_CTYPE
unset LC_NUMERIC
unset LC_TIME
unset LC_COLLATE
unset LC_MONETARY
unset LC_MESSAGES
unset LC_PAPER
unset LC_NAME
unset LC_ADDRESS
unset LC_TELEPHONE
unset LC_MEASUREMENT
unset LC_IDENTIFICATION
. /etc/sysconfig/i18n >/dev/null 2>&1 || :
[ -n "$LANG" ] && echo LANG=$LANG > /etc/locale.conf 2>&1 || :
[ -n "$LC_CTYPE" ] && echo LC_CTYPE=$LC_CTYPE >> /etc/locale.conf 2>&1 || :
[ -n "$LC_NUMERIC" ] && echo LC_NUMERIC=$LC_NUMERIC >> /etc/locale.conf 2>&1 || :
[ -n "$LC_TIME" ] && echo LC_TIME=$LC_TIME >> /etc/locale.conf 2>&1 || :
[ -n "$LC_COLLATE" ] && echo LC_COLLATE=$LC_COLLATE >> /etc/locale.conf 2>&1 || :
[ -n "$LC_MONETARY" ] && echo LC_MONETARY=$LC_MONETARY >> /etc/locale.conf 2>&1 || :
[ -n "$LC_MESSAGES" ] && echo LC_MESSAGES=$LC_MESSAGES >> /etc/locale.conf 2>&1 || :
[ -n "$LC_PAPER" ] && echo LC_PAPER=$LC_PAPER >> /etc/locale.conf 2>&1 || :
[ -n "$LC_NAME" ] && echo LC_NAME=$LC_NAME >> /etc/locale.conf 2>&1 || :
[ -n "$LC_ADDRESS" ] && echo LC_ADDRESS=$LC_ADDRESS >> /etc/locale.conf 2>&1 || :
[ -n "$LC_TELEPHONE" ] && echo LC_TELEPHONE=$LC_TELEPHONE >> /etc/locale.conf 2>&1 || :
[ -n "$LC_MEASUREMENT" ] && echo LC_MEASUREMENT=$LC_MEASUREMENT >> /etc/locale.conf 2>&1 || :
[ -n "$LC_IDENTIFICATION" ] && echo LC_IDENTIFICATION=$LC_IDENTIFICATION >> /etc/locale.conf 2>&1 || :
fi

# Migrate /etc/sysconfig/keyboard
if [ -e /etc/sysconfig/keyboard -a ! -e /etc/vconsole.conf ]; then
unset SYSFONT
unset SYSFONTACM
unset UNIMAP
unset KEYMAP
[ -e /etc/sysconfig/i18n ] && . /etc/sysconfig/i18n >/dev/null 2>&1 || :
. /etc/sysconfig/keyboard >/dev/null 2>&1 || :
[ -n "$SYSFONT" ] && echo FONT=$SYSFONT > /etc/vconsole.conf 2>&1 || :
[ -n "$SYSFONTACM" ] && echo FONT_MAP=$SYSFONTACM >> /etc/vconsole.conf 2>&1 || :
[ -n "$UNIMAP" ] && echo FONT_UNIMAP=$UNIMAP >> /etc/vconsole.conf 2>&1 || :
[ -n "$KEYTABLE" ] && echo KEYMAP=$KEYTABLE >> /etc/vconsole.conf 2>&1 || :
fi
rm -f /etc/sysconfig/i18n >/dev/null 2>&1 || :
rm -f /etc/sysconfig/keyboard >/dev/null 2>&1 || :

# Migrate HOSTNAME= from /etc/sysconfig/network
if [ -e /etc/sysconfig/network -a ! -e /etc/hostname ]; then
unset HOSTNAME
. /etc/sysconfig/network >/dev/null 2>&1 || :
[ -n "$HOSTNAME" ] && echo $HOSTNAME > /etc/hostname 2>&1 || :
fi
sed -i '/^HOSTNAME=/d' /etc/sysconfig/network >/dev/null 2>&1 || :

# Migrate the old systemd-setup-keyboard X11 configuration fragment
if [ ! -e /etc/X11/xorg.conf.d/00-keyboard.conf ] ; then
mv /etc/X11/xorg.conf.d/00-system-setup-keyboard.conf /etc/X11/xorg.conf.d/00-keyboard.conf >/dev/null 2>&1 || :
else
rm -f /etc/X11/xorg.conf.d/00-system-setup-keyboard.conf >/dev/null 2>&1 || :
fi

# sed-fu to add myhostname to the hosts line of /etc/nsswitch.conf
if [ -f /etc/nsswitch.conf ] ; then
sed -i.bak -e '
/^hosts:/ !b
/\<myhostname\>/ b
s/[[:blank:]]*$/ myhostname/
' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi

%posttrans
# Convert old /etc/sysconfig/desktop settings
preferred=
if [ -f /etc/sysconfig/desktop ]; then
. /etc/sysconfig/desktop
if [ "$DISPLAYMANAGER" = GNOME ]; then
preferred=gdm
elif [ "$DISPLAYMANAGER" = KDE ]; then
preferred=kdm
elif [ "$DISPLAYMANAGER" = WDM ]; then
preferred=wdm
elif [ "$DISPLAYMANAGER" = XDM ]; then
preferred=xdm
elif [ -n "$DISPLAYMANAGER" ]; then
preferred=${DISPLAYMANAGER##*/}
fi
fi
if [ -z "$preferred" ]; then
if [ -x /usr/sbin/gdm ]; then
preferred=gdm
elif [ -x /usr/bin/kdm ]; then
preferred=kdm
fi
fi
if [ -n "$preferred" -a -r "/usr/lib/systemd/system/$preferred.service" ]; then
# This is supposed to fail when the symlink already exists
ln -s "/usr/lib/systemd/system/$preferred.service" /etc/systemd/system/display-manager.service >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ] ; then
systemctl daemon-reload > /dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
systemctl disable \
remote-fs.target \
getty@.service \
serial-getty@.service \
console-getty.service \
console-shell.service \
debug-shell.service \
systemd-readahead-replay.service \
systemd-readahead-collect.service \
>/dev/null 2>&1 || :

rm -f /etc/systemd/system/default.target >/dev/null 2>&1 || :

if [ -f /etc/nsswitch.conf ] ; then
sed -i.bak -e '
/^hosts:/ !b
s/[[:blank:]]\+myhostname\>//
' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi
fi

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post -n libgudev1 -p /sbin/ldconfig
%postun -n libgudev1 -p /sbin/ldconfig

%pre journal-gateway
getent group systemd-journal-gateway >/dev/null 2>&1 || groupadd -r -g 191 systemd-journal-gateway 2>&1 || :
getent passwd systemd-journal-gateway >/dev/null 2>&1 || useradd -r -l -u 191 -g systemd-journal-gateway -d %{_localstatedir}/log/journal -s /sbin/nologin -c "Journal Gateway" systemd-journal-gateway >/dev/null 2>&1 || :
getent group systemd-journal-remote >/dev/null 2>&1 || groupadd -r systemd-journal-remote 2>&1 || :
getent passwd systemd-journal-remote >/dev/null 2>&1 || useradd -r -l -g systemd-journal-remote -d /%{_localstatedir}/log/journal/remote -s /sbin/nologin -c "Journal Remote" systemd-journal-remote >/dev/null 2>&1 || :
getent group systemd-journal-upload >/dev/null 2>&1 || groupadd -r systemd-journal-upload 2>&1 || :
getent passwd systemd-journal-upload >/dev/null 2>&1 || useradd -r -l -g systemd-journal-upload -d /%{_localstatedir}/log/journal/upload -s /sbin/nologin -c "Journal Upload" systemd-journal-upload >/dev/null 2>&1 || :

%post journal-gateway
%systemd_post systemd-journal-gatewayd.socket systemd-journal-gatewayd.service
%systemd_post systemd-journal-remote.socket systemd-journal-remote.service
%systemd_post systemd-journal-upload.service

%preun journal-gateway
%systemd_preun systemd-journal-gatewayd.socket systemd-journal-gatewayd.service
%systemd_preun systemd-journal-remote.socket systemd-journal-remote.service
%systemd_preun systemd-journal-upload.service

%postun journal-gateway
%systemd_postun_with_restart systemd-journal-gatewayd.service
%systemd_postun_with_restart systemd-journal-remote.service
%systemd_postun_with_restart systemd-journal-upload.service

%post networkd
%systemd_post systemd-networkd.service systemd-networkd-wait-online.service

%preun networkd
%systemd_preun systemd-networkd.service systemd-networkd-wait-online.service

%postun networkd
%systemd_postun_with_restart systemd-networkd.service systemd-networkd-wait-online.service

%pre resolved
getent group systemd-resolve >/dev/null 2>&1 || groupadd -r systemd-resolve 2>&1 || :
getent passwd systemd-resolve >/dev/null 2>&1 || useradd -r -l -g systemd-resolve -d / -s /sbin/nologin -c "systemd Resolver" systemd-resolve >/dev/null 2>&1 || :

%post resolved
%systemd_post systemd-resolved.service

%preun resolved
%systemd_preun systemd-resolved.service

%postun resolved
%systemd_postun_with_restart systemd-resolved.service

%files -f %{name}.lang
%doc %{_docdir}/systemd
%{!?_licensedir:%global license %%doc}
%license LICENSE.GPL2 LICENSE.LGPL2.1 LICENSE.MIT
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%dir %{_sysconfdir}/systemd/user
%dir %{_sysconfdir}/tmpfiles.d
%dir %{_sysconfdir}/sysctl.d
%dir %{_sysconfdir}/modules-load.d
%dir %{_sysconfdir}/binfmt.d
%dir %{_sysconfdir}/udev
%dir %{_sysconfdir}/udev/rules.d
%dir %{_prefix}/lib/systemd
%{_prefix}/lib/systemd/system-generators
%{_prefix}/lib/systemd/user-generators
%dir %{_prefix}/lib/systemd/system-preset
%dir %{_prefix}/lib/systemd/user-preset
%dir %{_prefix}/lib/systemd/system-shutdown
%dir %{_prefix}/lib/systemd/system-sleep
%dir %{_prefix}/lib/systemd/catalog
%dir %{_prefix}/lib/systemd/ntp-units.d
%dir %{_prefix}/lib/tmpfiles.d
#%dir %{_prefix}/lib/sysusers.d
%dir %{_prefix}/lib/sysctl.d
%dir %{_prefix}/lib/modules-load.d
%dir %{_prefix}/lib/binfmt.d
%dir %{_prefix}/lib/kernel
%dir %{_prefix}/lib/kernel/install.d
%dir %{_datadir}/systemd
%dir %{_datadir}/pkgconfig
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%ghost %dir %{_localstatedir}/log/journal
%dir %{_localstatedir}/lib/systemd
%dir %{_localstatedir}/lib/systemd/catalog
%ghost %dir %{_localstatedir}/lib/systemd/coredump
%ghost %dir %{_localstatedir}/lib/systemd/backlight
%ghost %dir %{_localstatedir}/lib/systemd/rfkill
%ghost %{_localstatedir}/lib/systemd/random-seed
%ghost %{_localstatedir}/lib/systemd/clock
%ghost %{_localstatedir}/lib/systemd/catalog/database
%ghost %attr(0664,root,utmp) %{_localstatedir}/run/utmp
%ghost %attr(0664,root,utmp) %{_localstatedir}/log/wtmp
%ghost %attr(0600,root,utmp) %{_localstatedir}/log/btmp
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.login1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.locale1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.machine1.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %{_sysconfdir}/systemd/user.conf
%config(noreplace) %{_sysconfdir}/systemd/logind.conf
%config(noreplace) %{_sysconfdir}/systemd/journald.conf
%config(noreplace) %{_sysconfdir}/systemd/bootchart.conf
%config(noreplace) %{_sysconfdir}/systemd/coredump.conf
%config(noreplace) %{_sysconfdir}/udev/udev.conf
%config(noreplace) %{_sysconfdir}/rsyslog.d/listen.conf
%config(noreplace) %{_sysconfdir}/yum/protected.d/systemd.conf
%config(noreplace) %{_sysconfdir}/pam.d/systemd-user
%ghost %{_sysconfdir}/udev/hwdb.bin
%{_rpmconfigdir}/macros.d/macros.systemd
%{_sysconfdir}/xdg/systemd
%{_sysconfdir}/rc.d/init.d/README
%ghost %config(noreplace) %{_sysconfdir}/hostname
%ghost %config(noreplace) %{_sysconfdir}/localtime
%ghost %config(noreplace) %{_sysconfdir}/vconsole.conf
%ghost %config(noreplace) %{_sysconfdir}/locale.conf
%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info
%dir %{_sysconfdir}/X11/xorg.conf.d
%ghost %config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf
%{_bindir}/systemctl
%{_bindir}/systemd-notify
%{_bindir}/systemd-analyze
%{_bindir}/systemd-escape
%{_bindir}/systemd-ask-password
%{_bindir}/systemd-tty-ask-password-agent
%{_bindir}/systemd-machine-id-setup
%{_bindir}/loginctl
%{_bindir}/systemd-loginctl
%{_bindir}/journalctl
%{_bindir}/machinectl
%{_bindir}/busctl
%{_bindir}/coredumpctl
%{_bindir}/systemd-coredumpctl
%{_bindir}/systemd-tmpfiles
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-stdio-bridge
%{_bindir}/systemd-cat
%{_bindir}/systemd-cgls
%{_bindir}/systemd-cgtop
%{_bindir}/systemd-delta
%{_bindir}/systemd-run
%{_bindir}/systemd-detect-virt
%{_bindir}/systemd-inhibit
%{_bindir}/systemd-path
#%{_bindir}/systemd-sysusers
%{_bindir}/systemd-firstboot
%{_bindir}/hostnamectl
%{_bindir}/localectl
%{_bindir}/timedatectl
%{_bindir}/bootctl
%{_bindir}/udevadm
%{_bindir}/kernel-install
%{_bindir}/systemd-hwdb
%{_prefix}/lib/systemd/systemd
%exclude %{_prefix}/lib/systemd/system/systemd-journal-gatewayd.*
%exclude %{_prefix}/lib/systemd/system/systemd-journal-remote.*
%exclude %{_prefix}/lib/systemd/system/systemd-journal-upload.*
%exclude %{_prefix}/lib/systemd/system/systemd-networkd.service
%exclude %{_prefix}/lib/systemd/system/systemd-networkd-wait-online.service
%exclude %{_prefix}/lib/systemd/system/systemd-resolved.service
%exclude %{_prefix}/lib/systemd/system/dbus-org.freedesktop.resolve1.service
%{_prefix}/lib/systemd/system
%{_prefix}/lib/systemd/user
%exclude %{_prefix}/lib/systemd/systemd-journal-gatewayd
%exclude %{_prefix}/lib/systemd/systemd-journal-remote
%exclude %{_prefix}/lib/systemd/systemd-networkd
%exclude %{_prefix}/lib/systemd/systemd-networkd-wait-online
%exclude %{_prefix}/lib/systemd/systemd-resolved
%exclude %{_prefix}/lib/systemd/systemd-resolve-host
%exclude %{_prefix}/lib/systemd/systemd-journal-upload
%{_prefix}/lib/systemd/systemd-*
%{_prefix}/lib/udev
%exclude  %{_sysconfdir}/udev/rules.d/80-net-setup-link.rules
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/systemd-nologin.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/tmpfiles.d/var.conf
%{_prefix}/lib/tmpfiles.d/etc.conf
%{_prefix}/lib/tmpfiles.d/sap.conf
%{_prefix}/lib/sysctl.d/50-default.conf
#%{_prefix}/lib/sysusers.d/basic.conf
#%{_prefix}/lib/sysusers.d/systemd.conf
%{_prefix}/lib/systemd/system-preset/90-systemd.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset
%{_prefix}/lib/systemd/catalog/systemd.catalog
%{_prefix}/lib/kernel/install.d/50-depmod.install
%{_prefix}/lib/kernel/install.d/90-loaderentry.install
%{_sbindir}/init
%{_sbindir}/reboot
%{_sbindir}/halt
%{_sbindir}/poweroff
%{_sbindir}/shutdown
%{_sbindir}/telinit
%{_sbindir}/runlevel
%{_sbindir}/udevadm
%{_mandir}/man1/*
%exclude %{_mandir}/man5/systemd.network.*
%exclude %{_mandir}/man5/systemd.netdev.*
%exclude %{_mandir}/man5/systemd.link.*
%exclude %{_mandir}/man5/resolved.conf.*
%{_mandir}/man5/*
%{_mandir}/man7/*
%exclude %{_mandir}/man8/systemd-journal-gatewayd.*
%exclude %{_mandir}/man8/systemd-journal-remote.*
%exclude %{_mandir}/man8/systemd-networkd.*
%exclude %{_mandir}/man8/systemd-resolved.*
%{_mandir}/man8/*
#%{_datadir}/factory/etc/nsswitch.conf
#%{_datadir}/factory/etc/pam.d/other
#%{_datadir}/factory/etc/pam.d/system-auth
%{_datadir}/systemd/kbd-model-map
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.login1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.locale1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timedate1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.machine1.service
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.hostname1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.login1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.locale1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.timedate1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.machine1.policy
%{_libdir}/pkgconfig/systemd.pc
%{_datadir}/pkgconfig/udev.pc
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/*
%{_prefix}/lib/systemd/catalog/systemd.*.catalog
%config(noreplace) %{_sysconfdir}/rc.d/rc.local
%{_sysconfdir}/rc.local
%{_datadir}/systemd/language-fallback-map

# Make sure we don't remove runlevel targets from F14 alpha installs,
# but make sure we don't create then anew.
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel2.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel3.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel4.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel5.target

%files libs
%{_libdir}/security/pam_systemd.so
%{_libdir}/libnss_myhostname.so.2
%{_libdir}/libnss_mymachines.so.2
%{_libdir}/libudev.so.*
%{_libdir}/libsystemd.so.*
%{_libdir}/libsystemd-daemon.so.*
%{_libdir}/libsystemd-login.so.*
%{_libdir}/libsystemd-journal.so.*
%{_libdir}/libsystemd-id128.so.*

%files devel
%dir %{_includedir}/systemd
%{_libdir}/libudev.so
%{_libdir}/libsystemd.so
%{_libdir}/libsystemd-daemon.so
%{_libdir}/libsystemd-login.so
%{_libdir}/libsystemd-journal.so
%{_libdir}/libsystemd-id128.so
%{_includedir}/systemd/sd-daemon.h
%{_includedir}/systemd/sd-login.h
%{_includedir}/systemd/sd-journal.h
%{_includedir}/systemd/sd-id128.h
%{_includedir}/systemd/sd-messages.h
%{_includedir}/systemd/_sd-common.h
%{_includedir}/libudev.h
%{_libdir}/pkgconfig/libudev.pc
%{_libdir}/pkgconfig/libsystemd.pc
%{_libdir}/pkgconfig/libsystemd-daemon.pc
%{_libdir}/pkgconfig/libsystemd-login.pc
%{_libdir}/pkgconfig/libsystemd-journal.pc
%{_libdir}/pkgconfig/libsystemd-id128.pc
%{_mandir}/man3/*
%dir %{_datadir}/gtk-doc/html/libudev
%{_datadir}/gtk-doc/html/libudev/*

%files sysv
%{_bindir}/systemd-sysv-convert

%files python
%{python_sitearch}/systemd

%files -n libgudev1
%{_libdir}/libgudev-1.0.so.*
%{_libdir}/girepository-1.0/GUdev-1.0.typelib

%files -n libgudev1-devel
%{_libdir}/libgudev-1.0.so
%dir %{_includedir}/gudev-1.0
%dir %{_includedir}/gudev-1.0/gudev
%{_includedir}/gudev-1.0/gudev/*.h
%{_datadir}/gir-1.0/GUdev-1.0.gir
%dir %{_datadir}/gtk-doc/html/gudev
%{_datadir}/gtk-doc/html/gudev/*
%{_libdir}/pkgconfig/gudev-1.0*

%files journal-gateway
%config(noreplace) %{_sysconfdir}/systemd/journal-remote.conf
%config(noreplace) %{_sysconfdir}/systemd/journal-upload.conf
%{_prefix}/lib/systemd/system/systemd-journal-gatewayd.*
%{_prefix}/lib/systemd/system/systemd-journal-remote.*
%{_prefix}/lib/systemd/system/systemd-journal-upload.*
%{_prefix}/lib/systemd/systemd-journal-gatewayd
%{_prefix}/lib/systemd/systemd-journal-upload
%{_prefix}/lib/systemd/systemd-journal-remote
%{_prefix}/lib/tmpfiles.d/systemd-remote.conf
#%{_prefix}/lib/sysusers.d/systemd-remote.conf
%{_mandir}/man8/systemd-journal-gatewayd.*
%{_mandir}/man8/systemd-journal-remote.*
%{_datadir}/systemd/gatewayd

%files networkd
%dir %{_prefix}/lib/systemd/network
%{_bindir}/networkctl
#%{_prefix}/lib/systemd/network/99-default.link
#%{_prefix}/lib/systemd/network/80-container-host0.network
#%{_prefix}/lib/systemd/network/80-container-ve.network
%{_prefix}/lib/systemd/system/systemd-networkd.service
%{_prefix}/lib/systemd/system/systemd-networkd-wait-online.service
%{_prefix}/lib/systemd/systemd-networkd
%{_prefix}/lib/systemd/systemd-networkd-wait-online
%{_mandir}/man8/systemd-journal-gatewayd.*
%{_mandir}/man8/systemd-journal-remote.*
%{_mandir}/man8/systemd-networkd.*
%{_mandir}/man5/systemd.network.*
%{_mandir}/man5/systemd.netdev.*
%{_mandir}/man5/systemd.link.*
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.network1.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.network1.service
#%{_datadir}/polkit-1/actions/org.freedesktop.network1.policy
%{_prefix}/lib/udev/rules.d/80-net-setup-link.rules

%files resolved
%{_prefix}/lib/systemd/systemd-resolved
%{_prefix}/lib/systemd/systemd-resolve-host
%{_sysconfdir}/systemd/resolved.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.resolve1.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.resolve1.service
%{_libdir}/libnss_resolve.so.2
%{_prefix}/lib/systemd/system/systemd-resolved.service
%{_prefix}/lib/systemd/system/dbus-org.freedesktop.resolve1.service
%{_mandir}/man5/resolved.conf.*
%{_mandir}/man8/systemd-resolved.*

%changelog
* Mon Oct 12 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-19
- udev: make naming for virtio devices opt-in (#1269216)
- tmpfiles.d: don't clean SAP sockets either (#1186044)

* Tue Oct 06 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-18
- tmpfiles.d: don't clean SAP lockfiles and logs (#1186044)

* Mon Sep 28 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-17
- sd-event: fix prepare priority queue comparison function (#1266479)
- units: run ldconfig also when cache is unpopulated (#1265539)
- selinux: fix regression of systemctl subcommands when absolute unit file paths are specified (#1185120)

* Wed Sep 23 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-16
- login: fix gcc warning, include missing header file (#1264073)
- shutdown: make sure /run/nologin has correct label (#1264073)

* Tue Sep 22 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-15
- login: fix label on /run/nologin (#1264073)
- udev-rules: prandom character device node permissions (#1264112)

* Tue Sep 15 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-14
- Revert "sysctl.d: default to fq_codel, fight bufferbloat" (#1263158)
- loginctl: print nontrivial properties in logictl show-* (#1260465)

* Wed Sep 02 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-13
- udev: net_id - support predictable ifnames on virtio buses (#1259015)

* Tue Sep 01 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-12
- selinux: fix check for transient units (#1255129)
- socket: fix setsockopt call. SOL_SOCKET changed to SOL_TCP. (#1135599)
- selinux: fix missing SELinux unit access check (#1185120)
- selinux: always use *_raw API from libselinux (#1256888)

* Wed Aug 12 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-11
- journald-server: don't read audit events (#1252409)
- everything: remove traces of --user (#1071363)

* Fri Aug 07 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-10
- Revert "journald: move /dev/log socket to /run" (#1249968)

* Fri Jul 31 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-9
- units: add [Install] section to tmp.mount
- bus-util: add articles to explanation messages (#1016680)
- bus-util: print correct warnings for units that fail but for which we have a NULL result only (#1016680)

* Thu Jul 16 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-8
- sysv-generator test: Fix assertion (#1222517)
- man: avoid line break in url (#1222517)
- Add VARIANT as a standard value for /etc/os-release (#1222517)
- Fix permissions on /run/systemd/nspawn/locks (#1222517)
- generators: rename add_{root,usr}_mount to add_{sysroot,sysroot_usr}_mount (#1222517)
- Generate systemd-fsck-root.service in the initramfs (#1222517)
- units: fix typo in systemd-resolved.service (#1222517)
- core: don't consider umask for SocketMode= (#1222517)
- timedate: fix memory leak in timedated (#1222517)
- coredump: make sure we vacuum by default (#1222517)
- tmpfiles: don't fail if we cannot create a subvolume because a file system is read-only but a dir already exists anyway (#1222517)
- resolved: fix crash when shutting down (#1222517)
- resolved: allow DnsAnswer objects with no space for RRs (#1222517)
- id128: add new sd_id128_is_null() call (#1222517)
- journalctl: Improve boot ID lookup (#1222517)
- test-hashmap: fix an assert (#1222517)
- units: make sure systemd-nspawn@.slice instances are actually located in machine.slice (#1222517)
- Revert "journald-audit: exit gracefully in the case we can't join audit multicast group" (#1222517)
- journald: handle more gracefully when bind() fails on audit sockets (#1222517)
- udev: link-config - fix corruption (#1222517)
- udev/net_id: Only read the first 64 bytes of PCI config space (#1222517)
- shared: generator - correct path to systemd-fsck (#1222517)
- logind: Save the user’s state when a session enters SESSION_ACTIVE (#1222517)
- small fix ru translation (#1222517)
- kmod-setup: don't warn when ipv6 can't be loaded (#1222517)
- Partially revert "ma-setup: simplify" (#1222517)
- ima-setup: write policy one line at a time (#1222517)
- ata_id: unbotch format specifier (#1222517)
- install: explicitly return 0 on success (#1222517)
- systemd.service.xml: document that systemd removes the PIDFile (#1222517)
- core: handle --log-target=null when calling systemd-shutdown (#1222517)
- man: ProtectHome= protects /root as well (#1222517)
- timedatectl: trim non-local RTC warning to 80 chars wide (#1222517)
- escape: fix exit code (#1222517)
- man: information about available properties (#1222517)
- journal: in persistent mode create /var/log/journal, with all parents. (#1222517)
- sysv-generator: fix wrong "Overwriting existing symlink" warnings (#1222517)
- mount: don't claim a device is gone from /proc/self/mountinfo before it is gone from *all* lines (#1222517)
- mount: properly check for mounts currently in /proc/self/mountinfo (#1222517)

* Tue Jul 14 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-7
- udev: fix crash in path_id builtin (#957112)

* Fri Jul 10 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-6
- sd-bus: don't inherit connection creds into message creds when we have a direct connection (#1230190)

* Tue Jun 30 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-5
- Revert "core: one step back again, for nspawn we actually can't wait for cgroups running empty since systemd will get exactly zero notifications about it" (#1199644)
- bus-creds: always set SD_BUS_CREDS_PID when we set pid in the mask (#1230190)
- sd-bus: do not use per-datagram auxiliary information (#1230190)
- sd-bus: store selinux context at connection time (#1230190)
- journald: simplify context handling (#1230190)
- bash-completion: add verb set-property (#1235635)

* Fri Jun 19 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-4
- core: Fix assertion with empty Exec*= paths (#1222517)
- rules: load sg module (#1186462)
- util: add shell_maybe_quote() call for preparing a string for shell cmdline inclusion (#1016680)
- bus-util: be more verbose if dbus job fails (#1016680)
- notify: fix badly backported help message (#1199644)
- cryptsetup: craft a unique ID with the source device (#1226333)
- systemctl: introduce --now for enable, disable and mask (#1233081)
- udev: also create old sas paths (#957112)
- journald: do not strip leading whitespace from messages (#1227396)

* Mon May 18 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-3
- console-getty.service: don't start when /dev/console is missing (#1222517)
- resolved: Do not add .busname dependencies, when compiling without kdbus. (#1222517)
- man: add journal-remote.conf(5) (#1222517)
- mount: don't run quotaon only for network filesystems (#1222517)
- mount: fix up wording in the comment (#1222517)
- udev: net_id - fix copy-paste error (#1222517)
- man: don't mention "journalctl /dev/sda" (#1222517)
- units: move After=systemd-hwdb-update.service dependency from udev to udev-trigger (#1222517)
- units: explicitly order systemd-user-sessions.service after nss-user-lookup.target (#1222517)
- zsh-completion: update loginctl (#1222517)
- zsh-completion: add missing -M completion for journalctl (#1222517)
- zsh-completion: update hostnamectl (#1222517)
- shell-completion: systemctl switch-root verb (#1222517)
- core/automount: beef up error message (#1222517)
- man: remove 'fs' from 'rootfsflags' (#1222517)
- shared: fix memleak (#1222517)
- udevd: fix synchronization with settle when handling inotify events (#1222517)
- python-systemd: fix is_socket_inet to cope with ports (#1222517)
- man: fix examples indentation in tmpfiles.d(5) (#1222517)
- systemctl: avoid bumping NOFILE rlimit unless needed (#1222517)
- exit-status: Fix "NOTINSSTALLED" typo (#1222517)
- tmpfiles: there's no systemd-forbid-user-logins.service service (#1222517)
- kmod-setup: load ip_tables kmod at boot (#1222517)
- util: Fix assertion in split() on missing ' (#1222517)
- units: set KillMode=mixed for our daemons that fork worker processes (#1222517)
- unit: don't add automatic dependencies on device units if they aren't supported (#1222517)
- update-done: ignore nanosecond file timestamp components, they are not reliable (#1222517)
- sd-daemon: simplify sd_pid_notify_with_fds (#1222517)
- fstab-generator: add x-systemd.requires and x-systemd.requires-mounts-for (#1164334)

* Thu May 14 2015 Lukas Nykryn <lnykryn@redhat.com> - 219-2
- udev: restore udevadm settle timeout (#1210981)
- udev: settle should return immediately when timeout is 0 (#1210981)
- udev: Fix ping timeout when settle timeout is 0 (#1210981)
- detect-virt: use /proc/device-tree (#1207773)
- ARM: detect-virt: detect Xen (#1207773)
- ARM: detect-virt: detect QEMU/KVM (#1207773)
- Persistent by_path links for ata devices (#1045498)
- man: document forwarding to syslog better (#1177336)
- man: fix typos in previous comimt (#1177336)
- LSB: always add network-online.target to services with priority over 10 (#1189253)
- rules: enable memory hotplug (#1105020)
- rules: reload sysctl settings when the bridge module is loaded (#1182105)

* Tue Apr 14 2015 Lukáš Nykrýn <lnykryn@redhat.com> - 219-1
- workaround build issues on ppc and s390
- some more patches

* Tue Mar 17 2015 Lukáš Nykrýn <lnykryn@redhat.com> - 219-0.4
- steal more patches from fedora

* Fri Mar 13 2015 Lukáš Nykrýn <lnykryn@redhat.com> - 219-0.3
- steal patches from fedora

* Fri Mar 06 2015 Lukáš Nykrýn <lnykryn@redhat.com> - 219-0.1
- rebase to 219

* Mon Dec 15 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 218-0.3
- rebase to 218
- remove networkd tmpfiles snipets due to packaging issues
- add resolved subpackage
- backport some nspawn features from upstream

* Thu Nov 20 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 217-0.3
- split systemd and networkd tmpfiles snippets

* Thu Nov 20 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 217-0.2
- spec fixes
- core: introduce new Delegate=yes/no property controlling creation of cgroup subhierarchies

* Mon Nov 17 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 217-0.1
- rebase to 217

* Mon Nov 10 2014 Lukas Nykryn <lnykryn@redhat.com> - 208-19
- cgroups-agent: really down-grade log level (#1044386)

* Mon Nov 10 2014 Lukas Nykryn <lnykryn@redhat.com> - 208-18
- login: rerun vconsole-setup when switching from vgacon to fbcon (#1002450)

* Fri Nov 07 2014 Lukas Nykryn <lnykryn@redhat.com> - 208-17
- udev: net_id dev_port is base 10 (#1155996)
- udev: Fix parsing of udev.event-timeout kernel parameter (#1154778)

* Thu Oct 30 2014 Lukas Nykryn <lnykryn@redhat.com> - 208-16
- logind: use correct "who" enum values with KillUnit. (#1155502)
- logind: always kill session when termination is requested (#1155502)
- udev: net_id - correctly name netdevs based on dev_port when set (#1155996)

* Tue Oct 21 2014 Lukas Nykryn <lnykryn@redhat.com> - 208-15
- core: do not segfault if /proc/swaps cannot be opened (#1151239)
- man: we don't have 'Wanted' dependency (#1152487)
- environment: append unit_id to error messages regarding EnvironmentFile (#1147691)
- udevd: add --event-timeout commandline option (#1154778)

* Wed Oct 08 2014 Lukas Nykryn <lnykryn@redhat.com> - 208-14
- core: don't allow enabling if unit is masked (#1149299)

* Tue Oct 07 2014 Lukas Nykryn <lnykryn@redhat.com> - 208-13
- tmpfiles: minor modernizations (#1147524)
- install: when looking for a unit file for enabling, search for templates only after traversing all search directories (#1147524)
- install: remove unused variable (#1147524)
- bootctl: typo fix in help message (#1147524)
- logind: ignore failing close() on session-devices (#1147524)
- sysfs-show.c: return negative error (#1147524)
- core: only send SIGHUP when doing first kill, not when doing final sigkill (#1147524)
- cgroup: make sure to properly send SIGCONT to all processes of a cgroup if that's requested (#1147524)
- core: don't send duplicate SIGCONT when killing units (#1147524)
- efi: fix Undefined reference efi_loader_get_boot_usec when EFI support is disabled (#1147524)
- macro: better make IN_SET() macro use const arrays (#1147524)
- macro: make sure we can use IN_SET() also with complex function calls as first argument (#1147524)
- core: fix property changes in transient units (#1147524)
- load-modules: properly return a failing error code if some module fails to load (#1147524)
- core/unit: fix unit_add_target_dependencies() for units with no dependencies (#1147524)
- man: there is no ExecStopPre= for service units (#1147524)
- man: document that per-interface sysctl variables are applied as network interfaces show up (#1147524)
- journal: downgrade vaccuum message to debug level (#1147524)
- logs-show: fix corrupt output with empty messages (#1147524)
- journalctl: refuse extra arguments with --verify and similar (#1147524)
- journal: assume that next entry is after previous entry (#1147524)
- journal: forget file after encountering an error (#1147524)
- man: update link to LSB (#1147524)
- man: systemd-bootchart - fix spacing in command (#1147524)
- man: add missing comma (#1147524)
- units: Do not unescape instance name in systemd-backlight@.service (#1147524)
- manager: flush memory stream before using the buffer (#1147524)
- man: multiple sleep modes are to be separated by whitespace, not commas (#1147524)
- man: fix description of systemctl --after/--before (#1147524)
- udev: properly detect reference to unexisting part of PROGRAM's result (#1147524)
- gpt-auto-generator: don't return OOM on parentless devices (#1147524)
- man: improve wording of systemctl's --after/--before (#1147524)
- cgroup: it's not OK to invoke alloca() in loops (#1147524)
- core: don't try to relabel mounts before we loaded the policy (#1147524)
- systemctl: --kill-mode is long long gone, don't mention it in the man page (#1147524)
- ask-password: when the user types a overly long password, beep and refuse (#1147524)
- logind: don't print error if devices vanish during ACL-init (#1147524)
- tty-ask-password-agent: return negative errno (#1147524)
- journal: cleanup up error handling in update_catalog() (#1147524)
- bash completion: fix __get_startable_units (#1147524)
- core: check the right variable for failed open() (#1147524)
- man: sd_journal_send does nothing when journald is not available (#1147524)
- man: clarify that the ExecReload= command should be synchronous (#1147524)
- conf-parser: never consider it an error if we cannot load a drop-in file because it is missing (#1147524)
- socket: properly handle if our service vanished during runtime (#1147524)
- Do not unescape unit names in [Install] section (#1147524)
- util: ignore_file should not allow files ending with '~' (#1147524)
- core: fix invalid free() in killall() (#1147524)
- install: fix invalid free() in unit_file_mask() (#1147524)
- unit-name: fix detection of unit templates/instances (#1147524)
- journald: make MaxFileSec really default to 1month (#1147524)
- bootchart: it's not OK to return -1 from a main program (#1147524)
- journald: Fix off-by-one error in "Missed X kernel messages" warning (#1147524)
- man: drop references to removed and obsolete 'systemctl load' command (#1147524)
- units: fix BindsTo= logic when applied relative to services with Type=oneshot (#1147524)

* Mon Sep 29 2014 Lukas Nykryn <lnykryn@redhat.com> - 208-12
- units/serial-getty@.service: add [Install] section (#1083936)
- units: order network-online.target after network.target (#1072431)
- util: consider both fuse.glusterfs and glusterfs network file systems (#1080229)
- core: make StopWhenUnneeded work in conjunction with units that fail during their start job (#986949)
- cgroups-agent: down-grade log level (#1044386)
- random-seed: raise POOL_SIZE_MIN constant to 1024 (#1066517)
- delta: do not use unicode chars in C locale (#1088419)
- core: print debug instead of error message (#1105608)
- journald: always add syslog facility for messages coming from kmsg (#1113215)
- fsck,fstab-generator: be lenient about missing fsck.<type> (#1098310)
- rules/60-persistent-storage: add nvme pcie ssd scsi_id ENV (#1042990)
- cgls: fix running with -M option (#1085455)
- getty: Start getty on 3270 terminals available on Linux on System z (#1075729)
- core: Added support for ERRNO NOTIFY_SOCKET  message parsing (#1106457)
- socket: add SocketUser= and SocketGroup= for chown()ing sockets in the file system (#1111761)
- tmpfiles: add --root option to operate on an alternate fs tree (#1111199)
- units: make ExecStopPost action part of ExecStart (#1036276)
- machine-id: only look into KVM uuid when we are not running in a container (#1123452)
- util: reset signals when we fork off agents (#1134818)
- udev: do not skip the execution of RUN when renaming a network device fails (#1102135)
- man: mention System Administrator's Guide in systemctl manpage (#978948)
- vconsole: also copy character maps (not just fonts) from vt1 to vt2, vt3, ... (#1002450)
- localed: consider an unset model as a wildcard (#903776)
- systemd-detect-virt: detect s390 virtualization (#1139149)
- socket: introduce SELinuxContextFromNet option (#1113790)
- sysctl: make --prefix allow all kinds of sysctl paths (#1138591)
- man: mention localectl in locale.conf (#1049286)
- rules: automatically online hot-added CPUs (#968811)
- rules: add rule for naming Dell iDRAC USB Virtual NIC as 'idrac' (#1054477)
- bash-completion: add verb set-property (#1064487)
- man: update journald rate limit defaults (#1145352)
- core: don't try to connect to d-bus after switchroot (#1083300)
- localed: check for partially matching converted keymaps (#1109145)
- fileio: make parse_env_file() return number of parsed items (#1069420)

* Wed Apr 02 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 208-11
- logind-session: save stopping flag (#1082692)
- unit: add waiting jobs to run queue in unit_coldplug (#1083159)

* Fri Mar 28 2014 Harald Hoyer <harald@redhat.com> 208-10
- require redhat-release >= 7.0
Resolves: rhbz#1070114

* Fri Mar 14 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 208-9
- fixes crashes in logind and systemd (#1073994)
- run fsck before mouting root in initramfs (#1056661)

* Thu Mar 06 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 208-8
- rules: mark loop device as SYSTEMD_READY=0 if no file is attached (#1067422)
- utmp: make sure we don't write the utmp reboot record twice on each boot (#1053600)
- rework session shutdown logic (#1047614)
- introduce new stop protocol for unit scopes (#1064976)

* Wed Mar 05 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 208-7
- setup tty permissions and group for /dev/sclp_line0 (#1070310)
- cdrom_id: use the old MMC fallback (#1038015)
- mount: don't send out PropertiesChanged message if actually nothing got changed (#1069718)

* Wed Feb 26 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 208-6
- fix boot if SELINUX=permissive in configuration file and trying to boot in enforcing=1 (#907841)

* Tue Feb 25 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 208-5
- reintroduce 60-alias-kmsg.rules (#1032711)

* Mon Feb 17 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 208-4
- fstab-generator: revert wrongly applied patch

* Fri Feb 14 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 208-3
- dbus-manager: fix selinux check for enable/disable

* Wed Feb 12 2014 Michal Sekletar <msekleta@redhat.com> - 208-2
- require redhat-release package
- call systemd-tmpfiles after package installation (#1059345)
- move preset policy out of systemd package (#903690)

* Tue Feb 11 2014 Michal Sekletar <msekleta@redhat.com> - 208-1
- rebase to systemd-208 (#1063332)
- do not create symlink /etc/systemd/system/syslog.service (#1055421)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 207-14
- Mass rebuild 2014-01-24

* Thu Jan 16 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 207-13
- fix SELinux check for transient units (#1008864)

* Wed Jan 15 2014 Lukáš Nykrýn <lnykryn@redhat.com> - 207-12
- shell-completion: remove load and dump from systemctl (#1048066)
- delta: ensure that d_type will be set on every fs (#1050795)
- tmpfiles: don't allow label_fix to print ENOENT when we want to ignore it (#1044871)
- udev/net_id: Introduce predictable network names for Linux on System z (#870859)
- coredumpctl: in case of error free pattern after print (#1052786)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 207-11
- Mass rebuild 2013-12-27

* Thu Dec 19 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-10
- cgroup_show: don't call show_pid_array on empty arrays

* Wed Dec 18 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-9
- treat reload failure as failure (#1036848)
- improve journal performance (#1029604)
- backport bugfixes (#1043525)
- fix handling of trailing whitespace in split_quoted (#984832)
- localed: match converted keymaps before legacy (#903776)
- improve the description of parameter X in tmpfiles.d page (#1029604)
- obsolete ConsoleKit (#1039761)
- make rc.local more backward comaptible (#1039465)

* Tue Nov 19 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-8
- tmpfiles: introduce m (#1030961)

* Tue Nov 12 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-7
- introduce DefaultStartLimit (#821723)

* Mon Nov 11 2013 Harald Hoyer <harald@redhat.com> 207-6
- changed systemd-journal-gateway login shell to /sbin/nologin
- backported a lot of bugfixes
- udev: path_id - fix by-path link generation for scm devices
Resolves: rhbz#888707

* Tue Nov 05 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-5
- create /etc/rc.d/rc.local (#968401)
- cgroup: always enable memory.use_hierarchy= for all cgroups (#1011575)
- remove user@.service (#1019738)
- drop some out-of-date references to cgroup settings (#1000004)
- explain NAME in systemctl man page (#978954)

* Tue Oct 15 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-4
- core: whenever a new PID is passed to us, make sure we watch it

* Tue Oct 01 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-3
- presets: add tuned.service

* Thu Sep 19 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-2
- Advertise hibernation only if there's enough free swap
- swap: create .wants symlink to 'auto' swap devices
- Verify validity of session name when received from outside
- polkit: Avoid race condition in scraping /proc
Resolves: rhbz#1005142

* Fri Sep 13 2013 Harald Hoyer <harald@redhat.com> 207-1
- version 207

* Fri Sep 06 2013 Harald Hoyer <harald@redhat.com> 206-8
- support "debug" kernel command line parameter
- journald: fix fd leak in journal_file_empty
- journald: fix vacuuming of archived journals
- libudev: enumerate - do not try to match against an empty subsystem
- cgtop: fixup the online help
- libudev: fix memleak when enumerating childs

* Wed Aug 28 2013 Harald Hoyer <harald@redhat.com> 206-7
- fixed cgroup hashmap corruption
Resolves: rhbz#997742 rhbz#995197

* Fri Aug 23 2013 Harald Hoyer <harald@redhat.com> 206-6
- cgroup.c: check return value of unit_realize_cgroup_now()
Resolves: rhbz#997742 rhbz#995197

* Thu Aug 22 2013 Harald Hoyer <harald@redhat.com> 206-5
- obsolete upstart
Resolves: rhbz#978014
- obsolete hal
Resolves: rhbz#975589
- service: always unwatch PIDs before forgetting old ones
Resolves: rhbz#995197
- units: disable kmod-static-nodes.service in containers
- use CAP_MKNOD ConditionCapability
- fstab-generator: read rd.fstab=on/off switch correctly
- backlight: add minimal tool to save/restore screen brightness
- backlight: instead of syspath use sysname for identifying
- sysctl: allow overwriting of values specified in "later"
- systemd-python: fix initialization of _Reader objects
- udevd: simplify sigterm check
- libudev: fix hwdb validation to look for the *new* file
- units: make fsck units remain after exit
- udev: replace CAP_MKNOD by writable /sys condition
- libudev-enumerate.c:udev_enumerate_get_list_entry() fixed
- journal: fix parsing of facility in syslog messages

* Fri Aug 09 2013 Harald Hoyer <harald@redhat.com> 206-4
- journal: handle multiline syslog messages
- man: Fix copy&paste error
- core: synchronously block when logging
- journal: immediately sync to disk as soon as we receieve an EMERG/ALERT/CRIT message
- initctl: use irreversible jobs when switching runlevels
- udev: log error if chmod/chown of static dev nodes fails
- udev: static_node - don't touch permissions uneccessarily
- tmpfiles: support passing --prefix multiple times
- tmpfiles: introduce --exclude-prefix
- tmpfiles-setup: exclude /dev prefixes files
- logind: update state file after generating the session fifo, not before
- journalctl: use _COMM= match for scripts
- man: systemd.unit: fix volatile path
- man: link up scope+slice units from systemd.unit(5)
- man: there is no session mode, only user mode
- journal: fix hashmap leak in mmap-cache
- systemd-delta: Only print colors when on a tty
- systemd: fix segv in snapshot creation
- udev: hwdb - try reading modalias for usb before falling back to the composed one
- udevd: respect the log-level set in /etc/udev/udev.conf
- fstab-generator: respect noauto/nofail when adding sysroot mount

* Fri Aug 02 2013 Lukáš Nykrýn <lnykryn@redhat.com> - 206-3
- add dependency on kmod >= 14
- remove /var/log/journal to make journal non-persistant (#989750)
- add hypervkvpd.service to presets (#924321)

* Thu Aug 01 2013 Lukáš Nykrýn <lnykryn@redhat.com> - 206-2
- 80-net-name-slot.rules: only rename network interfaces on ACTION==add

* Tue Jul 23 2013 Kay Sievers <kay@redhat.com> - 206-1
- New upstream release
Resolves (#984152)

* Wed Jul  3 2013 Lennart Poettering <lpoetter@redhat.com> - 205-1
- New upstream release

* Wed Jun 26 2013 Michal Schmidt <mschmidt@redhat.com> 204-10
- Split systemd-journal-gateway subpackage (#908081).

* Mon Jun 24 2013 Michal Schmidt <mschmidt@redhat.com> 204-9
- Rename nm_dispatcher to NetworkManager-dispatcher in default preset (#977433)

* Fri Jun 14 2013 Harald Hoyer <harald@redhat.com> 204-8
- fix, which helps to sucessfully browse journals with
duplicated seqnums

* Fri Jun 14 2013 Harald Hoyer <harald@redhat.com> 204-7
- fix duplicate message ID bug
Resolves: rhbz#974132

* Thu Jun 06 2013 Harald Hoyer <harald@redhat.com> 204-6
- introduce 99-default-disable.preset

* Thu Jun  6 2013 Lennart Poettering <lpoetter@redhat.com> - 204-5
- Rename 90-display-manager.preset to 85-display-manager.preset so that it actually takes precedence over 90-default.preset's "disable *" line (#903690)

* Tue May 28 2013 Harald Hoyer <harald@redhat.com> 204-4
- Fix kernel-install (#965897)

* Wed May 22 2013 Kay Sievers <kay@redhat.com> - 204-3
- Fix kernel-install (#965897)

* Thu May  9 2013 Lennart Poettering <lpoetter@redhat.com> - 204-2
- New upstream release
- disable isdn by default (#959793)

* Tue May 07 2013 Harald Hoyer <harald@redhat.com> 203-2
- forward port kernel-install-grubby.patch

* Tue May  7 2013 Lennart Poettering <lpoetter@redhat.com> - 203-1
- New upstream release

* Wed Apr 24 2013 Harald Hoyer <harald@redhat.com> 202-3
- fix ENOENT for getaddrinfo
- Resolves: rhbz#954012 rhbz#956035
- crypt-setup-generator: correctly check return of strdup
- logind-dbus: initialize result variable
- prevent library underlinking

* Fri Apr 19 2013 Harald Hoyer <harald@redhat.com> 202-2
- nspawn create empty /etc/resolv.conf if necessary
- python wrapper: add sd_journal_add_conjunction()
- fix s390 booting
- Resolves: rhbz#953217

* Thu Apr 18 2013 Lennart Poettering <lpoetter@redhat.com> - 202-1
- New upstream release

* Tue Apr 09 2013 Michal Schmidt <mschmidt@redhat.com> - 201-2
- Automatically discover whether to run autoreconf and add autotools and git
BuildRequires based on the presence of patches to be applied.
- Use find -delete.

* Mon Apr  8 2013 Lennart Poettering <lpoetter@redhat.com> - 201-1
- New upstream release

* Mon Apr  8 2013 Lennart Poettering <lpoetter@redhat.com> - 200-4
- Update preset file

* Fri Mar 29 2013 Lennart Poettering <lpoetter@redhat.com> - 200-3
- Remove NetworkManager-wait-online.service from presets file again, it should default to off

* Fri Mar 29 2013 Lennart Poettering <lpoetter@redhat.com> - 200-2
- New upstream release

* Tue Mar 26 2013 Lennart Poettering <lpoetter@redhat.com> - 199-2
- Add NetworkManager-wait-online.service to the presets file

* Tue Mar 26 2013 Lennart Poettering <lpoetter@redhat.com> - 199-1
- New upstream release

* Mon Mar 18 2013 Michal Schmidt <mschmidt@redhat.com> 198-7
- Drop /usr/s?bin/ prefixes.

* Fri Mar 15 2013 Harald Hoyer <harald@redhat.com> 198-6
- run autogen to pickup all changes

* Fri Mar 15 2013 Harald Hoyer <harald@redhat.com> 198-5
- do not mount anything, when not running as pid 1
- add initrd.target for systemd in the initrd

* Wed Mar 13 2013 Harald Hoyer <harald@redhat.com> 198-4
- fix switch-root and local-fs.target problem
- patch kernel-install to use grubby, if available

* Fri Mar 08 2013 Harald Hoyer <harald@redhat.com> 198-3
- add Conflict with dracut < 026 because of the new switch-root isolate

* Thu Mar  7 2013 Lennart Poettering <lpoetter@redhat.com> - 198-2
- Create required users

* Thu Mar 7 2013 Lennart Poettering <lpoetter@redhat.com> - 198-1
- New release
- Enable journal persistancy by default

* Sun Feb 10 2013 Peter Robinson <pbrobinson@fedoraproject.org> 197-3
- Bump for ARM

* Fri Jan 18 2013 Michal Schmidt <mschmidt@redhat.com> - 197-2
- Added qemu-guest-agent.service to presets (Lennart, #885406).
- Add missing pygobject3-base to systemd-analyze deps (Lennart).
- Do not require hwdata, it is all in the hwdb now (Kay).
- Drop dependency on dbus-python.

* Tue Jan  8 2013 Lennart Poettering <lpoetter@redhat.com> - 197-1
- New upstream release

* Mon Dec 10 2012 Michal Schmidt <mschmidt@redhat.com> - 196-4
- Enable rngd.service by default (#857765).

* Mon Dec 10 2012 Michal Schmidt <mschmidt@redhat.com> - 196-3
- Disable hardening on s390(x) because PIE is broken there and produces
text relocations with __thread (#868839).

* Wed Dec 05 2012 Michal Schmidt <mschmidt@redhat.com> - 196-2
- added spice-vdagentd.service to presets (Lennart, #876237)
- BR cryptsetup-devel instead of the legacy cryptsetup-luks-devel provide name
(requested by Milan Brož).
- verbose make to see the actual build flags

* Wed Nov 21 2012 Lennart Poettering <lpoetter@redhat.com> - 196-1
- New upstream release

* Tue Nov 20 2012 Lennart Poettering <lpoetter@redhat.com> - 195-8
- https://bugzilla.redhat.com/show_bug.cgi?id=873459
- https://bugzilla.redhat.com/show_bug.cgi?id=878093

* Thu Nov 15 2012 Michal Schmidt <mschmidt@redhat.com> - 195-7
- Revert udev killing cgroup patch for F18 Beta.
- https://bugzilla.redhat.com/show_bug.cgi?id=873576

* Fri Nov 09 2012 Michal Schmidt <mschmidt@redhat.com> - 195-6
- Fix cyclical dep between systemd and systemd-libs.
- Avoid broken build of test-journal-syslog.
- https://bugzilla.redhat.com/show_bug.cgi?id=873387
- https://bugzilla.redhat.com/show_bug.cgi?id=872638

* Thu Oct 25 2012 Kay Sievers <kay@redhat.com> - 195-5
- require 'sed', limit HOSTNAME= match

* Wed Oct 24 2012 Michal Schmidt <mschmidt@redhat.com> - 195-4
- add dmraid-activation.service to the default preset
- add yum protected.d fragment
- https://bugzilla.redhat.com/show_bug.cgi?id=869619
- https://bugzilla.redhat.com/show_bug.cgi?id=869717

* Wed Oct 24 2012 Kay Sievers <kay@redhat.com> - 195-3
- Migrate /etc/sysconfig/ i18n, keyboard, network files/variables to
systemd native files

* Tue Oct 23 2012 Lennart Poettering <lpoetter@redhat.com> - 195-2
- Provide syslog because the journal is fine as a syslog implementation

* Tue Oct 23 2012 Lennart Poettering <lpoetter@redhat.com> - 195-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=831665
- https://bugzilla.redhat.com/show_bug.cgi?id=847720
- https://bugzilla.redhat.com/show_bug.cgi?id=858693
- https://bugzilla.redhat.com/show_bug.cgi?id=863481
- https://bugzilla.redhat.com/show_bug.cgi?id=864629
- https://bugzilla.redhat.com/show_bug.cgi?id=864672
- https://bugzilla.redhat.com/show_bug.cgi?id=864674
- https://bugzilla.redhat.com/show_bug.cgi?id=865128
- https://bugzilla.redhat.com/show_bug.cgi?id=866346
- https://bugzilla.redhat.com/show_bug.cgi?id=867407
- https://bugzilla.redhat.com/show_bug.cgi?id=868603

* Wed Oct 10 2012 Michal Schmidt <mschmidt@redhat.com> - 194-2
- Add scriptlets for migration away from systemd-timedated-ntp.target

* Wed Oct  3 2012 Lennart Poettering <lpoetter@redhat.com> - 194-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=859614
- https://bugzilla.redhat.com/show_bug.cgi?id=859655

* Fri Sep 28 2012 Lennart Poettering <lpoetter@redhat.com> - 193-1
- New upstream release

* Tue Sep 25 2012 Lennart Poettering <lpoetter@redhat.com> - 192-1
- New upstream release

* Fri Sep 21 2012 Lennart Poettering <lpoetter@redhat.com> - 191-2
- Fix journal mmap header prototype definition to fix compilation on 32bit

* Fri Sep 21 2012 Lennart Poettering <lpoetter@redhat.com> - 191-1
- New upstream release
- Enable all display managers by default, as discussed with Adam Williamson

* Thu Sep 20 2012 Lennart Poettering <lpoetter@redhat.com> - 190-1
- New upstream release
- Take possession of /etc/localtime, and remove /etc/sysconfig/clock
- https://bugzilla.redhat.com/show_bug.cgi?id=858780
- https://bugzilla.redhat.com/show_bug.cgi?id=858787
- https://bugzilla.redhat.com/show_bug.cgi?id=858771
- https://bugzilla.redhat.com/show_bug.cgi?id=858754
- https://bugzilla.redhat.com/show_bug.cgi?id=858746
- https://bugzilla.redhat.com/show_bug.cgi?id=858266
- https://bugzilla.redhat.com/show_bug.cgi?id=858224
- https://bugzilla.redhat.com/show_bug.cgi?id=857670
- https://bugzilla.redhat.com/show_bug.cgi?id=856975
- https://bugzilla.redhat.com/show_bug.cgi?id=855863
- https://bugzilla.redhat.com/show_bug.cgi?id=851970
- https://bugzilla.redhat.com/show_bug.cgi?id=851275
- https://bugzilla.redhat.com/show_bug.cgi?id=851131
- https://bugzilla.redhat.com/show_bug.cgi?id=847472
- https://bugzilla.redhat.com/show_bug.cgi?id=847207
- https://bugzilla.redhat.com/show_bug.cgi?id=846483
- https://bugzilla.redhat.com/show_bug.cgi?id=846085
- https://bugzilla.redhat.com/show_bug.cgi?id=845973
- https://bugzilla.redhat.com/show_bug.cgi?id=845194
- https://bugzilla.redhat.com/show_bug.cgi?id=845028
- https://bugzilla.redhat.com/show_bug.cgi?id=844630
- https://bugzilla.redhat.com/show_bug.cgi?id=839736
- https://bugzilla.redhat.com/show_bug.cgi?id=835848
- https://bugzilla.redhat.com/show_bug.cgi?id=831740
- https://bugzilla.redhat.com/show_bug.cgi?id=823485
- https://bugzilla.redhat.com/show_bug.cgi?id=821813
- https://bugzilla.redhat.com/show_bug.cgi?id=807886
- https://bugzilla.redhat.com/show_bug.cgi?id=802198
- https://bugzilla.redhat.com/show_bug.cgi?id=767795
- https://bugzilla.redhat.com/show_bug.cgi?id=767561
- https://bugzilla.redhat.com/show_bug.cgi?id=752774
- https://bugzilla.redhat.com/show_bug.cgi?id=732874
- https://bugzilla.redhat.com/show_bug.cgi?id=858735

* Thu Sep 13 2012 Lennart Poettering <lpoetter@redhat.com> - 189-4
- Don't pull in pkg-config as dep
- https://bugzilla.redhat.com/show_bug.cgi?id=852828

* Wed Sep 12 2012 Lennart Poettering <lpoetter@redhat.com> - 189-3
- Update preset policy
- Rename preset policy file from 99-default.preset to 90-default.preset so that people can order their own stuff after the Fedora default policy if they wish

* Thu Aug 23 2012 Lennart Poettering <lpoetter@redhat.com> - 189-2
- Update preset policy
- https://bugzilla.redhat.com/show_bug.cgi?id=850814

* Thu Aug 23 2012 Lennart Poettering <lpoetter@redhat.com> - 189-1
- New upstream release

* Thu Aug 16 2012 Ray Strode <rstrode@redhat.com> 188-4
- more scriptlet fixes
(move dm migration logic to %%posttrans so the service
files it's looking for are available at the time
the logic is run)

* Sat Aug 11 2012 Lennart Poettering <lpoetter@redhat.com> - 188-3
- Remount file systems MS_PRIVATE before switching roots
- https://bugzilla.redhat.com/show_bug.cgi?id=847418

* Wed Aug 08 2012 Rex Dieter <rdieter@fedoraproject.org> - 188-2
- fix scriptlets

* Wed Aug  8 2012 Lennart Poettering <lpoetter@redhat.com> - 188-1
- New upstream release
- Enable gdm and avahi by default via the preset file
- Convert /etc/sysconfig/desktop to display-manager.service symlink
- Enable hardened build

* Mon Jul 30 2012 Kay Sievers <kay@redhat.com> - 187-3
- Obsolete: system-setup-keyboard

* Wed Jul 25 2012 Kalev Lember <kalevlember@gmail.com> - 187-2
- Run ldconfig for the new -libs subpackage

* Thu Jul 19 2012 Lennart Poettering <lpoetter@redhat.com> - 187-1
- New upstream release

* Mon Jul 09 2012 Harald Hoyer <harald@redhat.com> 186-2
- fixed dracut conflict version

* Tue Jul  3 2012 Lennart Poettering <lpoetter@redhat.com> - 186-1
- New upstream release

* Fri Jun 22 2012 Nils Philippsen <nils@redhat.com> - 185-7.gite7aee75
- add obsoletes/conflicts so multilib systemd -> systemd-libs updates work

* Thu Jun 14 2012 Michal Schmidt <mschmidt@redhat.com> - 185-6.gite7aee75
- Update to current git

* Wed Jun 06 2012 Kay Sievers - 185-5.gita2368a3
- disable plymouth in configure, to drop the .wants/ symlinks

* Wed Jun 06 2012 Michal Schmidt <mschmidt@redhat.com> - 185-4.gita2368a3
- Update to current git snapshot
- Add systemd-readahead-analyze
- Drop upstream patch
- Split systemd-libs
- Drop duplicate doc files
- Fixed License headers of subpackages

* Wed Jun 06 2012 Ray Strode <rstrode@redhat.com> - 185-3
- Drop plymouth files
- Conflict with old plymouth

* Tue Jun 05 2012 Kay Sievers - 185-2
- selinux udev labeling fix
- conflict with older dracut versions for new udev file names

* Mon Jun 04 2012 Kay Sievers - 185-1
- New upstream release
- udev selinux labeling fixes
- new man pages
- systemctl help <unit name>

* Thu May 31 2012 Lennart Poettering <lpoetter@redhat.com> - 184-1
- New upstream release

* Thu May 24 2012 Kay Sievers <kay@redhat.com> - 183-1
- New upstream release including udev merge.

* Wed Mar 28 2012 Michal Schmidt <mschmidt@redhat.com> - 44-4
- Add triggers from Bill Nottingham to correct the damage done by
the obsoleted systemd-units's preun scriptlet (#807457).

* Mon Mar 26 2012 Dennis Gilmore <dennis@ausil.us> - 44-3
- apply patch from upstream so we can build systemd on arm and ppc
- and likely the rest of the secondary arches

* Tue Mar 20 2012 Michal Schmidt <mschmidt@redhat.com> - 44-2
- Don't build the gtk parts anymore. They're moving into systemd-ui.
- Remove a dead patch file.

* Fri Mar 16 2012 Lennart Poettering <lpoetter@redhat.com> - 44-1
- New upstream release
- Closes #798760, #784921, #783134, #768523, #781735

* Mon Feb 27 2012 Dennis Gilmore <dennis@ausil.us> - 43-2
- don't conflict with fedora-release systemd never actually provided
- /etc/os-release so there is no actual conflict

* Wed Feb 15 2012 Lennart Poettering <lpoetter@redhat.com> - 43-1
- New upstream release
- Closes #789758, #790260, #790522

* Sat Feb 11 2012 Lennart Poettering <lpoetter@redhat.com> - 42-1
- New upstream release
- Save a bit of entropy during system installation (#789407)
- Don't own /etc/os-release anymore, leave that to fedora-release

* Thu Feb  9 2012 Adam Williamson <awilliam@redhat.com> - 41-2
- rebuild for fixed binutils

* Thu Feb  9 2012 Lennart Poettering <lpoetter@redhat.com> - 41-1
- New upstream release

* Tue Feb  7 2012 Lennart Poettering <lpoetter@redhat.com> - 40-1
- New upstream release

* Thu Jan 26 2012 Kay Sievers <kay@redhat.com> - 39-3
- provide /sbin/shutdown

* Wed Jan 25 2012 Harald Hoyer <harald@redhat.com> 39-2
- increment release

* Wed Jan 25 2012 Kay Sievers <kay@redhat.com> - 39-1.1
- install everything in /usr
https://fedoraproject.org/wiki/Features/UsrMove

* Wed Jan 25 2012 Lennart Poettering <lpoetter@redhat.com> - 39-1
- New upstream release

* Sun Jan 22 2012 Michal Schmidt <mschmidt@redhat.com> - 38-6.git9fa2f41
- Update to a current git snapshot.
- Resolves: #781657

* Sun Jan 22 2012 Michal Schmidt <mschmidt@redhat.com> - 38-5
- Build against libgee06. Reenable gtk tools.
- Delete unused patches.
- Add easy building of git snapshots.
- Remove legacy spec file elements.
- Don't mention implicit BuildRequires.
- Configure with --disable-static.
- Merge -units into the main package.
- Move section 3 manpages to -devel.
- Fix unowned directory.
- Run ldconfig in scriptlets.
- Split systemd-analyze to a subpackage.

* Sat Jan 21 2012 Dan Horák <dan[at]danny.cz> - 38-4
- fix build on big-endians

* Wed Jan 11 2012 Lennart Poettering <lpoetter@redhat.com> - 38-3
- Disable building of gtk tools for now

* Wed Jan 11 2012 Lennart Poettering <lpoetter@redhat.com> - 38-2
- Fix a few (build) dependencies

* Wed Jan 11 2012 Lennart Poettering <lpoetter@redhat.com> - 38-1
- New upstream release

* Tue Nov 15 2011 Michal Schmidt <mschmidt@redhat.com> - 37-4
- Run authconfig if /etc/pam.d/system-auth is not a symlink.
- Resolves: #753160

* Wed Nov 02 2011 Michal Schmidt <mschmidt@redhat.com> - 37-3
- Fix remote-fs-pre.target and its ordering.
- Resolves: #749940

* Wed Oct 19 2011 Michal Schmidt <mschmidt@redhat.com> - 37-2
- A couple of fixes from upstream:
- Fix a regression in bash-completion reported in Bodhi.
- Fix a crash in isolating.
- Resolves: #717325

* Tue Oct 11 2011 Lennart Poettering <lpoetter@redhat.com> - 37-1
- New upstream release
- Resolves: #744726, #718464, #713567, #713707, #736756

* Thu Sep 29 2011 Michal Schmidt <mschmidt@redhat.com> - 36-5
- Undo the workaround. Kay says it does not belong in systemd.
- Unresolves: #741655

* Thu Sep 29 2011 Michal Schmidt <mschmidt@redhat.com> - 36-4
- Workaround for the crypto-on-lvm-on-crypto disk layout
- Resolves: #741655

* Sun Sep 25 2011 Michal Schmidt <mschmidt@redhat.com> - 36-3
- Revert an upstream patch that caused ordering cycles
- Resolves: #741078

* Fri Sep 23 2011 Lennart Poettering <lpoetter@redhat.com> - 36-2
- Add /etc/timezone to ghosted files

* Fri Sep 23 2011 Lennart Poettering <lpoetter@redhat.com> - 36-1
- New upstream release
- Resolves: #735013, #736360, #737047, #737509, #710487, #713384

* Thu Sep  1 2011 Lennart Poettering <lpoetter@redhat.com> - 35-1
- New upstream release
- Update post scripts
- Resolves: #726683, #713384, #698198, #722803, #727315, #729997, #733706, #734611

* Thu Aug 25 2011 Lennart Poettering <lpoetter@redhat.com> - 34-1
- New upstream release

* Fri Aug 19 2011 Harald Hoyer <harald@redhat.com> 33-2
- fix ABRT on service file reloading
- Resolves: rhbz#732020

* Wed Aug  3 2011 Lennart Poettering <lpoetter@redhat.com> - 33-1
- New upstream release

* Fri Jul 29 2011 Lennart Poettering <lpoetter@redhat.com> - 32-1
- New upstream release

* Wed Jul 27 2011 Lennart Poettering <lpoetter@redhat.com> - 31-2
- Fix access mode of modprobe file, restart logind after upgrade

* Wed Jul 27 2011 Lennart Poettering <lpoetter@redhat.com> - 31-1
- New upstream release

* Wed Jul 13 2011 Lennart Poettering <lpoetter@redhat.com> - 30-1
- New upstream release

* Thu Jun 16 2011 Lennart Poettering <lpoetter@redhat.com> - 29-1
- New upstream release

* Mon Jun 13 2011 Michal Schmidt <mschmidt@redhat.com> - 28-4
- Apply patches from current upstream.
- Fixes memory size detection on 32-bit with >4GB RAM (BZ712341)

* Wed Jun 08 2011 Michal Schmidt <mschmidt@redhat.com> - 28-3
- Apply patches from current upstream
- https://bugzilla.redhat.com/show_bug.cgi?id=709909
- https://bugzilla.redhat.com/show_bug.cgi?id=710839
- https://bugzilla.redhat.com/show_bug.cgi?id=711015

* Sat May 28 2011 Lennart Poettering <lpoetter@redhat.com> - 28-2
- Pull in nss-myhostname

* Thu May 26 2011 Lennart Poettering <lpoetter@redhat.com> - 28-1
- New upstream release

* Wed May 25 2011 Lennart Poettering <lpoetter@redhat.com> - 26-2
- Bugfix release
- https://bugzilla.redhat.com/show_bug.cgi?id=707507
- https://bugzilla.redhat.com/show_bug.cgi?id=707483
- https://bugzilla.redhat.com/show_bug.cgi?id=705427
- https://bugzilla.redhat.com/show_bug.cgi?id=707577

* Sat Apr 30 2011 Lennart Poettering <lpoetter@redhat.com> - 26-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=699394
- https://bugzilla.redhat.com/show_bug.cgi?id=698198
- https://bugzilla.redhat.com/show_bug.cgi?id=698674
- https://bugzilla.redhat.com/show_bug.cgi?id=699114
- https://bugzilla.redhat.com/show_bug.cgi?id=699128

* Thu Apr 21 2011 Lennart Poettering <lpoetter@redhat.com> - 25-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=694788
- https://bugzilla.redhat.com/show_bug.cgi?id=694321
- https://bugzilla.redhat.com/show_bug.cgi?id=690253
- https://bugzilla.redhat.com/show_bug.cgi?id=688661
- https://bugzilla.redhat.com/show_bug.cgi?id=682662
- https://bugzilla.redhat.com/show_bug.cgi?id=678555
- https://bugzilla.redhat.com/show_bug.cgi?id=628004

* Wed Apr  6 2011 Lennart Poettering <lpoetter@redhat.com> - 24-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=694079
- https://bugzilla.redhat.com/show_bug.cgi?id=693289
- https://bugzilla.redhat.com/show_bug.cgi?id=693274
- https://bugzilla.redhat.com/show_bug.cgi?id=693161

* Tue Apr  5 2011 Lennart Poettering <lpoetter@redhat.com> - 23-1
- New upstream release
- Include systemd-sysv-convert

* Fri Apr  1 2011 Lennart Poettering <lpoetter@redhat.com> - 22-1
- New upstream release

* Wed Mar 30 2011 Lennart Poettering <lpoetter@redhat.com> - 21-2
- The quota services are now pulled in by mount points, hence no need to enable them explicitly

* Tue Mar 29 2011 Lennart Poettering <lpoetter@redhat.com> - 21-1
- New upstream release

* Mon Mar 28 2011 Matthias Clasen <mclasen@redhat.com> - 20-2
- Apply upstream patch to not send untranslated messages to plymouth

* Tue Mar  8 2011 Lennart Poettering <lpoetter@redhat.com> - 20-1
- New upstream release

* Tue Mar  1 2011 Lennart Poettering <lpoetter@redhat.com> - 19-1
- New upstream release

* Wed Feb 16 2011 Lennart Poettering <lpoetter@redhat.com> - 18-1
- New upstream release

* Mon Feb 14 2011 Bill Nottingham <notting@redhat.com> - 17-6
- bump upstart obsoletes (#676815)

* Wed Feb  9 2011 Tom Callaway <spot@fedoraproject.org> - 17-5
- add macros.systemd file for %%{_unitdir}

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  9 2011 Lennart Poettering <lpoetter@redhat.com> - 17-3
- Fix popen() of systemctl, #674916

* Mon Feb  7 2011 Bill Nottingham <notting@redhat.com> - 17-2
- add epoch to readahead obsolete

* Sat Jan 22 2011 Lennart Poettering <lpoetter@redhat.com> - 17-1
- New upstream release

* Tue Jan 18 2011 Lennart Poettering <lpoetter@redhat.com> - 16-2
- Drop console.conf again, since it is not shipped in pamtmp.conf

* Sat Jan  8 2011 Lennart Poettering <lpoetter@redhat.com> - 16-1
- New upstream release

* Thu Nov 25 2010 Lennart Poettering <lpoetter@redhat.com> - 15-1
- New upstream release

* Thu Nov 25 2010 Lennart Poettering <lpoetter@redhat.com> - 14-1
- Upstream update
- Enable hwclock-load by default
- Obsolete readahead
- Enable /var/run and /var/lock on tmpfs

* Fri Nov 19 2010 Lennart Poettering <lpoetter@redhat.com> - 13-1
- new upstream release

* Wed Nov 17 2010 Bill Nottingham <notting@redhat.com> 12-3
- Fix clash

* Wed Nov 17 2010 Lennart Poettering <lpoetter@redhat.com> - 12-2
- Don't clash with initscripts for now, so that we don't break the builders

* Wed Nov 17 2010 Lennart Poettering <lpoetter@redhat.com> - 12-1
- New upstream release

* Fri Nov 12 2010 Matthias Clasen <mclasen@redhat.com> - 11-2
- Rebuild with newer vala, libnotify

* Thu Oct  7 2010 Lennart Poettering <lpoetter@redhat.com> - 11-1
- New upstream release

* Wed Sep 29 2010 Jesse Keating <jkeating@redhat.com> - 10-6
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Bill Nottingham <notting@redhat.com> - 10-5
- merge -sysvinit into main package

* Mon Sep 20 2010 Bill Nottingham <notting@redhat.com> - 10-4
- obsolete upstart-sysvinit too

* Fri Sep 17 2010 Bill Nottingham <notting@redhat.com> - 10-3
- Drop upstart requires

* Tue Sep 14 2010 Lennart Poettering <lpoetter@redhat.com> - 10-2
- Enable audit
- https://bugzilla.redhat.com/show_bug.cgi?id=633771

* Tue Sep 14 2010 Lennart Poettering <lpoetter@redhat.com> - 10-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=630401
- https://bugzilla.redhat.com/show_bug.cgi?id=630225
- https://bugzilla.redhat.com/show_bug.cgi?id=626966
- https://bugzilla.redhat.com/show_bug.cgi?id=623456

* Fri Sep  3 2010 Bill Nottingham <notting@redhat.com> - 9-3
- move fedora-specific units to initscripts; require newer version thereof

* Fri Sep  3 2010 Lennart Poettering <lpoetter@redhat.com> - 9-2
- Add missing tarball

* Fri Sep  3 2010 Lennart Poettering <lpoetter@redhat.com> - 9-1
- New upstream version
- Closes 501720, 614619, 621290, 626443, 626477, 627014, 627785, 628913

* Fri Aug 27 2010 Lennart Poettering <lpoetter@redhat.com> - 8-3
- Reexecute after installation, take ownership of /var/run/user
- https://bugzilla.redhat.com/show_bug.cgi?id=627457
- https://bugzilla.redhat.com/show_bug.cgi?id=627634

* Thu Aug 26 2010 Lennart Poettering <lpoetter@redhat.com> - 8-2
- Properly create default.target link

* Wed Aug 25 2010 Lennart Poettering <lpoetter@redhat.com> - 8-1
- New upstream release

* Thu Aug 12 2010 Lennart Poettering <lpoetter@redhat.com> - 7-3
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=623561

* Thu Aug 12 2010 Lennart Poettering <lpoetter@redhat.com> - 7-2
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=623430

* Tue Aug 10 2010 Lennart Poettering <lpoetter@redhat.com> - 7-1
- New upstream release

* Fri Aug  6 2010 Lennart Poettering <lpoetter@redhat.com> - 6-2
- properly hide output on package installation
- pull in coreutils during package installtion

* Fri Aug  6 2010 Lennart Poettering <lpoetter@redhat.com> - 6-1
- New upstream release
- Fixes #621200

* Wed Aug  4 2010 Lennart Poettering <lpoetter@redhat.com> - 5-2
- Add tarball

* Wed Aug  4 2010 Lennart Poettering <lpoetter@redhat.com> - 5-1
- Prepare release 5

* Tue Jul 27 2010 Bill Nottingham <notting@redhat.com> - 4-4
- Add 'sysvinit-userspace' provide to -sysvinit package to fix upgrade/install (#618537)

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-3
- Add libselinux to build dependencies

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-2
- Use the right tarball

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-1
- New upstream release, and make default

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-3
- Used wrong tarball

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-2
- Own /cgroup jointly with libcgroup, since we don't dpend on it anymore

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-1
- New upstream release

* Fri Jul 9 2010 Lennart Poettering <lpoetter@redhat.com> - 2-0
- New upstream release

* Wed Jul 7 2010 Lennart Poettering <lpoetter@redhat.com> - 1-0
- First upstream release

* Tue Jun 29 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.7.20100629git4176e5
- New snapshot
- Split off -units package where other packages can depend on without pulling in the whole of systemd

* Tue Jun 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.6.20100622gita3723b
- Add missing libtool dependency.

* Tue Jun 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.5.20100622gita3723b
- Update snapshot

* Mon Jun 14 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.4.20100614git393024
- Pull the latest snapshot that fixes a segfault. Resolves rhbz#603231

* Fri Jun 11 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.3.20100610git2f198e
- More minor fixes as per review

* Thu Jun 10 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.2.20100610git2f198e
- Spec improvements from David Hollis

* Wed Jun 09 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.1.20090609git2f198e
- Address review comments

* Tue Jun 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.0.git2010-06-02
- Initial spec (adopted from Kay Sievers)
