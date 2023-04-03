%if 0%{?fedora} > 35
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

%global forgeurl   https://github.com/sk-spell/hunspell-sk
%global commit     d4f4383564caeb1ce58dc4c5bf08d939d34797ba
%global date       20230226
%forgemeta

Name:      hunspell-sk
# Fedora hunspell-sk package with Epoch 1
Epoch:     1
Version:   2.4.7
Release:   1%{?dist}
Summary:   Slovak dictionary for hunspell

License:   MPL-2.0
URL:       http://www.sk-spell.sk.cx/
Source0:   %{forgesource}
Source1:   https://addons.mozilla.org/firefox/downloads/file/4046244/sk_sk_ascii_spellchecking-2.4.7.xpi

BuildArch: noarch

BuildRequires: unzip
Requires:      hunspell
Supplements:   (hunspell and langpacks-sk)

%description
Slovak hunspell dictionaries.

%prep
%forgesetup
# temporary solution for ascii dict
# %setup -a 1
unzip $RPM_SOURCE_DIR/sk_sk_ascii_spellchecking-2.4.7.xpi

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p sk_SK.aff sk_SK.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/sk-SK-ascii.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sk_SK-ascii.aff
cp -p dictionaries/sk-SK-ascii.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sk_SK-ascii.dic

%files
%doc doc/*
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Apr 04 2023 Jan Musinsky <musinsky@gmail.com> - 1:2.4.7-1
- update snapshot to d4f4383 (2.4.7 version)

* Thu Feb 23 2023 Caolán McNamara <caolanm@redhat.com> - 1:0.20110228-24
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.20110228-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.20110228-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 11 2022 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 1:0.20110228-21
- rename install directory name from myspell to hunspell
- https://fedoraproject.org/wiki/Changes/Hunspell_dictionary_dir_change
