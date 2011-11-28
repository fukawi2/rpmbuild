Summary:	Python script to check the RAM usage on the local machine.
Name:		check_ram
Version:	1
Release:	1
Source0:	check_ram.py
License:	GPL
Group:		MyJunk
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Checks the ram usage on the local machine, good for remote checks using nrpe.
Works on 32-bit and 64-bit Linux systems. Just run it. The help displays all
the necessary details, it follows the standards of all the other nagios
plugins. Any comments, suggestions or requests to hpsekhon(at)googlemail.com

%install
install -m 0755 -d %{buildroot}%{_bindir}/
install -m 0755 %{_sourcedir}/check_ram.py %{buildroot}%{_bindir}/check_ram

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo " "
echo "This will display after rpm installs the package!"

%files
%{_bindir}/check_ram
