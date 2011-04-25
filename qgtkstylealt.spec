Name:		qgtkstylealt
Summary:	ROSA Alternative GTK+ style for Qt
Version:	0.1.1
Release:	%mkrel 1
Source0:	qgtkstylealt-%{version}.tar.gz
Group:		Graphical desktop/KDE
License:	GPLv3


Requires:       kdebase4-runtime qt4-common libgtk+2.0
BuildRequires:  libqt4-devel libgtk+2.0-devel

%description
ROSA Alternative GTK+ style for Qt

%prep
%setup -q

%build
cmake .
make

%install
%__rm -rf %{buildroot}

make DESTDIR=%{buildroot} install

%clean 
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plugins/styles/qgtkstylealt.so
%_kde_datadir/apps/kstyle/themes/qgtkstylealt.themerc

