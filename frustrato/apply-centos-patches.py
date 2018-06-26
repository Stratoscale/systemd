#!/usr/bin/env python
import subprocess
import sys
import os

if __name__ == "__main__":
    spec_file_path = sys.argv[1]
    if not os.path.exists(spec_file_path):
        print "BAD spec file path: '%s'" % spec_file_path
        sys.exit(1)

    patch_list = subprocess.check_output("egrep 'Patch[0-9]*\:' %s" % spec_file_path, shell=True)
    for patch in patch_list.strip().split('\n'):
        ppath = subprocess.check_output("find . | grep %s" % patch.split(' ')[1], shell=True)[:-1]
        print "APPLYING[%s]: %s" % (patch.split(' ')[0][:-1], ppath)
        subprocess.check_output("git am %s" % ppath, shell=True)
