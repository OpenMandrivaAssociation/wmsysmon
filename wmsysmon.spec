%define version 0.7.7
%define release %mkrel 7
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
URL:		http://www.gnugeneration.com/software/wmsysmon/src/
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxpm-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

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

