Summary:	Library to create and read several different archive formats
Name:		libarchive
Version:	3.1.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.libarchive.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	efad5a503f66329bb9d2f4308b5de98a
Patch0:		%{name}-man_progname.patch
Patch1:		0001-mtree-fix-line-filename-length-calculation.patch
URL:		http://www.libarchive.org/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
# for <ext2fs/ext2_fs.h>
BuildRequires:	e2fsprogs-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular TAR
variants and several CPIO formats. It can also write SHAR archives.

%package devel
Summary:	Header files for libarchive library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libarchive library.

%package bsd-tools
Summary:	BSD tools
Group:		Applications/Archiving
Requires:	%{name} = %{version}-%{release}

%description bsd-tools
BSD tools based on libarchive.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I build/autoconf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libarchive.so.??
%attr(755,root,root) %{_libdir}/libarchive.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarchive.so
%{_libdir}/libarchive.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*
%{_mandir}/man5/*

%files bsd-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bsdtar
%attr(755,root,root) %{_bindir}/bsdcpio
%{_mandir}/man1/bsdtar.1*
%{_mandir}/man1/bsdcpio.1*

