<!-- markdownlint-disable MD033 MD041-->
<p align="right">last edit: 2026-04-10</p>
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

- Recommended standards for latest ROOT 5 (see also [C](https://gcc.gnu.org/projects/c-status.html) and
  [C++](https://gcc.gnu.org/projects/cxx-status.html) standards support in GCC)
  - use `c11` (or `gnu11`) as standard for C
  - use `c++11` (or `gnu++11`) as standard for C++

---

- <https://root.cern.ch/root/html534/ClassIndex.html> (last changed/generated 2015-09-08)
- option [`--enable-cxx14`](https://github.com/root-project/root/commit/c57b379995525a04558652fdf4c954301a5549c1) added
  in 2014-10 via `-std=c++1y` in GCC, standard `c++14` in GCC 4.9 (released 2014-04) as experimantal via `-std=c++1y`
