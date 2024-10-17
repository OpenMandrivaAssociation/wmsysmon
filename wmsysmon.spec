%define version 0.7.7
%define release  9
%define name wmsysmon

Summary:	System information (memory, swap, uptime, IO) in a small dock app
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Toys
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch0:         01-break.dpatch
Patch1:         02-output.dpatch
Patch2:         03-src_makefile.dpatch
URL:		https://www.gnugeneration.com/software/wmsysmon/src/
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)

%description
This is a small dock application for use with WindowMaker (www.windowmaker.org)
to show system information on interrupt activity, memory use, swap use, and IO.
Wmsysmon was originally written by Dave Clark, Vito Caputo took over
development.


%prep

%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make -C src CC="gcc %optflags %ldflags"

%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%{_miconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_iconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_liconsdir}
tar xOjf %SOURCE1 %{name}.16x16.xpm > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.xpm
tar xOjf %SOURCE1 %{name}.32x32.xpm > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.xpm
tar xOjf %SOURCE1 %{name}.48x48.xpm > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.xpm

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/wmsysmon $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=System;Monitor;
Name=WmSysMon
Comment=System information (memory, swap, uptime, IO) in a small icon
EOF


%clean
[ -z $RPM_BUILD_ROOT ] || {
    rm -rf $RPM_BUILD_ROOT
}


%if %mdkversion < 200900
%post
%{update_menus}
%endif


%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr (-,root,root)
%doc ChangeLog README
%{_bindir}/%{name}
%{_liconsdir}/%{name}.xpm
%{_miconsdir}/%{name}.xpm
%{_iconsdir}/%{name}.xpm
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 0.7.7-7mdv2011.0
+ Revision: 634836
- tighten BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.7.7-6mdv2010.0
+ Revision: 434918
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.7.7-5mdv2009.0
+ Revision: 262093
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.7.7-4mdv2009.0
+ Revision: 256266
- rebuild
- fix 'error: for key "Icon" in group "Desktop Entry" is an icon name with an
  extension, but there should be no extension as described in the Icon Theme
  Specification if the value is not an absolute path'
- fix summary-ended-with-dot

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.7.7-2mdv2008.1
+ Revision: 132230
- auto-convert XDG menu entry

* Tue Dec 18 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.7.7-1mdv2008.1
+ Revision: 132082
- Add xdg
- Add Debian patches and bump release

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - use %%mkrel
    - import wmsysmon



* Sun Aug 15 2004 Michael Scherer <misc@mandrake.org> 0.7.6-4mdk 
- from Jean-Noel Avila <avila@nerim.net>
  - add s4t4n patch for 2.6 kernel series

* Sun Dec 07 2003 Franck Villaume <fvill@freesurf.fr> 0.7.6-3mdk
- add real support to RPM_OPT_FLAGS
- add BuildRequires : xpm-devel

* Thu Jun 12 2003 Marcel Pol <mpol@gmx.net> 0.7.6-2mdk
- rebuild for rpm 4.2

* Thu May 31 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.7.6-1mdk
- Anecdotical fixes in the spec. fix to the menu file.

* Wed Oct 31 2000 HA Quôc-Viêt <viet@mandrakesoft.com> 0.7.6-0mdk
- Initial release.
