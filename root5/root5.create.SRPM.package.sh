#!/usr/bin/env bash

# 2026-04-15
# https://github.com/musinsky/rpms/blob/rawhide/root5/root5.create.SRPM.package.sh

check_command() {
    local cmd="$1"
    local rpm="$2"
    command -v "$cmd" > /dev/null || {
        printf "# missing command '%s' => " "$cmd"
        printf "$ sudo dnf install %s\n" "$rpm"
        exit
    }
}

check_command rpmbuild rpm-build
check_command rpmdev-spectool rpmdevtools
check_command jq jq   # root5.get.root.master.files.sh

GHC="https://raw.githubusercontent.com/musinsky/rpms/rawhide/root5/"
SPECS_DIR="$(rpm --eval '%{_specdir}')"
SOURCES_DIR="$(rpm --eval '%{_sourcedir}')"

# download specfile
curl --silent --location "$GHC/root5.spec" \
     --remote-name --output-dir "$SPECS_DIR" --create-dirs

# download sources and patches from specfile
rpmdev-spectool --get-files --sourcedir "$SPECS_DIR/root5.spec"

# manually download another source
curl --silent --location "$GHC/root5.get.root.master.files.sh" | bash -s "$SOURCES_DIR"

# build SRPM package
rpmbuild -bs "$SPECS_DIR/root5.spec"   # -bs (source), -bb (binary), -ba (all)
