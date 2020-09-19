Summary:	Utility to show EXIF information hidden in JPEG files
Summary(pl.UTF-8):	Narzędzie do wyświetlania danych EXIF ukrytych w plikach JPEG
Name:		exif
Version:	0.6.22
%define	tagver	%(echo %{version} | tr . _)
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
#Source0Download: https://github.com/libexif/exif/releases
Source0:	https://github.com/libexif/exif/releases/download/exif-%{tagver}-release/%{name}-%{version}.tar.xz
# Source0-md5:	bc600b12c50fbb26f025819164d963e6
Patch0:		%{name}-ac.patch
URL:		https://libexif.github.io/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.14.1
BuildRequires:	libexif-devel >= 1:0.6.20
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.12
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libexif >= 1:0.6.20
Requires:	popt >= 1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'exif' is a small command-line utility to show EXIF information hidden
in JPEG files, written to demonstrate the power of libexif.

%description -l pl.UTF-8
exif to małe narzędzie działające z linii poleceń, służące do
pokazywania informacji EXIF ukrytych w plikach JPEG. Zostało napisane
do pokazania możliwości libexif.

%prep
%setup -q
%patch0 -p1

%{__rm} po/stamp-po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4m
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/exif
%{_mandir}/man1/exif.1*
