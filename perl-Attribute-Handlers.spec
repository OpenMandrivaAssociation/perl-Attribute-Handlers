%define module Attribute-Handlers
%define name    perl-%{module}
%define version 0.83
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:	Simpler definition of attribute handlers
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Attribute/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module, when inherited by a package, allows that package's class to
define attribute handler subroutines for specific attributes. Variables
and subroutines subsequently defined in that package, or in packages
derived from that package may be given attributes with the same names as
the attribute handler subroutines, which will then be called at the end
of the compilation phase (i.e. in a `CHECK' block).

%prep
%setup -q -n %{module}-%{version} 
chmod 644 Changes README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Attribute
%{_mandir}/*/*
