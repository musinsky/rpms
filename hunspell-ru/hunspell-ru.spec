%if 0%{?fedora} > 35
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
%global dict_path $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

Name:      hunspell-ru
Summary:   Russian dictionaries for hunspell
Epoch:     1   # Fedora hunspell-ru package with Epoch 1
Version:   2025.05.15
Release:   1%{?dist}

License:   BSD-2 or MPL-2.0 or LGPL-3.0
URL:       https://addons.mozilla.org/en-US/firefox/language-tools/

# more info on https://muke.saske.sk/wiki/Spelling#Russian
# src0     Firefox Russian spellchecking dictionary by Alexander Slovesnik
Source0:   https://addons.mozilla.org/firefox/downloads/file/4270210/russian_spellchecking_dic_3703-0.4.5.2resigned1.xpi
# src      Firefox Russian Hunspell dictionary by Aleksandr Klyukvin
Source1:   https://addons.mozilla.org/firefox/downloads/file/4270388/russian_hunspell_dictionary-1.0.20131101.3resigned1.xpi
# src2     Firefox Slovar orfografii Wiki by Kek
Source2:   https://addons.mozilla.org/firefox/downloads/file/4479738/2696307-1.109.xpi

BuildArch: noarch

BuildRequires: unzip sed dos2unix
Requires:      hunspell
Supplements:   (hunspell and langpacks-ru)

%description
Russian hunspell multi dictionaries.

%prep
# https://ftp.osuosl.org/pub/rpm/max-rpm/s1-rpm-inside-macros.html#S3-RPM-INSIDE-SETUP-MULTI-SOURCE
# correct solution in this case would be to create multiple RPMs
%setup -c -T
mkdir src0 && cd src0 && unzip %{S:0}
mkdir ../src1 && cd ../src1 && unzip %{S:1}
mkdir ../src2 && cd ../src2 && unzip %{S:2}
cd ..

%build

%install
mkdir -p %{dict_path}

# src0
iconv -f KOI8-R -t UTF8 src0/dictionaries/ru.aff --output=%{dict_path}/ru_RU-0.aff
iconv -f KOI8-R -t UTF8 src0/dictionaries/ru.dic --output=%{dict_path}/ru_RU-0.dic
sed -i 's/SET KOI8-R/SET UTF-8/' %{dict_path}/ru_RU-0.aff
sed -i '1 i \# Firefox Russian spellchecking dictionary by Alexander Slovesnik' \
    %{dict_path}/ru_RU-0.aff
sed -i '2 i \# ver 0.4.5.2resigned1 (released 2024-04-25, dictionary from 2013-06-29)\n' \
    %{dict_path}/ru_RU-0.aff
touch -md "2013-06-29" %{dict_path}/ru_RU-0.aff
touch -md "2013-06-29" %{dict_path}/ru_RU-0.dic

# src1
dos2unix src1/dictionaries/ru_RU.aff
dos2unix src1/dictionaries/ru_RU.dic
cp src1/dictionaries/ru_RU.aff %{dict_path}/ru_RU-1.aff
cp src1/dictionaries/ru_RU.dic %{dict_path}/ru_RU-1.dic
sed -i '1 i \# Firefox Russian Hunspell dictionary by Aleksandr Klyukvin' \
    %{dict_path}/ru_RU-1.aff
sed -i '2 i \# ver 1.0.20131101.3resigned1 (released 2024-04-25, dictionary from 2013-11-01)\n' \
    %{dict_path}/ru_RU-1.aff
touch -md "2013-11-01" %{dict_path}/ru_RU-1.aff
touch -md "2013-11-01" %{dict_path}/ru_RU-1.dic

# src2
cp src2/dictionaries/ru_RU.aff %{dict_path}/ru_RU-2.aff
cp src2/dictionaries/ru_RU.dic %{dict_path}/ru_RU-2.dic
sed -i '1 i \# Firefox Slovar orfografii Wiki by Kek' %{dict_path}/ru_RU-2.aff
sed -i '2 i \# ver 1.109 (released 2025-04-23)\n' %{dict_path}/ru_RU-2.aff
# wrong DateTime in packed Firefox extension
touch -md "2025-04-23" %{dict_path}/ru_RU-2.aff
touch -md "2025-04-23" %{dict_path}/ru_RU-2.dic

%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Thu May 15 2025 Jan Musinsky <musinsky@gmail.com> - 1:2025.05.15-1
- release 2025.05.15-1
