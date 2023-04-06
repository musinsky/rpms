%if 0%{?fedora} > 35
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name:      hunspell-ru
# Fedora hunspell-ru package with Epoch 1
Epoch:     1
Version:   0.99g5.0.4.5.1
Release:   1%{?dist}
Summary:   Russian dictionary for hunspell

License:   BSD-3
URL:       http://scon155.phys.msu.su/~swan/orthography.html
Source0:   https://addons.mozilla.org/firefox/downloads/file/1163927/russian_spellchecking_dic_3703-0.4.5.1webext.xpi

BuildArch: noarch

BuildRequires: sed
Requires:      hunspell
Supplements:   (hunspell and langpacks-ru)

%description
Russian hunspell dictionaries.

%prep
%setup -c

%build

%global dict_path $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
%install
mkdir -p %{dict_path}
iconv -f KOI8-R -t UTF8 dictionaries/ru.aff --output=%{dict_path}/ru_RU.aff
iconv -f KOI8-R -t UTF8 dictionaries/ru.dic --output=%{dict_path}/ru_RU.dic
sed -i 's/SET KOI8-R/SET UTF-8/' %{dict_path}/ru_RU.aff
touch -r dictionaries/ru.aff %{dict_path}/ru_RU.aff
touch -r dictionaries/ru.dic %{dict_path}/ru_RU.dic

%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Apr 04 2023 Jan Musinsky <musinsky@gmail.com> - 1:0.99g5.0.4.5.1-1
- update to 0.4.5.1 (0.99g5 version)

* Wed Feb 22 2023 Caolán McNamar <caolanm@redhat.com> 1:0.99g5-25
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.99g5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.99g5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 11 2022 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 1:0.99g5-22
- rename install directory name from myspell to hunspell
- https://fedoraproject.org/wiki/Changes/Hunspell_dictionary_dir_change
