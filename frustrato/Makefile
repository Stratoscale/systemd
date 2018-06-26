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
	git archive --format=tar.gz --prefix=$(SYSTEMD_BASE_VERSION)/ --output=$(RPMBUILD)/SOURCES/$(SYSTEMD_BASE_VERSION).tar.xz HEAD
	@echo "Updating spec file release version"
	sed -i -e "s/^Source0:.*/Source0:        $(SYSTEMD_TAR)/" $(SPEC)
	sed -i -e "s/^Release.*/&$(SYSTEMD_BUILDID)/" $(SPEC)

rpms: prepare_for_build
	@echo "Building the RPMs"
	rpmbuild -D "_topdir $(RPMBUILD)" -D "dist .el7_5" -bb $(SPEC)

.PHONY: rpms
