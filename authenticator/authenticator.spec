%global name_upstream Authenticator
%global forgeurl   https://gitlab.gnome.org/World/%{name_upstream}
%global commit     6380a4b232acee4cb524bbe43e3aabf15d1cc745
%global date       20260922
%global archiveext tar.gz
%forgemeta -i

Name:      authenticator
Version:   4.6.2
Release:   1%{?dist}
Summary:   Generate two-factor codes

License:   GPL-3.0-or-later
URL:       %{forgeurl}
Source0:   %{forgesource}
Source1:   %{name_upstream}-%{commit}-cargo-vendor.tar.gz
Source10:  https://raw.githubusercontent.com/musinsky/rpms/rawhide/%{name}/cern_provider_down.sql
Source11:  https://raw.githubusercontent.com/musinsky/rpms/rawhide/%{name}/cern_provider_up.sql

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Meson/
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Debuginfo/
%global debug_package %{nil}

BuildRequires: meson
%if 0%{?fedora} > 43 || 0%{?rhel} > 9
BuildRequires: cargo-rpm-macros
%else
BuildRequires: rust-packaging
%endif
BuildRequires: openssl-devel sqlite-devel
BuildRequires: gettext desktop-file-utils appstream
# $ dnf repoquery --whatprovides 'pkgconfig(glib-2.0)'
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)

%description
Simple application for generating Two-Factor Authentication Codes.
More info on https://apps.gnome.org/Authenticator/ page.

%prep
%autosetup -n %{name_upstream}-%{commit} -p0

mkdir -p migrations/2026-10-10_cern_provider/
cp %{SOURCE10} migrations/2026-10-10_cern_provider/down.sql
cp %{SOURCE11} migrations/2026-10-10_cern_provider/up.sql

tar -xzf %{SOURCE1}

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
* Thu Oct 15 2026 Jan Musinsky <musinsky@gmail.com> - 4.6.2-1
- Initial Authenticator build
