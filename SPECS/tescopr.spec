Name:           tescopr
Version:        1.0.0
Release:        1%{?dist}
Summary:        Program test sederhana

License:        MIT
URL:            http://example.com/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

# Tambahkan baris ini untuk menonaktifkan debug package
%global debug_package %{nil}

%description
Program sederhana yang menampilkan nama dan versi.

%prep
%setup -q

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