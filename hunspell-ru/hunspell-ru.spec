%if 0%{?fedora} > 35 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
%global dict_path %{buildroot}%{_datadir}/%{dict_dirname}

# https://src.fedoraproject.org/rpms/hunspell-ru/blob/rawhide/f/hunspell-ru.spec
# Fedora hunspell-ru package with Epoch: 1 (Epoch > Version > Release)
Name:      hunspell-ru
Epoch:     2
Version:   2013
# always increment release number (hunspell-ru-2013-1)
Release:   1
BuildArch: noarch
License:   BSD 2 and LGPL 3.0
URL:       https://addons.mozilla.org/firefox/language-tools/
Summary:   Russian dictionaries for hunspell

# https://addons.mozilla.org/firefox/addon/russian-spellchecking-dic-3703/
# src10 = Russian spellchecking dictionary by Alexander Slovesnik
Source10:  https://addons.mozilla.org/firefox/downloads/file/4270210/russian_spellchecking_dic_3703-0.4.5.2resigned1.xpi
%global dict10_name ru_RU-10
#
# https://addons.mozilla.org/firefox/addon/russian-hunspell-dictionary/
# src20 = Russian Hunspell dictionary by Aleksandr Klyukvin
Source20:  https://addons.mozilla.org/firefox/downloads/file/4270388/russian_hunspell_dictionary-1.0.20131101.3resigned1.xpi
%global dict20_name ru_RU-20

BuildRequires: unzip dos2unix
Requires:      hunspell
Supplements:   (hunspell and langpacks-ru)

%description
Russian dictionaries for hunspell.

This package replaces the default package in Fedora, which uses an outdated
dictionary.

%prep
# https://ftp.osuosl.org/pub/rpm/max-rpm/s1-rpm-inside-macros.html#S3-RPM-INSIDE-SETUP-MULTI-SOURCE
# correct solution in this case would be to create multiple RPMs
%dnl %setup -c -T   # pwd = $HOME/rpmbuild/BUILD/hunspell-ru-2013-build/hunspell-ru-2013
%dnl no %setup      # pwd = $HOME/rpmbuild/BUILD/hunspell-ru-2013-build
mkdir    src10 && cd    src10 && unzip %{SOURCE10}
mkdir ../src20 && cd ../src20 && unzip %{SOURCE20}
cd ..

echo $(pwd)

%build

%install
mkdir -p %{dict_path}

# src10
iconv -f KOI8-R -t UTF8 src10/dictionaries/ru.aff --output=%{dict_path}/%{dict10_name}.aff
iconv -f KOI8-R -t UTF8 src10/dictionaries/ru.dic --output=%{dict_path}/%{dict10_name}.dic
sed -i 's/SET KOI8-R/SET UTF-8/' %{dict_path}/%{dict10_name}.aff
sed -i '1 i \# Firefox Russian spellchecking dictionary by Alexander Slovesnik' \
    %{dict_path}/%{dict10_name}.aff
sed -i '2 i \# Dictionary from 2013-06-29 (based on Lebedev 0.99g5 dictionary)\n' \
    %{dict_path}/%{dict10_name}.aff
touch -md "2013-06-29" %{dict_path}/%{dict10_name}.aff
touch -md "2013-06-29" %{dict_path}/%{dict10_name}.dic

# src20
dos2unix -n src20/dictionaries/ru_RU.aff %{dict_path}/%{dict20_name}.aff
dos2unix -n src20/dictionaries/ru_RU.dic %{dict_path}/%{dict20_name}.dic
sed -i '1 i \# Firefox Russian Hunspell dictionary by Aleksandr Klyukvin' \
    %{dict_path}/%{dict20_name}.aff
sed -i '2 i \# Dictionary from 2013-11-01 (extended dictionary of Lebedev)\n' \
    %{dict_path}/%{dict20_name}.aff
touch -md "2013-11-01" %{dict_path}/%{dict20_name}.aff
touch -md "2013-11-01" %{dict_path}/%{dict20_name}.dic

# %%clean
# clean in modern rpm (rpmbuild 4.6+) is deprecated

%check

%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Apr 21 2026 Jan Musinsky <musinsky@gmail.com> - 2:2013-1
- Initial hunspell-ru build
