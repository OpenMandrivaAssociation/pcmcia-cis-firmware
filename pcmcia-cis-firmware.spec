%define old_name pcmcia-cs

Summary: PCMCIA CIS overrides
Name: pcmcia-cis-firmware
Version: 3.2.8
Release: %mkrel 1
Source0: http://pcmcia-cs.sourceforge.net/ftp/%{old_name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://pcmcia-cs.sf.net/
BuildArch: noarch


%description
This package contains PCMCIA "CIS" files (sort of "firmware"
overrides), needed for some PCMCIA cards to work properly.

%prep
%setup -q -n %{old_name}-%{version}

%build

%install
rm -rf %{buildroot}
install -d -m0755 %{buildroot}/lib/firmware
pushd etc/cis
for f in *.dat; do
  install -m0644 $f %{buildroot}/lib/firmware/${f%.dat}.cis
done
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/lib/firmware/*.cis


