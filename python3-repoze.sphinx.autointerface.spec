#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Sphinx extension: auto-generate API docs from Zope interfaces
Summary(pl.UTF-8):	Rozszerzenie Sphinksa: automatyczne generowanie dokumentacji API z interfejsów Zope
Name:		python3-repoze.sphinx.autointerface
Version:	1.0.0
Release:	1
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/repoze-sphinx-autointerface/
Source0:	https://files.pythonhosted.org/packages/source/r/repoze.sphinx.autointerface/repoze.sphinx.autointerface-%{version}.tar.gz
# Source0-md5:	63471c93810215ac7ad02b966ad16c39
URL:		https://pypi.org/project/repoze.sphinx.autointerface/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 4.0
BuildRequires:	python3-zope.interface
BuildRequires:	python3-zope.testrunner
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
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

%prep
%setup -q -n repoze.sphinx.autointerface-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
zope-testrunner-3 --test-path .
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/repoze/sphinx/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst CONTRIBUTORS.txt COPYRIGHT.txt LICENSE.txt README.rst TODO.txt
# XXX: dir shared with repoze.*
%dir %{py3_sitescriptdir}/repoze
%dir %{py3_sitescriptdir}/repoze/sphinx
%{py3_sitescriptdir}/repoze/sphinx/autointerface.py
%{py3_sitescriptdir}/repoze/sphinx/__pycache__
%{py3_sitescriptdir}/repoze.sphinx.autointerface-%{version}-py*.egg-info
%{py3_sitescriptdir}/repoze.sphinx.autointerface-%{version}-py*-nspkg.pth
