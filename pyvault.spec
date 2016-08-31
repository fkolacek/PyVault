Name:         PyVault
Version:      1.2
Release:      1%{?dist}
Summary:      Yet another implementation of Vault using pure Python (json and gnupg modules).
Packager:     Frantisek Kolacek <fkolacek@redhat.com>
Group:        Security
License:      GNU/GPL
URL:          https://github.com/fkolacek/PyVault
Source0:      https://github.com/fkolacek/PyVault/archive/PyVault-%{version}.tar.gz
BuildArch:    noarch
Requires:     python2-gnupg

%description
Yet another implementation of Vault using pure Python (json and gnupg modules).

%prep
%setup -q -n PyVault-%{name}-%{version}

%clean
rm -rf %{buildroot}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin

install -m 0755 pyvault %{buildroot}/usr/local/bin/pyvault
#install pyvault.1 %{buildroot}/usr/local/share/man/man1/pyvault.1

%files
#%doc /usr/local/share/man/man1/pyvault.1
/usr/local/bin/pyvault

%changelog
* Tue Aug 30 2016 Frantisek Kolacek <fkolacek@redhat.com> 1.1-1
--Added support for interactive shell
* Sun Aug 21 2016 Frantisek Kolacek <fkolacek@redhat.com> 1.0-1
--First repack
