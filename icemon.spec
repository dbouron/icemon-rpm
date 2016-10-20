Name:           icemon
Version:        3.0.1
Release:        2%{?dist}
Summary:        Icecream GUI monitor

Group:          Development/Tools
License:        GPLv2+
URL:            https://github.com/icecc/%{name}
Source0:        https://github.com/icecc/%{name}/archive/v%{version}.tar.gz
Patch1:         0001-Fix-man-generation-bug-using-db2x_docbook2man.patch

BuildRequires:  qt5-qtbase-devel >= 5.2.0
BuildRequires:  qt5-qtbase-gui
BuildRequires:  qtsinglecoreapplication-qt5-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  lzo-devel
BuildRequires:  icecream-devel
BuildRequires:  cmake
BuildRequires:  docbook2X
BuildRequires:  doxygen
BuildRequires:  graphviz

%description
Icemon is an Icecream GUI monitor which provide scheduler workload
dispatching.

%prep
%autosetup

%build
mkdir -p build
cd build

%cmake -DCMAKE_BUILD_TYPE=Release ..

make %{?_smp_mflags}

%install

cd build
%make_install

%files
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man*/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz

%changelog
* Thu Oct 20 2016 Dimitri Bouron <bouron.d@gmail.com> - 3.0.1-2
- Fix manual generation

* Thu Sep 22 2016 Dimitri Bouron <bouron.d@gmail.com> - 3.0.1-1
- Initial spec file
