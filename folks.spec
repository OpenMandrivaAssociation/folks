%define major 22
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define dirver 22

Name:           folks
Version:        0.4.3
Release:        %mkrel 1
Summary:        Aggregates people from multiple sources to create metacontacts

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/Folks
Source0:        http://ftp.gnome.org/pub/GNOME/sources/folks/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	libtelepathy-glib-devel >= 0.13
BuildRequires:	vala-devel > 0.9.5
BuildRequires:	vala-tools
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	libgee-devel

%description
libfolks is a library that aggregates people from multiple sources (eg,
Telepathy connection managers and eventually evolution data server, Facebook,
etc.) to create metacontacts. It's written in Vala (in part to evaluate Vala).
The initial goal is for GObject/C support, though the Vala bindings should
basically automatic.

%package i18n
Group: System/Internationalization
Summary: Translations for %name
%description i18n
This package contains the translations for %{name}.

%package -n %libname
Group: System/Libraries
Summary: Aggregates people from multiple sources to create metacontacts
Requires: %name-i18n >= %version

%description -n %libname
libfolks is a library that aggregates people from multiple sources (eg,
Telepathy connection managers and eventually evolution data server, Facebook,
etc.) to create metacontacts. It's written in Vala (in part to evaluate Vala).
The initial goal is for GObject/C support, though the Vala bindings should
basically automatic.

%package -n %develname
Group: Development/C
Summary: Aggregates people from multiple sources to create metacontacts
Requires: %libname = %version-%release
Provides: lib%name-devel = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
libfolks is a library that aggregates people from multiple sources (eg,
Telepathy connection managers and eventually evolution data server, Facebook,
etc.) to create metacontacts. It's written in Vala (in part to evaluate Vala).
The initial goal is for GObject/C support, though the Vala bindings should
basically automatic.

%files i18n -f %name.lang

%files
%defattr(-,root,root)
%doc AUTHORS README
%_bindir/folks-import

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}*
%dir %{_libdir}/folks/%dirver/
%{_libdir}/folks/%dirver/backends

%files -n %develname
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/folks
%_datadir/vala/vapi/folks*
#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std
%find_lang %name

%clean
rm -rf %buildroot
