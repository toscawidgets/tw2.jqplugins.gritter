%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global modname tw2.jqplugins.gritter

Name:           python-tw2-jqplugins-gritter
Version:        2.0.1
Release:        1%{?dist}
Summary:        jQuery gritter (growl-like pop-ups) for ToscaWidgets2

Group:          Development/Languages
License:        MIT
URL:            http://toscawidgets.org
Source0:        http://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
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
This module provides growl like pop-ups with the gritter plugin for
python-tw2-jqplugins-ui.

%prep
%setup -q -n %{modname}-%{version}

%if %{?rhel}%{!?rhel:0} >= 6

# Make sure that epel/rhel picks up the correct version of webob
awk 'NR==1{print "import __main__; __main__.__requires__ = __requires__ = [\"WebOb>=1.0\"]; import pkg_resources"}1' setup.py > setup.py.tmp
mv setup.py.tmp setup.py

# Remove all the fancy nosetests configuration for older python
rm setup.cfg

%endif


%build
%{__python} setup.py build
# This is a hack to get the jqplugins to not stomp all over each others
# namespace declarations.
rm -f build/lib/tw2/jqplugins/__init__.py*

%install
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%files
%doc README.rst LICENSE
%{python_sitelib}/*

%changelog
* Wed May 02 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-1
- Upstream release, includes the LICENSE

* Wed Apr 11 2012 Ralph Bean <rbean@redhat.com> - 2.0.0-1
- Initial packaging for Fedora
