all: rpms

PARALLEL = $(shell grep -c processor /proc/cpuinfo)

SYSTEMD_BASE_VERSION = systemd-219

SYSTEMD = $(CURDIR)
FRUSTRATO_BUILD = $(CURDIR)/frustrato/build
RPMBUILD = $(CURDIR)/build
SPEC = $(RPMBUILD)/SPECS/systemd.spec

BUILDID ?= .strato
SYSTEMD_HASH = $(shell git rev-parse --short HEAD)
SYSTEMD_BUILDID = $(BUILDID).$(SYSTEMD_HASH)
SYSTEMD_TAR = $(SYSTEMD_BASE_VERSION).tar.xz
SOURCE0 = $(RPMBUILD)/SOURCES/$(SYSTEMD_TAR)


clean:
	rm -rf $(RPMBUILD)
	-make -C $(SYSTEMD) $@

prepare_for_build: clean
	@echo "Preparing build folders"
	mkdir -p $(RPMBUILD)
	cp -rf $(FRUSTRATO_BUILD)/* $(RPMBUILD)
	$(SYSTEMD)/autogen.sh
	$(SYSTEMD)/configure CFLAGS='-g -O0' --sysconfdir=/etc --localstatedir=/var --libdir=/usr/lib64 --enable-gtk-doc --enable-compat-libs
	make -C $(SYSTEMD) all -j$(PARALLEL)
	make -C $(SYSTEMD) dist-xz -j$(PARALLEL)
	mv $(SYSTEMD)/$(SYSTEMD_TAR) $(SOURCE0)
	@echo "Updating spec file release version"
	sed -i -e "s/^Source0:.*/Source0:        $(SYSTEMD_TAR)/" $(SPEC)
	sed -i -e "s/^Release.*/&$(SYSTEMD_BUILDID)/" $(SPEC)

rpms: prepare_for_build
	@echo "Building the RPMs"
	rpmbuild -D "_topdir $(RPMBUILD)" -D "dist .el7_0" -bb $(SPEC)

.PHONY: rpms
