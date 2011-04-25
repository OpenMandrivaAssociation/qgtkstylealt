Name:		qgtkstylealt
Summary:	ROSA Alternative GTK+ style for Qt
Version:	0.1.1
Release:	%mkrel 1
Source0:	qgtkstylealt-%{version}.tar.gz
Group:		Graphical desktop/KDE
License:	GPLv3
Requires:       kdebase4-runtime
BuildRequires:	kdelibs4-devel
BuildRequires:  gtk+2-devel

%description
ROSA Alternative GTK+ style for Qt

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean 
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plugins/styles/qgtkstylealt.so
%_kde_datadir/apps/kstyle/themes/qgtkstylealt.themerc

