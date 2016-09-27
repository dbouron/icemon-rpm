Name:           icemon
Version:        3.0.1
Release:        1%{?dist}
Summary:        Icecream GUI monitor

Group:          Development/Tools
License:        GPLv2+
URL:            https://github.com/icecc/%{name}
Source0:        https://github.com/icecc/archive/v%{version}.tar.gz

BuildRequires:  qt5-qtbase-devel >= 5.2.0
BuildRequires:  qt5-qtbase-gui >= 5.6.1
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
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz

%changelog
* Thu Sep 22 2016 Dimitri Bouron <bouron.d@gmail.com> - 3.0.1-1
- Initial spec file
