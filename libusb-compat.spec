%bcond_without	doc	# don't build documentation

Summary:	Application access to USB devices
Name:		libusb-compat
Version:	0.1.4
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dowmloads.sourceforge.net/libusb/%{name}-%{version}.tar.bz2
# Source0-md5:	2ca521fffadd0c28fdf174e6ec73865b
Patch0:		%{name}-usbx.patch
URL:		http://libusbx.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusbx-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a library for application access to USB devices.

%package devel
Summary:	Header files for libusb library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files and other resources you can use to
incorporate libusb into applications.

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%check
%{__make} check

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
%doc AUTHORS README NEWS ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libusb-*.so.?
%attr(755,root,root) %{_libdir}/libusb-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libusb-config
%attr(755,root,root) %{_libdir}/libusb.so
%{_libdir}/libusb.la
%{_includedir}/usb.h
%{_pkgconfigdir}/libusb.pc

