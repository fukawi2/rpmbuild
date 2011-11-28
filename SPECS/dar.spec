#
# Specfile for DAR, the disk archiver
#
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=210790
#

# Static build is disabled by default by fedora policy, but also because the
# latest versions of glibc don't seem to compile proper static binaries.  Use
# "--with static" to enable the static subpackage
%define with_static %{?_with_static: 1} %{?!_with_static: 0}

#
# Basic descriptive tags for this package:
#
Name:           dar
Version:        2.4.2
Release:        2%{?dist}
Summary:        Software for making/restoring incremental CD/DVD backups

URL:            http://dar.linux.free.fr/
License:        GPL
Group:          Applications/Archiving

################################################################################

Source:         http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

################################################################################

BuildRequires:  bzip2-devel
BuildRequires:  openssl-devel
BuildRequires:  libgcrypt-devel

# Recommended, but no package yet in Epel.
#Requires:       par2cmdline

################################################################################

%description
DAR is a command line tool to backup a directory tree and files. DAR is
able to make differential backups, split them over a set of disks or files
of a given size, use compression, filter files or subtrees to be saved or
not saved, directly access and restore given files. DAR is also able
to handle extented attributes, and can make remote backups through an
ssh session for example. Finally, DAR handles save and restore of hard
and symbolic links.

################################################################################

%package -n libdar
Group:      System Environment/Libraries
Summary:    Library providing support for the DAR API

%description -n libdar
Common library code for DAR.

################################################################################

%package -n libdar-devel
Group:      Development/Libraries
Summary:    Development files for libdar
Requires:   libdar = %{version}-%{release}

%description -n libdar-devel
This package contains the header files and libraries for developing
programs that use the DAR API (libdar).

################################################################################
# The following two subpackages are only built when enabled via "--with static"
################################################################################

%if %{with_static}

%package -n dar-static
Group:      Applications/System
Summary:    Statically linked version of dar

%description -n dar-static
Statically linked version of dar that can be installed onto backup disks for
easier file retrieval.

%package -n libdar-static-devel
Group:      Development/Libraries
Summary:    Statically linked dar library files

%description -nlibdar-static-devel
Statically linked version of dar libraries that can be installed onto backup
disks for easier file retrieval.

%endif

################################################################################

%prep
%setup -q

################################################################################

%build

# Options
%if %{with_static}
    STATIC=""
%else
    STATIC="--disable-dar-static --disable-static"
%endif

%configure --disable-build-html $STATIC

make %{?_smp_mflags}

################################################################################

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

# Remove the libtool archive files
rm -f  $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT/%{_libdir}/pkgconfig

# Delete the sample files that we can't seem to disable
rm -rf $RPM_BUILD_ROOT/%{_datadir}/dar/

# Remove the doc makefiles so they don't get installed along with the other files.
rm -f doc/Makefile*
rm -f doc/*/Makefile*

# Rename the documentation directory so it makes more sense after installation.
mv doc html

# Sample scripts should not be executable
chmod 0644 html/samples/*

################################################################################

%clean
rm -rf $RPM_BUILD_ROOT

################################################################################

%post   -n libdar -p /sbin/ldconfig
%postun -n libdar -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc html/ ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO

%{_bindir}/dar
%{_bindir}/dar_cp
%{_bindir}/dar_manager
%{_bindir}/dar_slave
%{_bindir}/dar_xform
%{_mandir}/man1/*
%{_sysconfdir}/darrc

################################################################################

%files -n libdar
%defattr(-,root,root,-)
%{_libdir}/*.so.*

################################################################################

%files -n libdar-devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so

################################################################################

%if %{with_static}

%files -n dar-static
%defattr(-,root,root,-)
%{_bindir}/dar_static

################################################################################

%files -n libdar-static-devel
%defattr(-,root,root,-)
%{_libdir}/*.a

################################################################################
%endif

%changelog
