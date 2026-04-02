#!/usr/bin/env bash

# 2026-04-02
# https://github.com/musinsky/rpms/blob/rawhide/root5/root5-get.master.files.sh

CUR_DIR="$PWD"
ROOT_GH="https://raw.githubusercontent.com/root-project/root/master"

ROOT5_DIR="${TMPDIR:-/tmp}"
ROOT5_DIR="$ROOT5_DIR/ROOT5"
mkdir "$ROOT5_DIR" && cd "$ROOT5_DIR" || exit

ROOT5_RMKDEPEND="build/rmkdepend"
# ROOT master "misc/rmkdepend/" != ROOT 5 "build/rmkdepend/"
FILES=( "cppsetup.c" "def.h" "ifparser.c" "ifparser.h" "imakemdep.h"
        "include.c" "main.c" "mainroot.cxx" "parse.c" "pr.c" )
for FF in "${FILES[@]}"; do
    curl --silent --write-out "%{url}\n=> %{filename_effective}\n" \
         --location "$ROOT_GH/misc/rmkdepend/$FF" \
         --remote-name --output-dir "$ROOT5_RMKDEPEND" --create-dirs
done

ROOT5_MINICERN="misc/minicern/src"
# ROOT master "misc/minicern/src/" == ROOT 5 "misc/minicern/src/"
FILES=( "cernlib.c" "hbook.f" "kernlib.f" "zebra.f" )
for FF in "${FILES[@]}"; do
    curl --silent --write-out "%{url}\n=> %{filename_effective}\n" \
         --location "$ROOT_GH/misc/minicern/src/$FF" \
         --remote-name --output-dir "$ROOT5_MINICERN" --create-dirs
done

TGZ_FILE="root.master.files.tar.gz"
tar -czf "$TGZ_FILE" "$ROOT5_RMKDEPEND" "$ROOT5_MINICERN"
mv --verbose "$TGZ_FILE" "$CUR_DIR/"
rm -rf "$ROOT5_DIR"
