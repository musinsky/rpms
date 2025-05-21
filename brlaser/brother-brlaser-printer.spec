%global forgeurl https://github.com/pdewacht/brlaser
%global commit   9d7ddda8383bfc4d205b5e1b49de2b8bcd9137f1
%global date     20200420

%dnl #$ rpmdev-spectool -g -R $(rpm -E %{_specdir})/brother-brlaser-printer.spec
%dnl #$ rpmspec --parse $(rpm --eval %{_specdir})/brother-brlaser-printer.spec
%dnl #$ rpmbuild --nobuild --nodeps $(rpm --eval %{_specdir})/brother-brlaser-printer.spec
%dnl #$ rpmbuild -bb $(rpm --eval %{_specdir})/brother-brlaser-printer.spec --noclean

Name:           brother-brlaser-printer
Version:        6
%forgemeta -i   # flag '-i' for info or flag '-v' for verbose
Release:        3%{?dist}
Summary:        Brother laser printer driver

License:        GPL-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         https://raw.githubusercontent.com/musinsky/rpms/rawhide/brlaser/patch-20210908.patch
Patch1:         https://raw.githubusercontent.com/musinsky/rpms/rawhide/brlaser/tempfile.h.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cups-devel
Requires:       cups-filesystem
Requires:       ghostscript

%description
brlaser is a CUPS driver for Brother laser printers. For a detailed list
of supported printers, please refer to %{forgeurl}

%prep
%forgesetup -v  # flag '-v' for verbose, after this point forgemeta is no longer used
%patch -P0 -p1
%patch -P1

%build
%cmake
%cmake_build
%dnl # cmake_build --target rastertobrlaser

%install
%cmake_install
%dnl # only as example
%dnl # %global cups_serverbin_2 %(/usr/bin/cups-config --serverbin)
%dnl # printf "=> 'cups_serverbin_2' = '%s'\n" %{cups_serverbin_2}

%files
%{_cups_serverbin}/filter/rastertobrlaser
%{_datadir}/cups/drv/brlaser.drv
%doc README.md

%changelog
* Wed May 21 2025 Jan Musinsky <musinsky@gmail.com> - 6-3
- Package brlaser officially in Fedora and EPEL repositories (released 2022-05)
- Now brlaser only as source package example (simple and quick compilation)
