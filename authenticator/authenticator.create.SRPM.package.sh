#!/usr/bin/env bash

# 2026-10-15
# https://github.com/musinsky/rpms/blob/rawhide/authenticator/authenticator.create.SRPM.package.sh

check_command() {
  local cmd="$1"
  local rpm="$2"
  command -v "$cmd" > /dev/null || {
    printf "# missing command '%s' => " "$cmd"
    printf "$ sudo dnf install %s\n" "$rpm"
    exit
  }
}
create_cargo_vendor() {
  local src_file
  # src_file="$(rpmdev-spectool --list-files "$SPECS_DIR/$FSPEC" | grep Source0)"
  # 'rpmspec' is more universal than 'rpmdev-spectool'
  src_file="$(rpmspec --parse "$SPECS_DIR/$FSPEC" | grep Source0)"
  src_file="${src_file##*/}"
  local src_vendor_file="${src_file%.tar.gz}-cargo-vendor.tar.gz"
  local sources_dir
  sources_dir="$(rpm --eval '%{_sourcedir}')"
  local tmp_dir
  tmp_dir="$(mktemp --directory)" || return
  local current_dir
  current_dir="$(pwd)"
  tar -xzf "$sources_dir/$src_file" -C "$tmp_dir" --strip-components=1
  mkdir -p "$tmp_dir/.cargo"
  cd "$tmp_dir" || return
  cargo vendor --locked vendor > .cargo/config.toml   # 'vendor' (default) dir
  tar -czf "$sources_dir/$src_vendor_file" vendor .cargo/config.toml
  cd "$current_dir" || return
  rm -rf "$tmp_dir"
}

check_command rpmbuild rpm-build
check_command rpmspec  rpm-build
check_command rpmdev-spectool rpmdevtools
check_command cargo cargo

GHC="https://raw.githubusercontent.com/musinsky/rpms/rawhide/authenticator/"
FSPEC="authenticator.spec"
SPECS_DIR="$(rpm --eval '%{_specdir}')"

# download specfile
curl --silent --location "$GHC/$FSPEC" \
     --remote-name --output-dir "$SPECS_DIR" --create-dirs

# download sources and patches from specfile
rpmdev-spectool --get-files --sourcedir "$SPECS_DIR/$FSPEC"

create_cargo_vendor

# build SRPM package
rpmbuild -bs "$SPECS_DIR/$FSPEC"   # -bs (source), -bb (binary), -ba (all)
