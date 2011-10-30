%define         module launchpad-integration
Summary:	Python LaunchpadIntegration module
Summary(pl.UTF-8):	Moduł języka Python - LaunchpadIntegration
Name:		python-launchpad-integration
Version:	0.1.35
Release:	0.1
License:	GPL v3+
Group:		Libraries/Python
Source0:	https://launchpad.net/ubuntu/lucid/+source/launchpad-integration/0.1.35/+files/%{module}_%{version}.tar.gz
# Source0-md5:	542878a95ef5a6eef16a2cb0956899f2
URL:		https://launchpad.net/ubuntu/lucid/+source/launchpad-integration
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12
BuildRequires:	mono-csharp
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{module}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#######
