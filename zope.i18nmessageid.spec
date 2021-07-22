#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.i18nmessageid
Version  : 5.0.1
Release  : 38
URL      : https://files.pythonhosted.org/packages/fb/13/88454ff27740d9be8140a7be208b09114be79d99c732f058f4b01a684590/zope.i18nmessageid-5.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/fb/13/88454ff27740d9be8140a7be208b09114be79d99c732f058f4b01a684590/zope.i18nmessageid-5.0.1.tar.gz
Summary  : Message Identifiers for internationalization
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.i18nmessageid-license = %{version}-%{release}
Requires: zope.i18nmessageid-python = %{version}-%{release}
Requires: zope.i18nmessageid-python3 = %{version}-%{release}
Requires: setuptools
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : coverage-python
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.exceptions-python
BuildRequires : zope.testrunner-python

%description
``zope.i18nmessageid``
======================
.. image:: https://img.shields.io/pypi/v/zope.i18nmessageid.svg
:target: https://pypi.python.org/pypi/zope.i18nmessageid/
:alt: Latest Version

%package license
Summary: license components for the zope.i18nmessageid package.
Group: Default

%description license
license components for the zope.i18nmessageid package.


%package python
Summary: python components for the zope.i18nmessageid package.
Group: Default
Requires: zope.i18nmessageid-python3 = %{version}-%{release}

%description python
python components for the zope.i18nmessageid package.


%package python3
Summary: python3 components for the zope.i18nmessageid package.
Group: Default
Requires: python3-core
Provides: pypi(zope.i18nmessageid)
Requires: pypi(setuptools)
Requires: pypi(six)

%description python3
python3 components for the zope.i18nmessageid package.


%prep
%setup -q -n zope.i18nmessageid-5.0.1
cd %{_builddir}/zope.i18nmessageid-5.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583876093
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.i18nmessageid
cp %{_builddir}/zope.i18nmessageid-5.0.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.i18nmessageid/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.i18nmessageid/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
