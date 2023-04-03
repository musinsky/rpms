# 2023-04-03

# TODO rewrite as Makefile

PACKAGE='hunspell-sk'

GHRAW="https://raw.githubusercontent.com/musinsky/rpms/rawhide/$PACKAGE"
RPM_SPEC_DIR=$(rpm --eval %{_specdir})
RPM_SOURCE_DIR=$(rpm --eval %{_sourcedir})

wget --timestamping "$GHRAW/$PACKAGE.spec" --directory-prefix="$RPM_SPEC_DIR"
rpmdev-spectool --get-files --sourcedir "$RPM_SPEC_DIR/$PACKAGE.spec"
rpmbuild -bs "$RPM_SPEC_DIR/$PACKAGE.spec"   # build just the source package
