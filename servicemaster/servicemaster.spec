Name:      servicemaster
Version:   1.8.0
Release:   1%{?dist}
Summary:   Linux Systemd administration tool with nice TUI

License:   MIT
URL:       https://github.com/Lennart1978/servicemaster
Source:    https://github.com/Lennart1978/servicemaster/archive/V%{version}/%{name}-%{version}.tar.gz

BuildRequires: meson cmake gcc
BuildRequires: ncurses-devel systemd-devel

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Meson/
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Debuginfo/
%global debug_package %{nil}

%description
ServiceMaster is a powerful terminal-based tool for managing Systemd units
on Linux systems. It provides an intuitive interface for viewing and controlling
system and user units, making it easier to manage your units without leaving
the command line.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
install -Dpm 0644 %{name}.toml \
        %{buildroot}%{_sysconfdir}/%{name}/%{name}.toml

%check
# no test

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/%{name}/%{name}.toml

%changelog
* Wed Oct 14 2026 Jan Musinsky <musinsky@gmail.com> - 1.8.0-1
- Initial servicemaster build
