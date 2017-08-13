Name:      datadog-repo
Version:    0.1 
Release:    1
Summary:    DataDog repo

Group:  DataDog
License:    APL
Source0:    datadog.repo
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:     noarch

%description
DataDog repo

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT


%files
%config(noreplace) /etc/yum.repos.d/*

%changelog
