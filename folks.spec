%define dirver 33
%define major 25
%define gir_major 0.6

%define libname		%mklibname %{name} %{major}
%define girname		%mklibname %{name}-gir %{gir_major}
%define develname	%mklibname -d %{name}

%define enable_vala 0

Summary:	Aggregates people from multiple sources to create metacontacts
Name:		folks
Version:	0.7.0
Release:	1
Group:		Networking/Instant messaging
License:	LGPLv2+
URL:		http://telepathy.freedesktop.org/wiki/Folks
Source0:	http://ftp.gnome.org/pub/GNOME/sources/folks/%{name}-%{version}.tar.xz

BuildRequires: glib2.0-common
BuildRequires: intltool
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires: pkgconfig(telepathy-glib) >= 0.13
BuildRequires: pkgconfig(gconf-2.0) >= 2.31
BuildRequires: pkgconfig(gee-1.0)
BuildRequires: pkgconfig(libebook-1.2)
BuildRequires: pkgconfig(libedataserver-1.2)
BuildRequires: pkgconfig(libedata-book-1.2) >= 3.1.5
BuildRequires: pkgconfig(libsocialweb-client)
BuildRequires: tracker-devel
BuildRequires: vala-devel
BuildRequires: vala-tools

Obsoletes: %{name}-i18n

%description
libfolks is a library that aggregates people from multiple sources (eg,
Telepathy connection managers and eventually evolution data server, Facebook,
etc.) to create metacontacts. It's written in Vala (in part to evaluate Vala).
The initial goal is for GObject/C support, though the Vala bindings should
basically automatic.

%package -n %{libname}
Group: System/Libraries
Summary: Aggregates people from multiple sources to create metacontacts
# old libs left over in the repo
Obsoletes:	%mklibname %{name} 0
Obsoletes:	%mklibname %{name} 1

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{girname}
Group:		System/Libraries
Summary:	Aggregates people from multiple sources to create metacontacts
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
This package contains the Gir-repository typelib for %{name}.

%package -n %{develname}
Group: Development/C
Summary: Aggregates people from multiple sources to create metacontacts
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
This packages contains the headers and libraries for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure \
	--enable-tracker-backend \
	--enable-libsocialweb-backend=auto \
	--enable-eds-backend \
%if %{enable_vala}
	--enable-vala \
	--enable-inspect-tool \
%endif
	--enable-import-tool

%make LIBS='-lgmodule-2.0'

%install
%makeinstall_std
%find_lang %{name}

# remove unpackaged files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -f %{name}.lang
%doc AUTHORS README
%_bindir/folks-import
%dir %{_libdir}/folks/%{dirver}/
%{_libdir}/folks/%{dirver}/backends

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Folks-%{gir_major}.typelib


%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/folks
%{_datadir}/vala/vapi/folks*
%{_datadir}/gir-1.0/Folks-%{gir_major}.gir

