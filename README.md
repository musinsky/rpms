<!-- markdownlint-disable MD033 MD041-->
<p align="right">last edit: 2026-04-22</p>
<!-- markdownlint-enable  MD033 MD041-->

# Fedora Package Sources

Personal repository for package maintenance.

## Create SRPM packages

* replace outdated Fedora [hunspell-sk](https://src.fedoraproject.org/rpms/hunspell-sk/blob/rawhide/f/hunspell-sk.spec)
  dictionary  
  [![Copr build status](https://copr.fedorainfracloud.org/coprs/musinsky/rpm/package/hunspell-sk/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/musinsky/rpm/package/hunspell-sk/)

```console
curl https://raw.githubusercontent.com/musinsky/rpms/rawhide/hunspell-sk/hunspell-sk.create.SRPM.package.sh | bash
```

* replace outdated Fedora [hunspell-ru](https://src.fedoraproject.org/rpms/hunspell-ru/blob/rawhide/f/hunspell-ru.spec)
  dictionary  
  [![Copr build status](https://copr.fedorainfracloud.org/coprs/musinsky/rpm/package/hunspell-ru/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/musinsky/rpm/package/hunspell-ru/)

```console
curl https://raw.githubusercontent.com/musinsky/rpms/rawhide/hunspell-ru/hunspell-ru.create.SRPM.package.sh | bash
```

* add new [hunspell-ru-wiki](https://addons.mozilla.org/firefox/addon/2938464/) dictionary  
  [![Copr build status](https://copr.fedorainfracloud.org/coprs/musinsky/rpm/package/hunspell-ru-wiki/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/musinsky/rpm/package/hunspell-ru-wiki/)

```console
curl https://raw.githubusercontent.com/musinsky/rpms/rawhide/hunspell-ru-wiki/hunspell-ru-wiki.create.SRPM.package.sh | bash
```

* add legacy ROOT 5 (branch [v5-34-00-patches](https://github.com/root-project/root/commits/v5-34-00-patches)), works
  correctly together with Fedora version of [root](https://src.fedoraproject.org/rpms/root/blob/rawhide/f/root.spec)  
  [![Copr build status](https://copr.fedorainfracloud.org/coprs/musinsky/rpm/package/root5/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/musinsky/rpm/package/root5/)

```console
curl https://raw.githubusercontent.com/musinsky/rpms/rawhide/root5/root5.create.SRPM.package.sh | bash
```
