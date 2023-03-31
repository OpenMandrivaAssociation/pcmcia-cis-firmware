%define oname pcmcia-cs

Summary:	PCMCIA CIS overrides
Name:		pcmcia-cis-firmware
Version:	3.2.8
Release:	21
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://pcmcia-cs.sf.net/
Source0:	http://pcmcia-cs.sourceforge.net/ftp/%{oname}-%{version}.tar.bz2
BuildArch:	noarch

%description
This package contains PCMCIA "CIS" files (sort of "firmware"
overrides), needed for some PCMCIA cards to work properly.

%prep
%setup -qn %{oname}-%{version}

%build

%install
install -d -m0755 %{buildroot}/lib/firmware
pushd etc/cis
for f in *.dat; do
  install -m0644 $f %{buildroot}/lib/firmware/${f%.dat}.cis
done
popd

%files
/lib/firmware/*.cis

