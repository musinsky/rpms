brlaser in Fedora
-----------------
**2022-05 brlaser package is now officially in Fedora and EPEL repositories.**
```
$ dnf install printer-driver-brlaser
```

---

**Now brlaser only as source package example (simple and quick compilation)**

[brlaser](https://github.com/pdewacht/brlaser): Brother laser printer driver.

[brother-brlaser-printer](https://copr.fedorainfracloud.org/coprs/musinsky/brlaser/)
package repository for Fedora (or CentOS).

### Create SRPM
```
$ wget https://raw.githubusercontent.com/musinsky/rpms/rawhide/brlaser/brother-brlaser-printer.spec -P $(rpm --eval %{_specdir})
$ rpmdev-spectool -g -R $(rpm --eval %{_specdir})/brother-brlaser-printer.spec
# add patches
$ wget https://raw.githubusercontent.com/musinsky/rpms/rawhide/brlaser/patch-20210908.patch -P $(rpm --eval %{_sourcedir})
$ wget https://raw.githubusercontent.com/musinsky/rpms/rawhide/brlaser/tempfile.h.patch -P $(rpm --eval %{_sourcedir})
$ rpmbuild -bs $(rpm --eval %{_specdir})/brother-brlaser-printer.spec   # -bs, -bb, -ba
$ ls $(rpm --eval %{_srcrpmdir})
brother-brlaser-printer-6-3.20200420git9d7ddda.fc42.src.rpm
```
