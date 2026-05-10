%define debug_package %{nil}

Name:		evolution-on
Version:	v3.24.2.20211004
Release:	3%{?dist}
Summary:	Tray plugin for the Evolution email client

License:	GPL
URL:		https://github.com/acidrain42/evolution-on
Source0:	evolution-on.tar.gz

BuildRequires:	evolution-devel gcc libtool autoconf make GConf2-devel intltool
Requires:	evolution

%description
Tray plugin for the Evolution email client

%prep
%setup -n evolution-on-master


%build
autoreconf -sivf
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_libdir}/evolution/plugins/*
%{_datadir}/GConf/gsettings/evolution-on.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.evolution-on.gschema.xml

%changelog
* Sat May 10 2026 Rodrigo Araujo <araujo.rm@gmail.com>
- Move patches into the git history of the fork; build SRPM from repo via COPR

* Wed Apr 16 2025 Rodrigo Araujo <araujo.rm@gmail.com>
- Add required include for newer GTK versions

* Mon Oct 04 2021 Rodrigo Araujo <araujo.rm@gmail.com>
- Initial package
