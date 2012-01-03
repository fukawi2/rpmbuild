Name:		husk
Version:	0.9.5
Release:	2
Summary:	Natural language wrapper around the Linux iptables packet filtering engine
Source0:	http://download.sourceforge.net/husk/husk-0.9.5.tar.gz
License:	GPL
Group:		MyJunk
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	perl(Config::IniFiles) perl(Config::Simple) perl(Getopt::Long)

%description
husk is a natural language wrapper around the Linux iptables packet filtering
engine (iptables). It is designed to abstract the sometimes confusing syntax
of iptables, allowing use of rules that have better readability, and expressed
in a more 'freeform' fashion compared to normal 'raw' iptables rules. husk can
be used on either firewall/router computers (with multiple network interfaces),
or standalone systems (with one network interface)

%prep
%setup

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -m 0755 -d %{buildroot}%{_bindir}/
mv $RPM_BUILD_ROOT/usr/local/sbin/* %{buildroot}%{_bindir}/
install -m 0755 -d %{buildroot}%{_docdir}/
mv $RPM_BUILD_ROOT/usr/local/share/doc/husk %{buildroot}%{_docdir}/
install -m 0755 -d %{buildroot}%{_mandir}/
mv $RPM_BUILD_ROOT/usr/local/share/man/* %{buildroot}%{_mandir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo " "
echo "Example configuration is in /usr/share/doc/husk/"

%files
%{_bindir}/husk
%{_bindir}/fire
%config(noreplace) %{_sysconfdir}/husk/addr_groups.conf
%config(noreplace) %{_sysconfdir}/husk/husk.conf
%config(noreplace) %{_sysconfdir}/husk/interfaces.conf
%{_sysconfdir}/husk/helpers/apple-ios.conf
%{_sysconfdir}/husk/helpers/avg.conf
%{_sysconfdir}/husk/helpers/dhcp.conf
%{_sysconfdir}/husk/helpers/dns.conf
%{_sysconfdir}/husk/helpers/gotomeeting.conf
%{_sysconfdir}/husk/helpers/icmp.conf
%{_sysconfdir}/husk/helpers/mail.conf
%{_sysconfdir}/husk/helpers/pptp.conf
%{_sysconfdir}/husk/helpers/samba.conf
%{_sysconfdir}/husk/helpers/snmp.conf
%{_sysconfdir}/husk/helpers/sql.conf
%{_docdir}/husk/ABOUT
%{_docdir}/husk/LICENSE
%{_docdir}/husk/README
%{_docdir}/husk/rules.conf.simple
%{_docdir}/husk/rules.conf.standalone
%{_mandir}/man1/fire.1p.gz
%{_mandir}/man1/husk.1p.gz
