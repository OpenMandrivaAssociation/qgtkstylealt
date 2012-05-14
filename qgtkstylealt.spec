Name:		qgtkstylealt
Summary:	ROSA Alternative GTK+ style for Qt
Version:	0.1.1
Release:	2
Source0:	qgtkstylealt-%{version}.tar.gz
Group:		Graphical desktop/KDE
License:	GPLv3
Requires:       kdebase4-runtime
Requires:       gtk+2.0
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:	kde4-macros
BuildRequires:  kdebase4-devel 
BuildRequires:  kdebase4-workspace-devel

%description
ROSA Alternative GTK+ style for Qt

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plugins/styles/qgtkstylealt.so
%_kde_datadir/apps/kstyle/themes/qgtkstylealt.themerc

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde

%make

%install

%makeinstall_std -C build
