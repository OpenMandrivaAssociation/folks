%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define dirver 37
%define major 25
%define gir_major 0.6

%define libname		%mklibname %{name} %{major}
%define girname		%mklibname %{name}-gir %{gir_major}
%define develname	%mklibname -d %{name}

%define enable_vala 0

Summary:	Aggregates people from multiple sources to create metacontacts
Name:		folks
Version:	0.7.4.1
Release:	1
Group:		Networking/Instant messaging
License:	LGPLv2+
URL:		http://telepathy.freedesktop.org/wiki/Folks
Source0:	http://ftp.gnome.org/pub/GNOME/sources/folks/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	glib2.0-common
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:	pkgconfig(telepathy-glib) >= 0.13
BuildRequires:	pkgconfig(gconf-2.0) >= 2.31
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:	pkgconfig(libedata-book-1.2) >= 3.1.5
BuildRequires:	pkgconfig(libsocialweb-client)
BuildRequires:	pkgconfig(tracker-sparql-0.14)
BuildRequires:	pkgconfig(zeitgeist-1.0)
BuildRequires:	tracker-devel
BuildRequires:	vala-devel
BuildRequires:	vala-tools

Requires:	evolution-data-server

Obsoletes: %{name}-i18n

%description
libfolks is a library that aggregates people from multiple sources (eg,
Telepathy connection managers and eventually evolution data server, Facebook,
etc.) to create metacontacts. It's written in Vala (in part to evaluate Vala).
The initial goal is for GObject/C support, though the Vala bindings should
basically automatic.

%package -n %{libname}
Group:		System/Libraries
Summary:	Aggregates people from multiple sources to create metacontacts
# old libs left over in the repo
Obsoletes:	%{mklibname folks 0} < 0.7.0
Obsoletes:	%{mklibname folks 1} < 0.7.0

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{girname}
Group:		System/Libraries
Summary:	Aggregates people from multiple sources to create metacontacts
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
This package contains the Gir-repository typelib for %{name}.

%package -n %{develname}
Group:		Development/C
Summary:	Aggregates people from multiple sources to create metacontacts
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

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

%files -f %{name}.lang
%doc AUTHORS README
%{_bindir}/folks-import
%dir %{_libdir}/folks/%{dirver}/
%{_libdir}/folks/%{dirver}/backends
%{_datadir}/GConf/gsettings/folks.convert
%{_datadir}/glib-2.0/schemas/org.freedesktop.folks.gschema.xml

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

%changelog
* Tue Oct  2 2012 Arkady L. Shane <ashejn@rosalab.ru> 0.7.1.4-1
- update to 0.7.4.1

* Thu May 10 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.7.0-2
+ Revision: 798067
- rebuild
- added requires for eds otherwise none of the backend stuff works

* Sat May 05 2012 Guilherme Moro <guilherme@mandriva.com> 0.7.0-1
+ Revision: 796866
- Updated to version 0.7.0

  + Götz Waschk <waschk@mandriva.org>
    - update to new version 0.6.9
    - new version

* Thu Feb 23 2012 Götz Waschk <waschk@mandriva.org> 0.6.7-1
+ Revision: 779337
- update plugin version
- update to new version 0.6.7

* Thu Jan 19 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.6.6-1
+ Revision: 762807
- last fix
- try the pcpa method
- fix build
- split out gir pkg
- added enable vala option
- not working atm
- fixed files list
- new version 0.6.5
- removed defattr
- remove .la files
- merged i18n pkg in with main pkg
- moved backends to main pkg
- cleaned up spec
- shortened lib & devel descriptions
- removed extra devel provide
- converted BRs to pkgconfig provides
- removed mkrel & BuildRoot

  + Alexander Khrukin <akhrukin@mandriva.org>
    - version update 0.6.6

* Tue Apr 26 2011 Götz Waschk <waschk@mandriva.org> 0.4.3-1
+ Revision: 659416
- update to new version 0.4.3

* Mon Apr 04 2011 Götz Waschk <waschk@mandriva.org> 0.4.2-1
+ Revision: 650293
- new version
- new major
- add translations
- bump telepathy-glib dep

* Tue Oct 26 2010 Götz Waschk <waschk@mandriva.org> 0.2.1-1mdv2011.0
+ Revision: 589430
- new version
- new library major

* Mon Sep 20 2010 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdv2011.0
+ Revision: 579959
- new version
- update deps
- new directory version

* Sat Sep 11 2010 Götz Waschk <waschk@mandriva.org> 0.1.17-1mdv2011.0
+ Revision: 577153
- new version
- new dir version
- add folks-import
- add vala vapi files

* Wed Sep 01 2010 Götz Waschk <waschk@mandriva.org> 0.1.16-1mdv2011.0
+ Revision: 575173
- update to new version 0.1.16

* Fri Aug 27 2010 Götz Waschk <waschk@mandriva.org> 0.1.15-1mdv2011.0
+ Revision: 573462
- new version
- new dir version

* Wed Aug 18 2010 Götz Waschk <waschk@mandriva.org> 0.1.14.1-1mdv2011.0
+ Revision: 571214
- update to new version 0.1.14.1

* Wed Aug 18 2010 Götz Waschk <waschk@mandriva.org> 0.1.14-1mdv2011.0
+ Revision: 571200
- update build deps
- new version
- drop patch
- bump vala dep

* Wed Aug 11 2010 Götz Waschk <waschk@mandriva.org> 0.1.13-1mdv2011.0
+ Revision: 569148
- new version
- patch for new vala
- new plugin directory version

* Mon Aug 02 2010 Götz Waschk <waschk@mandriva.org> 0.1.12-1mdv2011.0
+ Revision: 565158
- new version
- update file list

* Mon Aug 02 2010 Funda Wang <fwang@mandriva.org> 0.1.11-1mdv2011.0
+ Revision: 565082
- import folks


