Summary: Dibbler - a portable DHCPv6
Name: dibbler
Version: 0.8.1
Release: 1
URL: http://klub.com.pl/dhcpv6/dibbler
Source: dibbler-0.8.1.tar.gz
License: GPL
Group: System/Servers
Source1: dibbler-client
Source2: dibbler-server
BuildRequires:  tetex-latex
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
It supports both stateful (i.e. IPv6 address granting) and stateless 
(i.e. options granting) autoconfiguration modes of DHCPv6 protocol. 
There are ports available for Linux 2.4/2.6 systems as well as MS 
Windows XP,2003 (experimental support for NT4 and 2000). 
They are freely available under GNU GPL v2 or later license. 

Install Dibbler if you'd like to have IPv6 hosts automatically 
configured in your network. All infrastructure elements are
provided: server, client and relay.

%prep
%setup

%build
./configure --prefix=/usr
make all

%install
#rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -m 755 dibbler-server $RPM_BUILD_ROOT/usr/sbin/
install -m 755 dibbler-client $RPM_BUILD_ROOT/usr/sbin/
install -m 755 dibbler-relay  $RPM_BUILD_ROOT/usr/sbin/
#mkdir -p $RPM_BUILD_ROOT/usr/share/doc/dibbler
#%{__install} -m 644 doc/dibbler-user.pdf $RPM_BUILD_ROOT/usr/share/doc/dibbler
#%{__install} -m 644 doc/dibbler-devel.pdf $RPM_BUILD_ROOT/usr/share/doc/dibbler
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man8
install -m 644 doc/man/dibbler-client.8 $RPM_BUILD_ROOT/usr/share/man/man8
install -m 644 doc/man/dibbler-server.8 $RPM_BUILD_ROOT/usr/share/man/man8
install -m 644 doc/man/dibbler-relay.8  $RPM_BUILD_ROOT/usr/share/man/man8
mkdir -p $RPM_BUILD_ROOT/etc/dibbler
mkdir -p $RPM_BUILD_ROOT/var/lib/dibbler/
mkdir -p $RPM_BUILD_ROOT/etc/init.d/

install -m 644 doc/examples/client.conf $RPM_BUILD_ROOT/etc/dibbler
install -m 644 doc/examples/client-stateless.conf $RPM_BUILD_ROOT/etc/dibbler
install -m 644 doc/examples/server.conf $RPM_BUILD_ROOT/etc/dibbler
install -m 644 doc/examples/server-stateless.conf $RPM_BUILD_ROOT/etc/dibbler
install -m 644 doc/examples/relay.conf $RPM_BUILD_ROOT/etc/dibbler
install -m 700 %{SOURCE1} %{buildroot}/etc/init.d/
install -m 700 %{SOURCE2} %{buildroot}/etc/init.d/

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG LICENSE RELNOTES doc/dibbler-user.pdf
/usr/sbin/dibbler-server
/usr/sbin/dibbler-client
/usr/sbin/dibbler-relay
/usr/share/man/man8/*
/var/lib/dibbler/
/etc/dibbler/client.conf
/etc/dibbler/client-stateless.conf
/etc/dibbler/server.conf
/etc/dibbler/server-stateless.conf
/etc/dibbler/relay.conf
/etc/init.d/*


%changelog
* Thu Oct 22 2009 Vincent Guardiola <vguardiola@mandriva.com> 0.7.3-2mdv2010.0
+ Revision: 458897
- Add initscript Client and Sever

* Tue Oct 20 2009 Anne Nicolas <anne.nicolas@mandriva.com> 0.7.3-1mdv2010.0
+ Revision: 458431
- add build require (V.Guardiola)
- import dibbler

