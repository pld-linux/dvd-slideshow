Summary:	dvd-slideshow makes a DVD slideshow video
Name:		dvd-slideshow
Version:	0.6.0
Release:	0.1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/dvd-slideshow/%{name}_%{version}.tar.gz
# Source0-md5:	e06335611f3108a6caba807633696127
URL:		http://dvd-slideshow.sourceforge.net/
Requires:	ImageMagic >= 5.5.4
Requires:	dvdauthor >= 0.6.10
Requires:	mjpegtools >= 1.6.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvd-slideshow makes a DVD slideshow video with menus from a text
file listing of pictures, effects, and audio tracks. You can add
some nice effects like fades, crops, scrolls, or Ken Burns effects.
It will hopefully become a command-line clone of imovie.

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
