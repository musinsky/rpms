%global name_upstream Authenticator

Name:      authenticator
Version:   4.6.2
Release:   1%{?dist}
Summary:   Generate two-factor codes

License:   GNU GPLv3
URL:       https://apps.gnome.org/Authenticator/
Source:    https://gitlab.gnome.org/World/%{name_upstream}/-/archive/%{version}/%{name_upstream}-%{version}.tar.gz
Patch1:    https://raw.githubusercontent.com/musinsky/rpms/rawhide/%{name}/Cargo.OpenSSLv4.patch
Source10:  https://raw.githubusercontent.com/musinsky/rpms/rawhide/%{name}/cern_provider_down.sql
Source11:  https://raw.githubusercontent.com/musinsky/rpms/rawhide/%{name}/cern_provider_up.sql

BuildRequires: meson
BuildRequires: cargo-rpm-macros cargo rust
BuildRequires: glib2-devel gtk4-devel libadwaita-devel
BuildRequires: gstreamer1-devel gstreamer1-plugins-base-devel
BuildRequires: gettext desktop-file-utils appstream

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Meson/
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Debuginfo/
%global debug_package %{nil}

%description
Simple application for generating Two-Factor Authentication Codes.
More info on https://apps.gnome.org/Authenticator/ page.

%prep
%autosetup -n %{name_upstream}-%{version} -p0

mkdir -p migrations/2026-10-10_cern_provider/
cp %{SOURCE10} migrations/2026-10-10_cern_provider/down.sql
cp %{SOURCE11} migrations/2026-10-10_cern_provider/up.sql

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
# no test

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/gnome-shell/search-providers/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/hicolor/symbolic/apps/*
%{_datadir}/metainfo/*

%changelog
* Wed Oct 14 2026 Jan Musinsky <musinsky@gmail.com> - 4.6.2-1
- Initial Authenticator build
