Summary:	dvd-slideshow makes a DVD slideshow video
Summary(pl):	dvd-slideshow - tworzenie filmu DVD z pokazem slajd�w
Name:		dvd-slideshow
Version:	0.7.1
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/dvd-slideshow/%{name}_%{version}.tar.gz
# Source0-md5:	34c3455cc8b75f5ea3c199d447a34a9b
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

%description -l pl
dvd-slideshow tworzy film DVD z pokazem slajd�w zawieraj�cy menu z
tekstowej listy plik�w, efekt�w i �cie�ek d�wi�kowych. Mo�na dodawa�
r�ne �adne efekty, takie jak przej�cia, obci�cia, przewijanie albo
efekty Kena Burnsa. Projekt w zamierzeniu ma sta� si� dzia�aj�cym z
linii polece� klonem imovie.

%prep
%setup -q -n %{name}_%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dir2slideshow $RPM_BUILD_ROOT%{_bindir}
install dvd-menu $RPM_BUILD_ROOT%{_bindir}
install dvd-slideshow $RPM_BUILD_ROOT%{_bindir}
install dvd-menu $RPM_BUILD_ROOT%{_bindir}
install gallery2slideshow $RPM_BUILD_ROOT%{_bindir}
install jigl2slideshow $RPM_BUILD_ROOT%{_bindir}
install man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
