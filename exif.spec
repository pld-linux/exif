Summary:	Utility to show EXIF information hidden in JPEG files
Summary(pl.UTF-8):	Narzędzie do wyświetlania danych EXIF ukrytych w plikach JPEG
Name:		exif
Version:	0.6.9
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/libexif/%{name}-%{version}.tar.gz
# Source0-md5:	555029098386fa677c461eb249d852d7
Source1:	%{name}-pl.po
Patch0:		%{name}-nls.patch
URL:		http://libexif.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libexif-devel >= 1:0.6.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
Requires:	libexif >= 1:0.6.9
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

cp %{SOURCE1} po/pl.po
%{__perl} -pi -e 's/de es fr/de es fr pl/' configure.in
rm -f po/stamp-po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
