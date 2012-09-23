Summary:	Library to create and read several different archive formats
Name:		libarchive
Version:	2.6.0
Release:	12
License:	BSD
Group:		Libraries
Source0:	https://github.com/downloads/libarchive/libarchive/%{name}-%{version}.tar.gz
# Source0-md5:	e8ceea99a86b022e192a06d2b411a29b
Patch0:		%{name}-man_progname.patch
URL:		http://libarchive.github.com/
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

%package bsdtar
Summary:	bsdtar - tar(1) implementation based on libarchive
Group:		Applications/Archiving
Requires:	%{name} = %{version}-%{release}

%description bsdtar
bsdtar - tar(1) implementation based on libarchive.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
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
%attr(755,root,root) %ghost %{_libdir}/libarchive.so.?
%attr(755,root,root) %{_libdir}/libarchive.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarchive.so
%{_libdir}/libarchive.la
%{_includedir}/*.h
%{_mandir}/man3/*
%{_mandir}/man5/*

%files bsdtar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bsdtar
%{_mandir}/man1/bsdtar.1*

