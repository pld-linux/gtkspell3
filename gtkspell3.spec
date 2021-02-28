#
# Conditional build:
%bcond_without	gtk2	# GTK+ 2.x variant
%bcond_without	gtk3	# GTK+ 3.x variant
%bcond_without	vala	# Vala API

Summary:	GTK+ 3 Spell Checker Interface Library
Summary(pl.UTF-8):	Biblioteka z interfejsem do narzędzia sprawdzającego pisownię dla GTK+ 3
Name:		gtkspell3
Version:	3.0.10
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/gtkspell/%{name}-%{version}.tar.xz
# Source0-md5:	34ece0c8cd0f68e6e125624ec0953cba
URL:		http://gtkspell.sourceforge.net/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	docbook-dtd42-xml
BuildRequires:	enchant2-devel >= 2
BuildRequires:	gettext-tools
BuildRequires:	gobject-introspection-devel >= 1.30.0
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 1:2.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iso-codes
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
%{?with_vala:BuildRequires:	vala >= 2:0.18.0}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words
in a GtkTextView widget. Right-clicking a misspelled word pops up a
menu of suggested replacements.

This package contains GtkSpell3 version for GTK+ 3.

%description -l pl.UTF-8
GtkSpell udostępnia podobne do MS Worda lub MacOSX podświetlanie
błędnie napisanych słów w widgecie GtkTextView. Kliknięcie prawym
przyciskiem na błędne słowo otwiera menu z sugerowanymi poprawkami.

Ten pakiet zawiera wersję biblioteki GtkSpell3 dla GTK+ 3.

%package devel
Summary:	Development files for GtkSpell3 for GTK+ 3
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GtkSpell3 dla GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-common-devel = %{version}-%{release}
Requires:	enchant2-devel >= 2
Requires:	gtk+3-devel >= 3.0

%description devel
Development files for GtkSpell3 for GTK+ 3.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki GtkSpell3 dla GTK+ 3.

%package static
Summary:	Static GtkSpell3 library for GTK+ 3
Summary(pl.UTF-8):	Biblioteka statyczna GtkSpell3 dla GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GtkSpell3 library for GTK+ 3.

%description static -l pl.UTF-8
Biblioteka statyczna GtkSpell3 dla GTK+ 3.

%package -n vala-%{name}
Summary:	GtkSpell3 API for Vala language (GTK+ 3 variant)
Summary(pl.UTF-8):	API GtkSpell3 dla języka Vala (wersja dla GTK+ 3)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18.0
BuildArch:	noarch

%description -n vala-%{name}
GtkSpell3 API for Vala language (GTK+ 3 variant).

%description -n vala-%{name} -l pl.UTF-8
API GtkSpell3 dla języka Vala (wersja dla GTK+ 3).

%package gtk2
Summary:	GTK+ 2 Spell Checker Interface Library
Summary(pl.UTF-8):	Biblioteka z interfejsem do narzędzia sprawdzającego pisownię dla GTK+ 2
Group:		X11/Libraries
Requires:	%{name}-common = %{version}-%{release}

%description gtk2
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words
in a GtkTextView widget. Right-clicking a misspelled word pops up a
menu of suggested replacements.

This package contains GtkSpell3 version for GTK+ 2.

%description gtk2 -l pl.UTF-8
GtkSpell udostępnia podobne do MS Worda lub MacOSX podświetlanie
błędnie napisanych słów w widgecie GtkTextView. Kliknięcie prawym
przyciskiem na błędne słowo otwiera menu z sugerowanymi poprawkami.

Ten pakiet zawiera wersję biblioteki GtkSpell3 dla GTK+ 2.

%package gtk2-devel
Summary:	Development files for GtkSpell3 for GTK+ 2
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GtkSpell3 dla GTK+ 2
Group:		X11/Development/Libraries
Requires:	%{name}-common-devel = %{version}-%{release}
Requires:	%{name}-gtk2 = %{version}-%{release}
Requires:	enchant-devel >= 0.4.0
Requires:	gtk+2-devel >= 1:2.0

