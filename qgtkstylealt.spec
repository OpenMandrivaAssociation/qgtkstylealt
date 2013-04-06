Name:		qgtkstylealt
Summary:	ROSA Alternative GTK+ style for Qt
Version:	0.1.2
Release:	2
Source0:	qgtkstylealt-%{version}.tar.gz
Group:		Graphical desktop/KDE
License:	GPLv3


Requires:       kdebase4-runtime qt4-common %{_lib}gtk+2.0_0
BuildRequires:  qt4-devel gtk2-devel kdebase4-devel kdebase4-workspace-devel

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


%changelog
* Thu Oct 25 2012 Dmitry Ashkadov <dmitry.ashkadov@rosalab.ru> 0.1.2-1
- Sources were updated to version 0.1.2: support of Drag&Drop for menus and toolbars

*Thu Apr 12 2012 akdengi <akdengi> 0.1.1-2
- update qstylehelper_p.h and qstylehelper.cpp from 4.8.x branch for propertly build

* Mon Apr 25 2011 Alex Burmashev <burmashev@mandriva.org> 0.1.1-1mdv2011.0
+ Revision: 658767
- fix
- fix
- import qgtkstylealt

  + Funda Wang <fwang@mandriva.org>
    - qt4 is not enough, as it is detecting kde in cmakelists.txt
    - rework spec file

