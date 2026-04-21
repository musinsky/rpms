<!-- markdownlint-disable MD033 MD041-->
<p align="right">last edit: 2026-04-22</p>
<!-- markdownlint-enable  MD033 MD041-->

# Fedora Package Sources

Personal repository for package maintenance.

## Create SRPM packages

* replace outdated Fedora [hunspell-sk](https://src.fedoraproject.org/rpms/hunspell-sk/blob/rawhide/f/hunspell-sk.spec)
  and [hunspell-ru](https://src.fedoraproject.org/rpms/hunspell-ru/blob/rawhide/f/hunspell-ru.spec) dictionaries

```console
curl https://raw.githubusercontent.com/musinsky/rpms/rawhide/hunspell-sk/hunspell-sk.create.SRPM.package.sh | bash
curl https://raw.githubusercontent.com/musinsky/rpms/rawhide/hunspell-ru/hunspell-ru.create.SRPM.package.sh | bash
```

* add [hunspell-ru-wiki](https://addons.mozilla.org/firefox/addon/2938464/) dictionary

```console
curl https://raw.githubusercontent.com/musinsky/rpms/rawhide/hunspell-ru-wiki/hunspell-ru-wiki.create.SRPM.package.sh | bash
```

* add legacy ROOT 5 (branch [v5-34-00-patches](https://github.com/root-project/root/commits/v5-34-00-patches)), works
  correctly together with Fedora version of [root](https://src.fedoraproject.org/rpms/root/blob/rawhide/f/root.spec)

```console
curl https://raw.githubusercontent.com/musinsky/rpms/rawhide/root5/root5.create.SRPM.package.sh | bash
```
