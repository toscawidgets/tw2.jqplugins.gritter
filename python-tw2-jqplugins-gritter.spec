%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global modname tw2.jqplugins.gritter

Name:           python-tw2-jqplugins-gritter
Version:        2.0.0
Release:        1%{?dist}
Summary:        jQuery gritter (growl-like popups) for ToscaWidgets2

Group:          Development/Languages
License:        MIT
URL:            http://toscawidgets.org
Source0:        http://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

# For building
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-simplejson
BuildRequires:  python-tw2-core
BuildRequires:  python-tw2-jquery
BuildRequires:  python-tw2-jqplugins-ui

# Runtime requirements
Requires:       python-tw2-core
Requires:       python-tw2-jquery
Requires:       python-tw2-jqplugins-ui

%description
This module provides growl like popups with the gritter plugin for
python-tw2-jqplugins-ui.

%prep
%setup -q -n %{modname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*

%changelog
* Wed Apr 11 2012 Ralph Bean <rbean@redhat.com> - 2.0.0-1
- Initial packaging for Fedora