%description gtk2-devel
Development files for GtkSpell3 for GTK+ 2.

%description gtk2-devel -l pl.UTF-8
Pliki programistyczne biblioteki GtkSpell3 dla GTK+ 2.

%package gtk2-static
Summary:	Static GtkSpell3 library for GTK+ 2
Summary(pl.UTF-8):	Biblioteka statyczna GtkSpell3 dla GTK+ 2
Group:		X11/Development/Libraries
Requires:	%{name}-gtk2-devel = %{version}-%{release}

%description gtk2-static
Static GtkSpell3 library for GTK+ 2.

%description gtk2-static -l pl.UTF-8
Biblioteka statyczna GtkSpell3 dla GTK+ 2.

%package -n vala-%{name}-gtk2
Summary:	GtkSpell3 API for Vala language (GTK+ 2 variant)
Summary(pl.UTF-8):	API GtkSpell3 dla języka Vala (wersja dla GTK+ 2)
Group:		Development/Libraries
Requires:	%{name}-gtk2-devel = %{version}-%{release}
Requires:	vala >= 2:0.18.0
BuildArch:	noarch

%description -n vala-%{name}-gtk2
GtkSpell3 API for Vala language (GTK+ 2 variant).

%description -n vala-%{name}-gtk2 -l pl.UTF-8
API GtkSpell3 dla języka Vala (wersja dla GTK+ 2).

%package common
Summary:	Common files for GtkSpell3 libraries
Summary(pl.UTF-8):	Pliki wspólne bibliotek GtkSpell3
Group:		Libraries
Conflicts:	gtkspell3 < 3.0.9
BuildArch:	noarch

%description common
Common files for GtkSpell3 libraries.

%description common -l pl.UTF-8
Pliki wspólne bibliotek GtkSpell3.

%package common-devel
Summary:	Common headers for GtkSpell3 libraries
Summary(pl.UTF-8):	Wspólne pliki nagłówkowe bibliotek GtkSpell3
Group:		Development/Libraries
Requires:	%{name}-common = %{version}-%{release}
BuildArch:	noarch

%description common-devel
Common headers for GtkSpell3 libraries.

%description common-devel -l pl.UTF-8
Wspólne pliki nagłówkowe bibliotek GtkSpell3.

%package apidocs
Summary:	GtkSpell API documentation
Summary(pl.UTF-8):	Dokumentacja API gtkspell
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
GtkSpell API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gtkspell.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	%{?with_gtk2:--enable-gtk2} \
	%{!?with_gtk3:--disable-gtk2} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgtkspell3-*.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/son

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   gtk2 -p /sbin/ldconfig
%postun gtk2 -p /sbin/ldconfig

%if %{with gtk3}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkspell3-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkspell3-3.so.0
%{_libdir}/girepository-1.0/GtkSpell-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkspell3-3.so
%{_pkgconfigdir}/gtkspell3-3.0.pc
%{_datadir}/gir-1.0/GtkSpell-3.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkspell3-3.a

%if %{with vala}
%files -n vala-%{name}
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gtkspell3-3.0.deps
%{_datadir}/vala/vapi/gtkspell3-3.0.vapi
%endif
%endif

%if %{with gtk2}
%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkspell3-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkspell3-2.so.0
%{_libdir}/girepository-1.0/GtkSpell-2.0.typelib

%files gtk2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkspell3-2.so
%{_pkgconfigdir}/gtkspell3-2.0.pc
%{_datadir}/gir-1.0/GtkSpell-2.0.gir

%files gtk2-static
%defattr(644,root,root,755)
%{_libdir}/libgtkspell3-2.a

%if %{with vala}
%files -n vala-%{name}-gtk2
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gtkspell3-2.0.deps
%{_datadir}/vala/vapi/gtkspell3-2.0.vapi
%endif
%endif

%files common -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README

%files common-devel
%defattr(644,root,root,755)
%{_includedir}/gtkspell-3.0

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtkspell3
