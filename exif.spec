Summary:	Utility to show EXIF information hidden in JPEG files
Summary(pl):	Narzêdzie do wy¶wietlania danych EXIF ukrytych w plikach JPEG
Name:		exif
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/libexif/%{name}-%{version}.tar.bz2
URL:		http://libexif.sourceforge.net/
BuildRequires:	libexif-devel >= 0.5.9
BuildRequires:	libmnote-devel >= 0.5.6
BuildRequires:	popt-devel
Requires:	libexif >= 0.5.9
Requires:	libmnote >= 0.5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'exif' is a small command-line utility to show EXIF information hidden
in JPEG files, written to demonstrate the power of libexif.

%description -l pl
exif to ma³e narzêdzie dzia³aj±ce z linii poleceñ, s³u¿±ce do
pokazywania informacji EXIF ukrytych w plikach JPEG. Zosta³o napisane
do pokazania mo¿liwo¶ci libexif.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
