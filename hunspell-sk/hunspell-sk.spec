%if 0%{?fedora} > 35 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

%global forgeurl https://github.com/sk-spell/hunspell-sk
%global commit   864a08dcb5b861b98bbbebaa8f6311f3f1e654f8
%global date     20251001
%forgemeta -i

# https://src.fedoraproject.org/rpms/hunspell-sk/blob/rawhide/f/hunspell-sk.spec
# Fedora hunspell-sk package with Epoch: 1 (Epoch > Version > Release)
Name:      hunspell-sk
Epoch:     2
Version:   %{date}
# always increment release number (hunspell-sk-20251001-1)
Release:   1
BuildArch: noarch
License:   MPL 2.0
URL:       https://www.sk-spell.sk.cx/
Summary:   Slovak dictionaries for hunspell

Source0:   %{forgesource}
Source1:   https://addons.mozilla.org/firefox/downloads/file/4046244/sk_sk_ascii_spellchecking-2.4.7.xpi

BuildRequires: unzip
Requires:      hunspell
Supplements:   (hunspell and langpacks-sk)

%description
Slovak dictionaries for hunspell.

This package replaces the default package in Fedora, which uses an outdated
dictionary and adds an ASCII dictionary.

%prep
# forgesetup = uncompress SOURCE0, cd {topdir} (same as {extractdir}), chmod
%forgesetup -v
# unzip to the same directory as SOURCE0 dir
unzip %{SOURCE1}
# rpmuncompress (unzip) to the parent dir of SOURCE0 dir
%dnl %setup -b 1 -n %{builddir}/%{topdir}

echo $(pwd)
echo %{builddir}/%{topdir}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
cp -p sk_SK.aff sk_SK.dic %{buildroot}%{_datadir}/%{dict_dirname}
# Firefox dictionaries packs (*.xpi) with wrong timestamp
cp -p dictionaries/sk-SK-ascii.aff %{buildroot}%{_datadir}/%{dict_dirname}/sk_SK-ascii.aff
cp -p dictionaries/sk-SK-ascii.dic %{buildroot}%{_datadir}/%{dict_dirname}/sk_SK-ascii.dic

# %%clean
# clean in modern rpm (rpmbuild 4.6+) is deprecated

%check

%files
%dnl %doc doc/*
%{_datadir}/%{dict_dirname}/*

# rpmspec --parse $HOME/rpmbuild/SPECS/hunspell-sk.spec
# rpmlint         $HOME/rpmbuild/SPECS/hunspell-sk.spec
# rpmbuild -bb --noclean $HOME/rpmbuild/SPECS/hunspell-sk.spec

%changelog
* Tue Apr 21 2026 Jan Musinsky <musinsky@gmail.com> - 2:20251001-1
- Initial hunspell-sk build
