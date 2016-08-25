#%global         commit          1be2d2afdcb0313831be3274a2388a551fb145a8
#%global         githash         %(c=%{commit}; echo ${c:0:7})
#Source:         https://github.com/tista500/%{name}/archive/%{commit}/%{name}-v%{version}-%{githash}.ta
Name:         PyVault
Version:      1.0
Release:      1%{?dist}
Summary:      Yet another implementation of Vault using pure Python (json and gnupg modules).
Packager:     Frantisek Kolacek <fkolacek@redhat.com>
Group:        Security
License:      GNU/GPL
URL:          https://github.com/fkolacek/%{name}
Source0:      https://github.com/fkolacek/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:    noarch
Requires:     python2-gnupg zenity xclip dmenu

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
mkdir -p %{buildroot}/usr/local/share/man/man1
mkdir -p %{buildroot}/etc/bash_completion.d/

install -m 0755 pyvault %{buildroot}/usr/local/bin/pyvault
install -m 0755 pyvault-get %{buildroot}/usr/local/bin/pyvault-get
install -m 0755 .bash_completion.d/pyvault %{buildroot}/etc/bash_completion.d/pyvault
#install pyvault.1 %{buildroot}/usr/local/share/man/man1/pyvault.1

%files
#%doc /usr/local/share/man/man1/pyvault.1
/usr/local/bin/pyvault
/usr/local/bin/pyvault-get
/etc/bash_completion.d/pyvault

%changelog
* Sun Aug 21 2016 Frantisek Kolacek <fkolacek@redhat.com> 1.0-1
--First repack
