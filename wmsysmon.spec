%define version 0.7.7
%define release %mkrel 1
%define name wmsysmon

Summary:	System information (memory, swap, uptime, IO) in a small dock app.
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
BuildRequires:	X11-devel
BuildRequires:	xpm-devel
Prefix:		/usr/X11R6

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
make -C src

%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%{_miconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_iconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_liconsdir}
tar xOjf %SOURCE1 %{name}.16x16.xpm > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.xpm
tar xOjf %SOURCE1 %{name}.32x32.xpm > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.xpm
tar xOjf %SOURCE1 %{name}.48x48.xpm > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.xpm

mkdir -p $RPM_BUILD_ROOT%{prefix}/bin/
install -m 755 src/wmsysmon $RPM_BUILD_ROOT%{prefix}/bin/

install -m 755 -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{prefix}/bin/%{name}" icon="%{name}.xpm"\\
                 needs="X11" section="Applications/Monitoring" title="WmSysMon"\\
                 longtitle="System information (memory, swap, uptime, IO) in a small icon"\\
EOF


%clean
[ -z $RPM_BUILD_ROOT ] || {
    rm -rf $RPM_BUILD_ROOT
}


%post
%{update_menus}


%postun
%{clean_menus}


%files
%defattr (-,root,root)
%doc ChangeLog README
%{prefix}/bin/%{name}
%{_liconsdir}/%{name}.xpm
%{_miconsdir}/%{name}.xpm
%{_iconsdir}/%{name}.xpm
%{_menudir}/%{name}

