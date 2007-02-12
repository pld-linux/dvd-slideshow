Summary:	dvd-slideshow makes a DVD slideshow video
Summary(pl.UTF-8):   dvd-slideshow - tworzenie filmu DVD z pokazem slajdów
Name:		dvd-slideshow
Version:	0.8.0
%define		_rel	-1
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/dvd-slideshow/%{name}-%{version}%{_rel}.tar.gz
# Source0-md5:	83ff69e76ba2bfd0d1c735ada0dc64dd
URL:		http://dvd-slideshow.sourceforge.net/
Requires:	ImageMagick >= 5.5.4
Requires:	dvdauthor >= 0.6.10
Requires:	mjpegtools >= 1.6.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvd-slideshow makes a DVD slideshow video with menus from a text
file listing of pictures, effects, and audio tracks. You can add
some nice effects like fades, crops, scrolls, or Ken Burns effects.
It will hopefully become a command-line clone of imovie.

%description -l pl.UTF-8
dvd-slideshow tworzy film DVD z pokazem slajdów zawierający menu z
tekstowej listy plików, efektów i ścieżek dźwiękowych. Można dodawać
różne ładne efekty, takie jak przejścia, obcięcia, przewijanie albo
efekty Kena Burnsa. Projekt w zamierzeniu ma stać się działającym z
linii poleceń klonem imovie.

%prep
%setup -q -n %{name}-%{version}%{_rel}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dir2slideshow $RPM_BUILD_ROOT%{_bindir}
install dvd-menu $RPM_BUILD_ROOT%{_bindir}
install dvd-slideshow $RPM_BUILD_ROOT%{_bindir}
install gallery1-to-slideshow $RPM_BUILD_ROOT%{_bindir}
install jigl2slideshow $RPM_BUILD_ROOT%{_bindir}
install man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
