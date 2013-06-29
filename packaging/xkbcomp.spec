Name:           xkbcomp
Version:        1.2.4
Release:        0
License:        MIT
Summary:        Utility to compile XKB keyboard description
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source:         %{name}-%{version}.tar.bz2
Source1001: 	xkbcomp.manifest
BuildRequires:  bison
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17

%description
The xkbcomp keymap compiler converts a description of an XKB keymap
into one of several output formats.

%package devel
Summary:        Utility to compile XKB keyboard description -- Development Files
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}

%description devel
The xkbcomp keymap compiler converts a description of an XKB keymap
into one of several output formats.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc COPYING
%{_bindir}/xkbcomp
%{_mandir}/man1/xkbcomp.1%{?ext_man}

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/pkgconfig/xkbcomp.pc

%changelog