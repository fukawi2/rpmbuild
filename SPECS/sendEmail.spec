Name		: sendEmail
Version		: 1.56
Release		: 1%{?dist}

License		: GPL
Summary		: A lightweight, completly command line based, SMTP email agent.
Group		: Applications/Internet

URL			: http://caspian.dotconf.net/menu/Software/SendEmail/
Vendor		: LandShark Networks
Distribution: %distro
Packager	: %{myname} %{myemail}

BuildRoot	: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0		: http://caspian.dotconf.net/menu/Software/SendEmail/%{name}-v%{version}.tar.gz

Buildarch	: noarch

%description
SendEmail is a lightweight tool written in Perl for sending SMTP
email from the console. It was designed to be used in bash scripts,
Perl programs, and Web pages. It requires no special modules, and
has a simple interface, making it very easy to install and use.
It should work on any platform that has Perl and supports Unix
sockets, but was designed for Linux.

%prep
%setup -q -n %{name}-v%{version}

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%{__install} -d %{buildroot}%{_bindir}

%{__install} -c -m 755 %{name} %{buildroot}%{_bindir}/

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}
%doc CHANGELOG README TODO

%changelog
* Sat Jan 14 2006 LandShark BuildSys <BuildSys[AT]LandShark.Net>
- Specfile update.
