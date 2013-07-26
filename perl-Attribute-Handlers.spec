%define upstream_name    Attribute-Handlers
%define upstream_version 0.93

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.93
Release:	1

Summary:	Simpler definition of attribute handlers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Attribute/Attribute-Handlers-0.93.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module, when inherited by a package, allows that package's class to
define attribute handler subroutines for specific attributes. Variables
and subroutines subsequently defined in that package, or in packages
derived from that package may be given attributes with the same names as
the attribute handler subroutines, which will then be called at the end
of the compilation phase (i.e. in a `CHECK' block).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes README

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Attribute
%{_mandir}/*/*

%changelog
* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.910.0-1mdv2011.0
+ Revision: 677319
- update to new version 0.91

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.880.0-3mdv2011.0
+ Revision: 597090
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.880.0-2mdv2011.0
+ Revision: 562417
- rebuild

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.880.0-1mdv2011.0
+ Revision: 532135
- update to 0.88

* Tue Sep 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.870.0-1mdv2010.0
+ Revision: 447131
- update to 0.87

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.860.0-2mdv2010.0
+ Revision: 420976
- rebuild

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.860.0-1mdv2010.0
+ Revision: 416945
- update to 0.86

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.850.0-1mdv2010.0
+ Revision: 402982
- rebuild using %%perl_convert_version

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.85-1mdv2010.0
+ Revision: 386995
- update to new version 0.85

* Thu Jun 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-1mdv2010.0
+ Revision: 385207
- update to new version 0.84

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.83-1mdv2009.1
+ Revision: 354877
- update to new version 0.83

* Thu Mar 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.82-1mdv2009.1
+ Revision: 354393
- update to new version 0.82

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.81-1mdv2009.1
+ Revision: 302890
- update to new version 0.81

* Wed Oct 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.80-1mdv2009.1
+ Revision: 298176
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.78-3mdv2009.0
+ Revision: 241151
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 14 2007 Oden Eriksson <oeriksson@mandriva.com> 0.78-1mdv2008.0
+ Revision: 26669
- Import perl-Attribute-Handlers



* Mon May 14 2007 Oden Eriksson <oeriksson@mandriva.com> 0.78-1mdv2007.1
- initial Mandriva package 

