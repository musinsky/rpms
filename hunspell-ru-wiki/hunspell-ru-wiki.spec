%if 0%{?fedora} > 35 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
%global dict_path %{buildroot}%{_datadir}/%{dict_dirname}

Name:      hunspell-ru-wiki
Version:   1.120
Release:   1
BuildArch: noarch
License:   MPL 2.0
URL:       https://addons.mozilla.org/firefox/addon/2938464/
Summary:   Russian dictionary (wiktionary) for hunspell

# hunspell-ru-wiki-1.120-1
%global date 2026-04-03
Source0:   https://addons.mozilla.org/firefox/downloads/file/4750542/2938464-%{version}.xpi

BuildRequires: unzip
Requires:      hunspell
Supplements:   (hunspell and langpacks-ru)

%description
Russian dictionary (wiktionary) for hunspell.

This package add dictionary from Firefox extension
'Slovar russkoj orfografii iz Vikislovarya (yo = ye) by Kek'

%prep
# -c => create the build directory (and change to it) before unpacking
%setup -c

echo $(pwd)

%build

%install
mkdir -p %{dict_path}
cp dictionaries/ru_RU.aff %{dict_path}/ru_RU-wiki.aff
cp dictionaries/ru_RU.dic %{dict_path}/ru_RU-wiki.dic
sed -i '1 i \# Firefox Slovar russkoj orfografii iz Vikislovarya (yo = ye) by Kek' \
    %{dict_path}/ru_RU-wiki.aff
sed -i '2 i \# Version %{version} (released %{date})\n' \
    %{dict_path}/ru_RU-wiki.aff
touch -md "%{date}" %{dict_path}/ru_RU-wiki.aff
touch -md "%{date}" %{dict_path}/ru_RU-wiki.dic

# %%clean
# clean in modern rpm (rpmbuild 4.6+) is deprecated

%check

%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Wed Apr 22 2026 Jan Musinsky <musinsky@gmail.com> - 1.120-1
- Initial hunspell-ru-wiki build
