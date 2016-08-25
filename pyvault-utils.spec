Name:         PyVault-utils
Version:      1.0
Release:      1%{?dist}
Summary:      Yet another implementation of Vault using pure Python (json and gnupg modules).
Packager:     Frantisek Kolacek <fkolacek@redhat.com>
Group:        Security
License:      GNU/GPL
URL:          https://github.com/fkolacek/PyVault
Source0:      https://github.com/fkolacek/PyVault/archive/PyVault-%{version}.tar.gz
BuildArch:    noarch
Requires:     PyVault zenity xclip dmenu bash-completion

%description
Bunch of utilities for making life with PyVault easier.

%prep
%setup -q -n PyVault-%{name}-%{version}

%clean
rm -rf %{buildroot}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/bash_completion.d/

install -m 0755 pyvault-get %{buildroot}/usr/local/bin/pyvault-get
install -m 0644 .bash_completion.d/pyvault %{buildroot}/etc/bash_completion.d/pyvault

%files
/usr/local/bin/pyvault-get
/etc/bash_completion.d/pyvault

%changelog
* Sun Aug 21 2016 Frantisek Kolacek <fkolacek@redhat.com> 1.0-1
--First repack
