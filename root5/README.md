<!-- markdownlint-disable MD033 MD041-->
<p align="right">last edit: 2026-04-17</p>
<!-- markdownlint-enable  MD033 MD041-->

# ROOT 5

- [ROOT Version v5-34-00 Patch Release Notes](https://root.cern.ch/install/all_releases/root-version-v5-34-00-patch-release-notes/)
(between 2012-06 and 2018-03)
- ROOT GitHub [v5-34-00-patches](https://github.com/root-project/root/tree/v5-34-00-patches) branch
- Last ROOT 5: release [5.34.38](https://root.cern.ch/releases/release-53438/) (2018-03-12)
- Last ROOT 5: GitHub [v5-34-00-patches](https://github.com/root-project/root/commits/v5-34-00-patches)
(last commit 2025-09-10)

## GCC standards

- Latest ROOT 5 was compiled by the ROOT team with GCC 4.8, 4.9 or 5.1 and with option `-std=c++11`
(and with GCC default C standard `-std=gnu90` or `-std=gnu11`)
- [GCC 4.8](https://gcc.gnu.org/gcc-4.8/changes.html) (GCC 4.8.0 [released](https://gcc.gnu.org/gcc-4.8/) 2013-03)
or [GCC 4.9](https://gcc.gnu.org/gcc-4.9/changes.html) (GCC 4.9.0 [released](https://gcc.gnu.org/gcc-4.9/) 2014-04)
  - C default standard is `-std=gnu90` (identical as `-std=gnu89`)
  - C++ default standard is `-std=gnu++98`
- [GCC 5](https://gcc.gnu.org/gcc-5/changes.html) (GCC 5.1 [released](https://gcc.gnu.org/gcc-5/) 2015-04)
  - Default standard for C is now `-std=gnu11` (instead of `-std=gnu89/gnu90`)
  - Default standard for C++ is `-std=gnu++98`
- Recommended standards for latest ROOT 5 in the [latest](https://gcc.gnu.org/releases.html) versions of GCC
  - **use `c11` (or `gnu11`) as standard for C**
  - **use `c++11` (or `gnu++11`) as standard for C++**
  - see also [C](https://gcc.gnu.org/projects/c-status.html) and [C++](https://gcc.gnu.org/projects/cxx-status.html)
  standards support in GCC

## ROOT 5 in Fedora

- Last ROOT 5 in Fedora 23: release [5.34.36](https://root.cern.ch/releases/release-53436/) (2016-04-05)
  - [root.spec](https://src.fedoraproject.org/rpms/root/blob/f23/f/root.spec) (2016-04-08) is compiled without any
  modification of `-std=` option, i.e. with default standard `-std=gnu++98` and `-std=gnu11` in GCC 5.3 (released
  2015-12) in Fedora 23
  - [root-5.34.36-1.fc23.src.rpm](https://archives.fedoraproject.org/pub/archive/fedora/linux/updates/23/SRPMS/r/root-5.34.36-1.fc23.src.rpm)
  (2016-04-13)
  - [root-doc-5.34.36-1.fc23.noarch.rpm](https://archives.fedoraproject.org/pub/archive/fedora/linux/updates/23/x86_64/r/root-doc-5.34.36-1.fc23.noarch.rpm)
  (2016-04-13, `ClassIndex.html` last changed/generated 2016-04-10)
- Other software (used by ROOT 5) in Fedora 23
  - glibc 2.22 (released 2015-08)

## Notes

- <https://root.cern.ch/root/html534/ClassIndex.html> (last changed/generated 2015-09-08)
- Option [`--enable-cxx14`](https://github.com/root-project/root/commit/c57b379995525a04558652fdf4c954301a5549c1) added
  in 2014-10 via `-std=c++1y` in GCC, standard `c++14` in GCC 4.9 (released 2014-04) as experimantal via `-std=c++1y`
- If compilation with `--enable-xrootd` is required then latest ROOT 5 with latest GCC need latest XRootD of 4.x series ([v4.12.9](https://github.com/xrootd/xrootd/releases/tag/v4.12.9))
  - OpenSSL 3 (Fedora 36+ and RHEL 9+) and latest XRootD of 4.x series (required OpenSSL 1.x) cannot be compiled without XRootD patching

## ROOT 5 compilation with latest GCC versions

Solved issues 2026-04 (Fedora 43, gcc 15.2): [1](https://github.com/musinsky/rpms/issues/1),
[2](https://github.com/musinsky/rpms/issues/2), [3](https://github.com/musinsky/rpms/issues/3) and
[4](https://github.com/musinsky/rpms/issues/4)

<!-- markdownlint-disable MD014-->
```console
$ cd /cern/
$ git clone --depth 1 --branch=v5-34-00-patches https://github.com/root-project/root.git root_v5-34-00-patches
$ # ln -s root_v5-34-00-patches root            # export ROOTSYS="/cern/root"
$ cd root_v5-34-00-patches
$ curl -O https://raw.githubusercontent.com/musinsky/ROOTHighlight/master/root_v5-34-00-patches/HighlightROOT5.patch
$ git apply HighlightROOT5.patch

$ ./configure --disable-memstat --disable-xrootd --disable-mathmore --disable-tmva --disable-python
$ make

$ export ROOTSYS="$(pwd)"
$ # export ROOTSYS="$(root-config --prefix)"    # if ROOTSYS is not declare (only PATH)
$ make install
```
<!-- markdownlint-enable  MD014-->
