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
	sudo yum-builddep --assumeyes $(ORIG_SPEC)

clean:
	sudo rm -fr $(RPMBUILD)
	make -C $(SYSTEMD) $@

distclean: clean
	make -C $(SYSTEMD) $@

sources:
	mkdir -p $(RPMBUILD)/SOURCES
	cp $(FRUSTRATO)/centos/SOURCES/* $(RPMBUILD)/SOURCES/
	$(SYSTEMD)/autogen.sh
	$(SYSTEMD)/configure CFLAGS='-g -O0' --sysconfdir=/etc --localstatedir=/var --libdir=/usr/lib64 --enable-gtk-doc
	make -C $(SYSTEMD) all -j$(PARALLEL)
	make -C $(SYSTEMD) dist-xz -j$(PARALLEL)
	mv $(SYSTEMD)/$(SYSTEMD_TAR) $(SOURCE0)

spec:
	mkdir -p $(dir $(SPEC))
	sed -e "s/^Source0:.*/Source0: $(SYSTEMD_TAR)/" \
	    -e "s/^Release.*/&$(SYSTEMD_BUILDID)/" $(ORIG_SPEC) > $(SPEC)

systemd: sources spec
	rpmbuild -D "_topdir $(RPMBUILD)" -D "dist .el7_0" -bb $(SPEC)

.PHONY: rpms
