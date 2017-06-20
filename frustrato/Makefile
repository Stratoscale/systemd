all: rpms

SYSTEMD = $(CURDIR)
FRUSTRATO = $(SYSTEMD)/frustrato
RPMBUILD = $(FRUSTRATO)/build

ORIG_SPEC = $(FRUSTRATO)/centos/SPECS/systemd.spec
VERSION = $(shell grep "^Version:" $(ORIG_SPEC) | awk '{print $$2}')
SPEC = $(FRUSTRATO)/build/SPECS/systemd.spec

SYSTEMD_HASH = $(shell git rev-parse --short=12 HEAD)
SYSTEMD_BUILDID = .strato.$(SYSTEMD_HASH)

SYSTEMD_TAR = systemd-$(VERSION).tar.xz
SOURCE0 = $(RPMBUILD)/SOURCES/$(SYSTEMD_TAR)

PARALLEL = $(shell grep -c processor /proc/cpuinfo)

rpms: systemd

submit:
	solvent submitproduct rpms $(RPMBUILD)/RPMS/x86_64

approve:
	solvent approve --product=rpms

prepareForCleanBuild:
	sudo yum install $(CENTOS72_RPMS_TO_INSTALL_FOR_BUILD) --assumeyes --nogpgcheck
	sudo yum-builddep --assumeyes $(ORIG_SPEC)
	mkdir -p /usr/share/unifont
	cp frustrato/unifont-5.1.20080808.hex /usr/share/unifont/unifont.hex

clean:
	sudo rm -fr $(RPMBUILD)
	-make -C $(SYSTEMD) $@

distclean: clean
	-make -C $(SYSTEMD) $@

sources: clean
	mkdir -p $(RPMBUILD)/SOURCES
	cp $(FRUSTRATO)/centos/SOURCES/* $(RPMBUILD)/SOURCES/
	$(SYSTEMD)/autogen.sh
	$(SYSTEMD)/configure CFLAGS='-g -O0' --sysconfdir=/etc --localstatedir=/var --libdir=/usr/lib64 --enable-gtk-doc
	make -C $(SYSTEMD) all -j$(PARALLEL)
	make -C $(SYSTEMD) dist-xz -j$(PARALLEL)
	mv $(SYSTEMD)/$(SYSTEMD_TAR) $(SOURCE0)

spec: clean
	mkdir -p $(dir $(SPEC))
	sed -e "s/^Source0:.*/Source0: $(SYSTEMD_TAR)/" \
	    -e "s/^Release.*/&$(SYSTEMD_BUILDID)/" $(ORIG_SPEC) > $(SPEC)

systemd: sources spec
	rpmbuild -D "_topdir $(RPMBUILD)" -D "dist .el7_0" -bb $(SPEC)

.PHONY: rpms

# we need kmod >= 15 to build systemd v219-19/
CENTOS_7_2_MIRROR = http://yumcache.strato/mirrors/www/mirror/centos-7/7.2.1511
CENTOS72_RPMS_TO_INSTALL_FOR_BUILD = \
	$(CENTOS_7_2_MIRROR)/os/x86_64/Packages/kmod-20-5.el7.x86_64.rpm \
	$(CENTOS_7_2_MIRROR)/os/x86_64/Packages/kmod-devel-20-5.el7.x86_64.rpm \
	$(CENTOS_7_2_MIRROR)/os/x86_64/Packages/kmod-libs-20-5.el7.x86_64.rpm \
	$(CENTOS_7_2_MIRROR)/os/x86_64/Packages/libevdev-1.4.1-1.el7.x86_64.rpm \
	$(CENTOS_7_2_MIRROR)/os/x86_64/Packages/libevdev-devel-1.4.1-1.el7.x86_64.rpm\
	$(CENTOS_7_2_MIRROR)/os/x86_64/Packages/libevdev-utils-1.4.1-1.el7.x86_64.rpm \
	$(CENTOS_7_2_MIRROR)/os/x86_64/Packages/libdrm-2.4.60-3.el7.x86_64.rpm \
	$(CENTOS_7_2_MIRROR)/os/x86_64/Packages/libdrm-devel-2.4.60-3.el7.x86_64.rpm \
	$(CENTOS_7_2_MIRROR)/os/x86_64/Packages/libxkbfile-1.0.8-5.el7.x86_64.rpm \
	$(CENTOS_7_2_MIRROR)/os/x86_64/Packages/libxkbfile-devel-1.0.8-5.el7.x86_64.rpm \
