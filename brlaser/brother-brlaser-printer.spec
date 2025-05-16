%global forgeurl https://github.com/pdewacht/brlaser
%global commit   9d7ddda8383bfc4d205b5e1b49de2b8bcd9137f1
%global date     20200420

Name:           brother-brlaser-printer
Version:        6
%forgemeta
Release:        3%{?dist}
Summary:        Brother laser printer driver

License:        GPL-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         patch-20210908.patch
Patch1:         tempfile.h.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cups-devel
Requires:       cups-filesystem
Requires:       ghostscript

%description
brlaser is a CUPS driver for Brother laser printers.

Although most Brother printers support a standard printer language
such as PCL or PostScript, not all do. If you have a monochrome
Brother laser printer (or multi-function device) and the other open
source drivers don't work, this one might help.

For a detailed list of supported printers, please refer to
%{forgeurl}

%prep
%forgesetup
%patch -P0 -p1
%patch -P1

%build
%cmake
%cmake_build
# %dnl cmake_build --target rastertobrlaser

%install
%cmake_install
#printf "=> '_cups_serverbin'='%s'\n" %{_cups_serverbin}
#printf "=> '_datadir'='%s'\n" %{_datadir}

%files
%{_cups_serverbin}/filter/rastertobrlaser
%{_datadir}/cups/drv/brlaser.drv
%doc README.md

%changelog
* Fri May 16 2025 Jan Musinsky <musinsky@gmail.com> - 6-3
- Package brlaser officially in Fedora and EPEL repositories (released 2022-05)
- Now brlaser only as source package example (simple and quick compilation)
- Add patches from GitHub pull requests 175

* Thu Oct 07 2021 Jan Musinsky <musinsky@gmail.com> - 6-2
- Fedora 35
- Add patches from GitHub pull requests 92, 107 and 133

* Sat Jan 30 2021 Jan Musinsky <musinsky@gmail.com> - 6-1
- First release for Fedora 33
- Patch adds support for Brother DCP-7070DW model
