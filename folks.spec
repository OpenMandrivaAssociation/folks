%define major 22
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}
%define dirver 22

Summary:	Aggregates people from multiple sources to create metacontacts
Name:		folks
Version:	0.6.5
Release:	1
Group:		Networking/Instant messaging
License:	LGPLv2+
URL:		http://telepathy.freedesktop.org/wiki/Folks
Source0:	http://ftp.gnome.org/pub/GNOME/sources/folks/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires: pkgconfig(telepathy-glib) >= 0.13
BuildRequires: vala-devel > 0.9.5
BuildRequires: vala-tools
BuildRequires: pkgconfig(gee-1.0)

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

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{develname}
Group: Development/C
Summary: Aggregates people from multiple sources to create metacontacts
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

# remove unpackaged files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%description -n %{develname}
This packages contains the headers and libraries for %{name}.

%files -f %{name}.lang
%doc AUTHORS README
%_bindir/folks-import
%dir %{_libdir}/folks/%dirver/
%{_libdir}/folks/%dirver/backends

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/folks
%{_datadir}/vala/vapi/folks*

