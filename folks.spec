%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1
%define _disable_lto 1

%define dirver	46
%define major	26
%define gmajor	0.7
%define libname		%mklibname %{name} %{major}
%define libdummy	%mklibname %{name}-dummy %{major}
%define libeds		%mklibname %{name}-eds %{major}
%define libtelepathy	%mklibname %{name}-telepathy %{major}
%define libtracker	%mklibname %{name}-tracker %{major}
%define girname		%mklibname %{name}-gir %{gmajor}
%define devname		%mklibname -d %{name}

Summary:	Aggregates people from multiple sources to create metacontacts
Name:		folks
Version:	0.15.2
Release:	1
Group:		Networking/Instant messaging
License:	LGPLv2+
Url:		http://telepathy.freedesktop.org/wiki/Folks
Source0:	http://ftp.gnome.org/pub/GNOME/sources/folks/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	glib2.0-common
BuildRequires:	intltool
BuildRequires:	pkgconfig(readline)
#BuildRequires:	tracker-devel
BuildRequires:	tracker-vala
BuildRequires:	vala
BuildRequires:	vala-tools
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:	pkgconfig(telepathy-glib) >= 0.13
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:	pkgconfig(libedata-book-1.2) >= 3.1.5
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(zeitgeist-2.0)
BuildRequires:	python3dist(python-dbusmock)
Requires:	evolution-data-server
Requires:	tracker-miners
Obsoletes:	%{name}-i18n

%description
libfolks is a library that aggregates people from multiple sources (eg,
Telepathy connection managers and eventually evolution data server, Facebook,
etc.) to create metacontacts. It's written in Vala (in part to evaluate Vala).
The initial goal is for GObject/C support, though the Vala bindings should
basically automatic.

%package -n %{libname}
Group:		System/Libraries
Summary:	Aggregates people from multiple sources to create metacontacts

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{libdummy}
Group:          System/Libraries
Summary:        Aggregates people from multiple sources to create metacontacts
Conflicts:      %{_lib}folks25 < 0.8.0-3

%description -n %{libdummy}
This package contains the dynamic libraries from %{name}.


%package -n %{libeds}
Group:		System/Libraries
Summary:	Aggregates people from multiple sources to create metacontacts
Conflicts:	%{_lib}folks25 < 0.8.0-3

%description -n %{libeds}
This package contains the dynamic libraries from %{name}.

%package -n %{libtelepathy}
Group:		System/Libraries
Summary:	Aggregates people from multiple sources to create metacontacts
Conflicts:	%{_lib}folks25 < 0.8.0-3

%description -n %{libtelepathy}
This package contains the dynamic libraries from %{name}.

%package -n %{libtracker}
Group:		System/Libraries
Summary:	Aggregates people from multiple sources to create metacontacts
Conflicts:	%{_lib}folks25 < 0.8.0-3

%description -n %{libtracker}
This package contains the dynamic libraries from %{name}.

%package -n %{girname}
Group:		System/Libraries
Summary:	Aggregates people from multiple sources to create metacontacts

%description -n %{girname}
This package contains the Gir-repository typelib for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Aggregates people from multiple sources to create metacontacts
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libdummy} = %{version}-%{release}
Requires:	%{libeds} = %{version}-%{release}
Requires:	%{libtelepathy} = %{version}-%{release}
#Requires:	#{libtracker} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This packages contains the headers and libraries for %{name}.

%prep
%setup -q
%autopatch -p1

%build

%meson \
	-Deds_backend=true \
	-Dinspect_tool=true \
	-Dimport_tool=true \
	-Dzeitgeist=true \
	-Dtracker_backend=false
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.md
%{_bindir}/folks-import
%{_bindir}/folks-inspect
%dir %{_libdir}/folks/%{dirver}/
%{_libdir}/folks/%{dirver}/backends
#{_datadir}/GConf/gsettings/folks.convert
%{_datadir}/glib-2.0/schemas/org.freedesktop.folks.gschema.xml
%{_datadir}/GConf/gsettings/folks.convert

%files -n %{libname}
%{_libdir}/libfolks.so.%{major}*

%files -n %{libdummy}
%{_libdir}/libfolks-dummy.so.%{major}*

%files -n %{libeds}
%{_libdir}/libfolks-eds.so.%{major}*

%files -n %{libtelepathy}
%{_libdir}/libfolks-telepathy.so.%{major}*

%files -n %{libtracker}
#{_libdir}/libfolks-tracker.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Folks-%{gmajor}.typelib
%{_libdir}/girepository-1.0/FolksDummy-%{gmajor}.typelib
%{_libdir}/girepository-1.0/FolksEds-%{gmajor}.typelib
%{_libdir}/girepository-1.0/FolksTelepathy-%{gmajor}.typelib
#{_libdir}/girepository-1.0/FolksTracker-%{gmajor}.typelib

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/folks
%{_datadir}/vala/vapi/folks*
%{_datadir}/gir-1.0/Folks-%{gmajor}.gir
%{_datadir}/gir-1.0/FolksDummy-%{gmajor}.gir
%{_datadir}/gir-1.0/FolksEds-%{gmajor}.gir
%{_datadir}/gir-1.0/FolksTelepathy-%{gmajor}.gir
#{_datadir}/gir-1.0/FolksTracker-%{gmajor}.gir

