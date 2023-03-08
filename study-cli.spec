%define version 0.0.1
%define release 1

Name:           study-cli
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A command-line interface for studying
License:        GPL

URL:            https://github.com/study-cli/study-cli
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3-devel
Requires:       python3

%description
Study CLI is a command-line interface for studying.

%prep
%autosetup -p1

%build
python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%{python3_sitelib}/study_cli/
%{_bindir}/study-cli
