Summary:	Utility to show EXIF information hidden in JPEG files
Summary(pl.UTF-8):	Narzędzie do wyświetlania danych EXIF ukrytych w plikach JPEG
Name:		exif
Version:	0.6.19
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/libexif/%{name}-%{version}.tar.bz2
# Source0-md5:	75f0dd6f9f2d128261721c0896e0b324
Patch0:		%{name}-pl.po-update.patch
Patch1:		%{name}-ac.patch
URL:		http://libexif.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	libexif-devel >= 1:0.6.19
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
Requires:	libexif >= 1:0.6.19
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
%patch1 -p1

rm -f po/stamp-po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4m
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/exif
%{_mandir}/man1/exif.1*
