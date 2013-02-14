# TODO
# - gtk+2 bindings possible besides gtk+3 as well
Summary:	GTK+ Spell Checker Interface Library
Summary(pl.UTF-8):	Biblioteka z interfejsem do narzędzia sprawdzającego pisownię dla GTK+
Name:		gtkspell3
Version:	3.0.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	861c7188dbcc89dc24744d47102c4b18
URL:		http://gtkspell.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	docbook-dtd42-xml
BuildRequires:	enchant-devel >= 0.4.0
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.13.3
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words
in a GtkTextView widget. Right-clicking a misspelled word pops up a
menu of suggested replacements.

%description -l pl.UTF-8
GtkSpell udostępnia podobne do MS Worda lub MacOSX podświetlanie
błędnie napisanych słów w widgecie GtkTextView. Kliknięcie prawym
przyciskiem na błędne słowo otwiera menu z sugerowanymi poprawkami.

%package devel
Summary:	Header files for GtkSpell API version 3.0
Summary(pl.UTF-8):	Pliki nagłówkowe dla gtkspella
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	enchant-devel >= 0.4.0
Requires:	gtk+3-devel

%description devel
Header files for GtkSpell API version 3.0.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gtkspella.

%package static
Summary:	Static libraries for GtkSpell
Summary(pl.UTF-8):	Biblioteki statyczne dla gtkspella
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for GtkSpell.

%description static -l pl.UTF-8
Biblioteki statyczne dla gtkspella.

%package apidocs
Summary:	GtkSpell API documentation
Summary(pl.UTF-8):	Dokumentacja API gtkspell
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GtkSpell API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gtkspell.

%prep
%setup -q -n %{name}-%{version}

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
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgtkspell3-3.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ak
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/son

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libgtkspell3-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkspell3-3.so.0
%{_libdir}/girepository-1.0/GtkSpell-3.0.typelib

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgtkspell3-3.so
%{_includedir}/gtkspell-3.0
%{_pkgconfigdir}/gtkspell3-3.0.pc
%{_datadir}/gir-1.0/GtkSpell-3.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkspell3-3.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtkspell3
