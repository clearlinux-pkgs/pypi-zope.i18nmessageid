#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-zope.i18nmessageid
Version  : 6.0.1
Release  : 61
URL      : https://files.pythonhosted.org/packages/67/0a/2f7ef863b4a19b01c87558edea49d155908f3588d02e3269bbf3b42164b1/zope.i18nmessageid-6.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/67/0a/2f7ef863b4a19b01c87558edea49d155908f3588d02e3269bbf3b42164b1/zope.i18nmessageid-6.0.1.tar.gz
Summary  : Message Identifiers for internationalization
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.i18nmessageid-license = %{version}-%{release}
Requires: pypi-zope.i18nmessageid-python = %{version}-%{release}
Requires: pypi-zope.i18nmessageid-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(coverage)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(zope.testrunner)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
``zope.i18nmessageid``
======================
.. image:: https://img.shields.io/pypi/v/zope.i18nmessageid.svg
:target: https://pypi.python.org/pypi/zope.i18nmessageid/
:alt: Latest Version

%package license
Summary: license components for the pypi-zope.i18nmessageid package.
Group: Default

%description license
license components for the pypi-zope.i18nmessageid package.


%package python
Summary: python components for the pypi-zope.i18nmessageid package.
Group: Default
Requires: pypi-zope.i18nmessageid-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.i18nmessageid package.


%package python3
Summary: python3 components for the pypi-zope.i18nmessageid package.
Group: Default
Requires: python3-core
Provides: pypi(zope.i18nmessageid)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-zope.i18nmessageid package.


%prep
%setup -q -n zope.i18nmessageid-6.0.1
cd %{_builddir}/zope.i18nmessageid-6.0.1
pushd ..
cp -a zope.i18nmessageid-6.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685545720
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.i18nmessageid
cp %{_builddir}/zope.i18nmessageid-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zope.i18nmessageid/a0b53f43aab58b46bf79ba756c50771c605ab4c5 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.i18nmessageid/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
