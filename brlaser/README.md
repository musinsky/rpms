brlaser in Fedora
-----------------
**2022-05 brlaser package is now officially in Fedora and EPEL repositories.**
```
$ dnf install printer-driver-brlaser
```

---

**Now brlaser only as source package example (simple and quick compilation)**

[brlaser](https://github.com/pdewacht/brlaser): Brother laser printer driver.

Fedora [brother-brlaser-printer](https://copr.fedorainfracloud.org/coprs/musinsky/brlaser/)
copr package repository (no longer maintained).

### Create SRPM package
```
# download specfile
$ wget https://raw.githubusercontent.com/musinsky/rpms/rawhide/brlaser/brother-brlaser-printer.spec -P $(rpm --eval %{_specdir})

# download sources and patches from specfile
$ rpmdev-spectool --get-files --sourcedir $(rpm --eval %{_specdir})/brother-brlaser-printer.spec

# build SRPM package
$ rpmbuild -bs $(rpm --eval %{_specdir})/brother-brlaser-printer.spec   # -bs (source), -bb (binary), -ba (all)

$ ls $(rpm --eval %{_srcrpmdir})
brother-brlaser-printer-6-3.20200420git9d7ddda.fc42.src.rpm
```
