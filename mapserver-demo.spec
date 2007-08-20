Name:		mapserver-demo
Version:	3.5
Release:	%mkrel 2
Summary:	Demo Data for Mapserver
Source:		http://mapserver.gis.umn.edu/dist/itasca%{version}.tar.gz
Patch:		mapserver-demo-webserver-paths.patch
URL:		http://mapserver.gis.umn.edu/
License:	GPL
Group:		Sciences/Geosciences
Requires:	mapserver
BuildRequires:	ImageMagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Buildarch:	noarch

%description
MapServer is an  OpenSource development environment for building spatially 
enabled Internet applications. The software builds upon other popular 
OpenSource or freeware systems like Shapelib, FreeType, Proj.4, libTIFF, 
Perl and others.

This package provides the Mapserver demo data, and should be accessible
as http://localhost/mapserver/itasca on the machine it is installed on.

%prep
%setup -q -c
%patch -b .orig
find . -type d -name 'CVS' -exec rm -Rf {} \; >/dev/null 2>&1 ||:
for i in itasca/*/*.gif;do convert $i `echo $i|sed -e 's/gif/png/g'`;done
perl -pi -e 's/\.gif/\.png/g' itasca/demo.map
cp itasca/demo_init.html itasca/index.html

%build

%install
mkdir -p %{buildroot}/%{_var}/www/html/mapserver
cp -a itasca %{buildroot}/%{_var}/www/html/mapserver
find %{buildroot}/%{_var}/ -name '*.pl' -exec rm -f {} \;

%files
%defattr(-,root,root)
%{_var}/www/html/mapserver/*
#%doc INSTALL README HISTORY.TXT

%clean
rm -Rf %{buildroot}

