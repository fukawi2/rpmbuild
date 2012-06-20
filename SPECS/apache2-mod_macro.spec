Summary: Allows the definition and use of macros within apache.
Name: apache2-mod_macro
Version: 1.1.11
Release: 1
URL: http://cri.ensmp.fr/~coelho/mod_macro/
Source: http://cri.ensmp.fr/~coelho/mod_macro/mod_macro-1.1.11.tar.gz
License: Custom
Group: System/Servers
Source1:	macro.conf
BuildRequires:  httpd-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
mod_macro is a third-party module to the Apache Http Server, distributed with a BSD-style license like Apache. 
It allows the definition and use of macros (configuration templates) within apache runtime configuration files. 
The syntax is a natural extension to apache html-like configuration style.

#%prep
#%setup

%build
cd mod_macro-1.1.11/
apxs -c mod_macro.c

%install
cd mod_macro-1.1.11/

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/httpd/modules/
%{__install} -m 755 mod_macro.o $RPM_BUILD_ROOT/%{_libdir}/httpd/modules/mod_macro.so

mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf.d/
%{__install} -m 644 %{SOURCE1} %{buildroot}/etc/httpd/conf.d/

mkdir -p $RPM_BUILD_ROOT/$RPM_DOC_DIR/$RPM_PACKAGE_NAME-$RPM_PACKAGE_VERSION/
%{__install} -m 644 CHANGES $RPM_BUILD_ROOT/$RPM_DOC_DIR/$RPM_PACKAGE_NAME-$RPM_PACKAGE_VERSION/
%{__install} -m 644 README $RPM_BUILD_ROOT/$RPM_DOC_DIR/$RPM_PACKAGE_NAME-$RPM_PACKAGE_VERSION/
%{__install} -m 644 LICENSE $RPM_BUILD_ROOT/$RPM_DOC_DIR/$RPM_PACKAGE_NAME-$RPM_PACKAGE_VERSION/
%{__install} -m 644 mod_macro.html $RPM_BUILD_ROOT/$RPM_DOC_DIR/$RPM_PACKAGE_NAME-$RPM_PACKAGE_VERSION/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc mod_macro-1.1.11/CHANGES mod_macro-1.1.11/LICENSE mod_macro-1.1.11/README mod_macro-1.1.11/mod_macro.html
/etc/httpd/conf.d/macro.conf
%{_libdir}/httpd/modules/mod_macro.so
/usr/share/doc/apache2-mod_macro-1.1.11/CHANGES
/usr/share/doc/apache2-mod_macro-1.1.11/LICENSE
/usr/share/doc/apache2-mod_macro-1.1.11/README
/usr/share/doc/apache2-mod_macro-1.1.11/mod_macro.html


%changelog
