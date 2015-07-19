%define major	6
%define	libname	%mklibname gif %{major}
%define	devname	%mklibname -d gif

Summary:	Library for reading and writing gif images
Name:		giflib5.0
Version:	5.0.4
Release:	14
Group:		System/Libraries
License:	BSD like
Url:		http://giflib.sourceforge.net/
Source0:	http://switch.dl.sourceforge.net/project/giflib/giflib-5.x/giflib-%version.tar.bz2
Patch2:		giflib-4.2.1-automake-1.13.patch
BuildRequires:	xmlto
BuildRequires:	pkgconfig(x11)

%track
prog %name = {
	url = http://sourceforge.net/projects/giflib/
	regex = %name-(__VER__)\.tar\.bz2
	version = %version
}

%description
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for reading and writing gif images

%description -n	%{libname}
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

%prep
%setup -q -n giflib-%{version}
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

rm -Rf %{buildroot}/%_bindir
rm -Rf %{buildroot}/%_mandir
rm -Rf %{buildroot}/%_libdir/*.so
rm -Rf %{buildroot}/%_includedir

%files -n %{libname}
%{_libdir}/libgif.so.%{major}*

