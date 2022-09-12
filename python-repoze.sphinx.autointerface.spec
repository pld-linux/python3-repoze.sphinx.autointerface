#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension: auto-generate API docs from Zope interfaces
Summary(pl.UTF-8):	Rozszerzenie Sphinksa: automatyczne generowanie dokumentacji API z interfejsów Zope
Name:		python-repoze.sphinx.autointerface
# keep 0.x here for python2 support
Version:	0.8
Release:	6
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/repoze-sphinx-autointerface/
Source0:	https://files.pythonhosted.org/packages/source/r/repoze.sphinx.autointerface/repoze.sphinx.autointerface-%{version}.tar.gz
# Source0-md5:	8e05cb8421b0a3bea8ec3b0aa3695310
URL:		https://pypi.org/project/repoze.sphinx.autointerface/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package defines an extension for the Sphinx documentation system.
The extension allows generation of API documentation by introspection
of zope.interface instances in code.

%description -l pl.UTF-8
Ten pakiet definiuje rozszerzenie systemu dokumentacji Sphinx,
pozwalające generować dokumentację API poprzez wgląd w instancje
zope.interface w kodzie.

%package -n python3-repoze.sphinx.autointerface
Summary:	Sphinx extension: auto-generate API docs from Zope interfaces
Summary(pl.UTF-8):	Rozszerzenie Sphinksa: automatyczne generowanie dokumentacji API z interfejsów Zope
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-repoze.sphinx.autointerface
This package defines an extension for the Sphinx documentation system.
The extension allows generation of API documentation by introspection
of zope.interface instances in code.

%description -n python3-repoze.sphinx.autointerface -l pl.UTF-8
Ten pakiet definiuje rozszerzenie systemu dokumentacji Sphinx,
pozwalające generować dokumentację API poprzez wgląd w instancje
zope.interface w kodzie.

%prep
%setup -q -n repoze.sphinx.autointerface-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst CONTRIBUTORS.txt COPYRIGHT.txt LICENSE.txt README.rst TODO.txt
# XXX: shared dir
%dir %{py_sitescriptdir}/repoze
%dir %{py_sitescriptdir}/repoze/sphinx
%{py_sitescriptdir}/repoze/sphinx/autointerface.py[co]
%{py_sitescriptdir}/repoze.sphinx.autointerface-%{version}-py*.egg-info
%{py_sitescriptdir}/repoze.sphinx.autointerface-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-repoze.sphinx.autointerface
%defattr(644,root,root,755)
%doc CHANGES.rst CONTRIBUTORS.txt COPYRIGHT.txt LICENSE.txt README.rst TODO.txt
%dir %{py3_sitescriptdir}/repoze
%dir %{py3_sitescriptdir}/repoze/sphinx
%{py3_sitescriptdir}/repoze/sphinx/autointerface.py
%{py3_sitescriptdir}/repoze/sphinx/__pycache__
%{py3_sitescriptdir}/repoze.sphinx.autointerface-%{version}-py*.egg-info
%{py3_sitescriptdir}/repoze.sphinx.autointerface-%{version}-py*-nspkg.pth
%endif
