#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-py_pure_client
Version  : 1.23.0
Release  : 2
URL      : https://github.com/PureStorage-OpenConnect/py-pure-client/archive/1.23.0/py-pure-client-1.23.0.tar.gz
Source0  : https://github.com/PureStorage-OpenConnect/py-pure-client/archive/1.23.0/py-pure-client-1.23.0.tar.gz
Summary  : Pure Storage Python clients for FlashArray, FlashBlade, and Pure1 APIs
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-py_pure_client-license = %{version}-%{release}
Requires: pypi-py_pure_client-python = %{version}-%{release}
Requires: pypi-py_pure_client-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(certifi)
BuildRequires : pypi(paramiko)
BuildRequires : pypi(pyjwt)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi(typing)
BuildRequires : pypi(urllib3)

%description
# Pure Storage Unified Python SDK
## Overview
The `py-pure-client` Python package provides clients that use the Pure1 1.x REST API,
the FlashArray REST 2.x API, and the FlashBlade REST 2.x API.

%package license
Summary: license components for the pypi-py_pure_client package.
Group: Default

%description license
license components for the pypi-py_pure_client package.


%package python
Summary: python components for the pypi-py_pure_client package.
Group: Default
Requires: pypi-py_pure_client-python3 = %{version}-%{release}

%description python
python components for the pypi-py_pure_client package.


%package python3
Summary: python3 components for the pypi-py_pure_client package.
Group: Default
Requires: python3-core
Provides: pypi(py_pure_client)
Requires: pypi(certifi)
Requires: pypi(paramiko)
Requires: pypi(pyjwt)
Requires: pypi(python_dateutil)
Requires: pypi(requests)
Requires: pypi(setuptools)
Requires: pypi(six)
Requires: pypi(typing)
Requires: pypi(urllib3)

%description python3
python3 components for the pypi-py_pure_client package.


%prep
%setup -q -n py-pure-client-1.23.0
cd %{_builddir}/py-pure-client-1.23.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650126050
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-py_pure_client
cp %{_builddir}/py-pure-client-1.23.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-py_pure_client/2b874e6b1e7f063ef687afd4395bdd1263ac700f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-py_pure_client/2b874e6b1e7f063ef687afd4395bdd1263ac700f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
