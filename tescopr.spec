Name:           tescopr
Version:        1.0.0
Release:        1%{?dist}
Summary:        Program test sederhana

License:        MIT
URL:            https://github.com/se7uh/tescopr
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%global debug_package %{nil}

%description
Program sederhana yang menampilkan nama dan versi.

%prep
%autosetup

%build
gcc -o %{name} main.c

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Wed Mar 20 2024 Your Name <your.email@example.com> - 1.0.0-1
- Initial package