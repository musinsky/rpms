#!/usr/bin/env bash

# 2026-04-14
# https://github.com/musinsky/rpms/blob/rawhide/root5/root5.get.root.master.files.sh

CUR_DIR="$PWD"
ROOT_GH="https://raw.githubusercontent.com/root-project/root/master"
ROOT_API="https://api.github.com/repos/root-project/root/commits"

ROOT5_DIR="${TMPDIR:-/tmp}"
ROOT5_DIR="$ROOT5_DIR/ROOT5"
mkdir "$ROOT5_DIR" && cd "$ROOT5_DIR" || exit

RMKDEPEND_DIR5="build/rmkdepend" # ROOT 5
RMKDEPEND_DIR="misc/rmkdepend"   # ROOT master
FILES=( "cppsetup.c" "def.h" "ifparser.c" "ifparser.h" "imakemdep.h"
        "include.c" "main.c" "mainroot.cxx" "parse.c" "pr.c" )
for FF in "${FILES[@]}"; do
    curl --silent --write-out "%{url}\n=> %{filename_effective}\n" \
         --location "$ROOT_GH/$RMKDEPEND_DIR/$FF" \
         --remote-name --output-dir "$RMKDEPEND_DIR5" --create-dirs
done
RMKDEPEND_DATE=$(curl --silent "$ROOT_API?path=$RMKDEPEND_DIR&per_page=1" |
                     jq --raw-output '.[0].commit.committer.date')
printf "Last commit: %s in 'root/master/%s/' dir\n\n" \
       "$RMKDEPEND_DATE"  "$RMKDEPEND_DIR"

MINICERN_DIR5="misc/minicern/src" # ROOT 5
MINICERN_DIR="misc/minicern/src"  # ROOT master
FILES=( "cernlib.c" "hbook.f" "kernlib.f" "zebra.f" )
for FF in "${FILES[@]}"; do
    curl --silent --write-out "%{url}\n=> %{filename_effective}\n" \
         --location "$ROOT_GH/$MINICERN_DIR/$FF" \
         --remote-name --output-dir "$MINICERN_DIR5" --create-dirs
done
MINICERN_DATE=$(curl --silent "$ROOT_API?path=$MINICERN_DIR&per_page=1" |
                    jq --raw-output '.[0].commit.committer.date')
printf "Last commit: %s in 'root/master/%s/' dir\n\n" \
       "$MINICERN_DATE" "$MINICERN_DIR"

LAST_DATE="$RMKDEPEND_DATE"
[[ "$MINICERN_DATE" > "$RMKDEPEND_DATE" ]] && LAST_DATE="$MINICERN_DATE"
LAST_DATE=$(date --date "$LAST_DATE" +%F)
TGZ_FILE="root5.with.root.master.$LAST_DATE.files.tar.gz"
tar -czf "$TGZ_FILE" "$RMKDEPEND_DIR5" "$MINICERN_DIR5"
mv --verbose "$TGZ_FILE" "$CUR_DIR/"
rm -rf "$ROOT5_DIR"
