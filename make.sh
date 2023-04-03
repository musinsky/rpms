# 2023-04-04

# TODO rewrite as Makefile

PACKAGE='hunspell-sk'

# GHRAW="https://raw.githubusercontent.com/musinsky/rpms/rawhide/$PACKAGE"
# RPM_SOURCE_DIR=$(rpm --eval %{_sourcedir})
RPM_SPEC_DIR=$(rpm --eval %{_specdir})

rpmdev-setuptree
# wget --timestamping "$GHRAW/$PACKAGE.spec" --directory-prefix="$RPM_SPEC_DIR"
cp -p "$PACKAGE/$PACKAGE.spec" "$RPM_SPEC_DIR/$PACKAGE.spec"
rpmdev-spectool --get-files --sourcedir "$RPM_SPEC_DIR/$PACKAGE.spec"
rpmbuild -bs "$RPM_SPEC_DIR/$PACKAGE.spec"   # build just the source package
