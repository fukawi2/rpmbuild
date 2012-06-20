# Thanks to OpenSUSE Build Service for basis of this spec file
Name:           httpd-mod_macro
BuildRequires:  httpd-devel
%define modname mod_macro
%define apxs /usr/sbin/apxs
#%define apache apache2
%define apache_libexecdir %(%{apxs} -q LIBEXECDIR)
#%define apache_sysconfdir %(%{apxs} -q SYSCONFDIR)
#%define apache_includedir %(%{apxs} -q INCLUDEDIR)
#%define apache_serverroot %(%{apxs} -q PREFIX)
#%define apache_localstatedir %(%{apxs} -q LOCALSTATEDIR)
%define apache_mmn        %(MMN=$(%{apxs} -q LIBEXECDIR)_MMN; test -x $MMN && $MMN)
Version:        1.1.11
Release:        1
Requires:       httpd %{apache_mmn}
Summary:        Define and Use Macros within the Apache Configuration
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Servers
Url:            http://people.apache.org/~fabien/mod_macro/
Source:         http://people.apache.org/~fabien/mod_macro/%{modname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
mod_macro is a third-party module for the Apache HTTP Server.  It is
distributed with a BSD-style license similar to Apache. It allows the
definition and use of macros within Apache runtime configuration files.

To load the module into Apache, run the command "a2enmod macro" as
root.

To learn about the configuration, refer to
/usr/share/doc/packages/apache2-mod_macro/mod_macro.html

%prep
%setup -n %{modname}-%{version}

%build
%{apxs} -c mod_macro.c

%install
mkdir -p $RPM_BUILD_ROOT/%{apache_libexecdir}
cp -p .libs/mod_macro.so $RPM_BUILD_ROOT/%{apache_libexecdir}

%files
%defattr(-,root,root)
%doc README
%doc INSTALL
%doc CHANGES
%doc LICENSE
%doc mod_macro.html
%{apache_libexecdir}/%{modname}.so

%changelog

