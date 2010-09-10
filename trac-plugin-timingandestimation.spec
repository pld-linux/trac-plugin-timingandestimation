%define		trac_ver	0.12
%define		plugin		timingandestimation
Summary:	Trac plugin to track hours spent on tickets
Name:		trac-plugin-timingandestimation
Version:	1.0.6
Release:	0.2
License:	BSD-like
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/timingandestimationplugin/branches/trac0.12?old_path=/&filename=timingandestimationplugin/branches/trac0.12&format=zip
# Source0-md5:	d2ed4beba5e99d1758e7e9c57cb74f5f
URL:		http://trac-hacks.org/wiki/TimingAndEstimationPlugin
BuildRequires:	python-devel
BuildRequires:	unzip
Requires:	python >= 1:2.4
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of this plugin is to help keep trac of hours worked on
tickets.

%prep
%setup -qc

%build
cd %{plugin}plugin/branches/trac%{trac_ver}
%{__python} setup.py build
%{__python} setup.py egg_info

ver=$(awk '$1 == "Version:" {print $2}' *.egg-info/PKG-INFO)
test "$ver" = %{version}

%install
rm -rf $RPM_BUILD_ROOT
cd %{plugin}plugin/branches/trac%{trac_ver}
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
trac-enableplugin "trac%{plugin}.*"

if [ "$1" = "1" ]; then
	%banner -e %{name} <<-'EOF'
TODO
EOF
fi

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{plugin}plugin
%{py_sitescriptdir}/*-*.egg-info
