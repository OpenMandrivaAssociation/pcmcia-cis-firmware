%define old_name pcmcia-cs

Summary: PCMCIA CIS overrides
Name: pcmcia-cis-firmware
Version: 3.2.8
Release: 9
Source0: http://pcmcia-cs.sourceforge.net/ftp/%{old_name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://pcmcia-cs.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.8-6mdv2011.0
+ Revision: 667001
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.8-5mdv2011.0
+ Revision: 607083
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.8-4mdv2010.1
+ Revision: 523606
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.2.8-3mdv2010.0
+ Revision: 426380
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.2.8-2mdv2009.0
+ Revision: 223449
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 3.2.8-1mdv2008.1
+ Revision: 131060
- kill re-definition of %%buildroot on Pixel's request


(none)
