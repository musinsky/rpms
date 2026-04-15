%global forgeurl https://github.com/root-project/root
%global branch   v5-34-00-patches
%global commit   8943a403dfda3a5a46890c41757f4207526f7048
%global date     20250910
%forgemeta -i

%global prefix_root5 /opt/root5
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Debuginfo/
%global debug_package %{nil}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_shebang_lines
%undefine __brp_mangle_shebangs

Name:      root5
Version:   5.34.39
# always increment release number (root5-5.34.39-1.20250910git8943a40)
Release:   1%{?dist}
License:   LGPL 2.1
URL:       https://root.cern.ch
Summary:   Numerical data analysis framework

Source0:   %{forgesource}
Source1:   root5.with.root.master.2026-02-18.files.tar.gz
Patch10:   https://raw.githubusercontent.com/musinsky/rpms/rawhide/root5/g__cfunc.c.patch
Patch90:   https://raw.githubusercontent.com/musinsky/rpms/rawhide/root5/HighlightROOT5.patch

BuildRequires: gcc gcc-c++ gcc-gfortran make
BuildRequires: libjpeg-devel libpng-devel
Requires:      bash

%description
ROOT is open source data analysis framework used by high energy physics
and others, born at CERN.

This is legacy ROOT5 version that is no longer being developed.

%prep
# forgesetup = uncompress SOURCE0, cd, chmod
%forgesetup -v
tar -xzf %{SOURCE1}
# patches have different format
%patch -P 10 -b .orig
%patch -P 90 -p 1 -b .orig

echo $(pwd)
echo %{prefix_root5}

%build
./configure --prefix=%{prefix_root5} \
            --libdir=%{prefix_root5}/lib \
            --incdir=%{prefix_root5}/include \
            --etcdir=%{prefix_root5}/etc \
            --datadir=%{prefix_root5} \
            --mandir=%{prefix_root5}/man/man1 \
            --docdir=%{prefix_root5}/README \
            --testdir=%{prefix_root5}/test \
            --tutdir=%{prefix_root5}/tutorials \
            --aclocaldir=/tmp/null \
            --elispdir=/tmp/null \
            --gminimal \
            --disable-builtin-afterimage \
            --disable-builtin-ftgl \
            --disable-builtin-freetype \
            --disable-builtin-glew \
            --disable-builtin-pcre \
            --disable-builtin-zlib \
            --disable-builtin-lzma \
            --disable-builtin-lz4 \
            --enable-asimage \
            --enable-astiff \
            --enable-cintex \
            --enable-reflex \
            --enable-gviz \
            --enable-genvector \
            --enable-mysql \
            --enable-opengl \
            --enable-soversion \
            --enable-sqlite \
            --enable-xft \
            --enable-xml \
            --with-mysql-incdir=/usr/include/mysql/

# Enabled support for asimage, astiff, cintex, explicitlink, gviz, genvector,
# mysql, opengl, reflex, shadowpw, shared, soversion, sqlite, x11, xft, xml.

echo %{?_smp_mflags}
make %{?_smp_mflags}
make

%install
# make_install = install to DESTDIR=$HOME/rpmbuild/BUILD/root5-5.34.39-build/BUILDROOT
#              = %%{buildroot}
%make_install

echo $(pwd)
echo %{buildroot}%{prefix_root5}

rm -rf %{buildroot}/tmp/
rm -rf %{buildroot}%{prefix_root5}/tutorials/pyroot/
rm -rf %{buildroot}%{prefix_root5}/tutorials/eve/lineset.py
rm -rf %{buildroot}%{prefix_root5}/tutorials/histfactory/makeQuickModel.py
rm -rf %{buildroot}%{prefix_root5}/tutorials/histfactory/example.py

# %%clean
# clean in modern rpm (rpmbuild 4.6+) is deprecated

# %%check
# make any test

%files
%{prefix_root5}

# rpmspec --parse $HOME/rpmbuild/SPECS/root5.spec
# rpmlint         $HOME/rpmbuild/SPECS/root5.spec
# rpmbuild -bb    $HOME/rpmbuild/SPECS/root5.spec
# rpmbuild -bb --noclean $HOME/rpmbuild/SPECS/root5.spec

%changelog
* Wed Apr 15 2026 Jan Musinsky <musinsky@gmail.com> - 5.34.39-1
- Initial ROOT 5 build
