#!/usr/bin/env bash

# 2026-04-22
# https://github.com/musinsky/rpms/blob/rawhide/hunspell-ru-wiki/hunspell-ru-wiki.create.SRPM.package.sh

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

GHC="https://raw.githubusercontent.com/musinsky/rpms/rawhide/hunspell-ru-wiki/"
FSPEC="hunspell-ru-wiki.spec"
SPECS_DIR="$(rpm --eval '%{_specdir}')"

# download specfile
curl --silent --location "$GHC/$FSPEC" \
     --remote-name --output-dir "$SPECS_DIR" --create-dirs

# download sources and patches from specfile
rpmdev-spectool --get-files --sourcedir "$SPECS_DIR/$FSPEC"

# build SRPM package
rpmbuild -bs "$SPECS_DIR/$FSPEC"   # -bs (source), -bb (binary), -ba (all)
