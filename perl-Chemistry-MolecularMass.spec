#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Chemistry
%define	pnam	MolecularMass
Summary:	Chemistry::MolecularMass - Perl extension for calculating molecular mass of a chemical compound given its chemical formula.
Name:		perl-Chemistry-MolecularMass
Version:	0.1
Release:	1
License:	Perl Artistic Licence
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d0d56e49920ca0f18237ef81ef946ca6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chemistry::MolecularMass is an Object Oriented Perl module for calculating
molcular mass of chemical compounds implemented with Perl and C.
Molecular masses of elements stored in the module follow recommendations
of IUPAC (1995). The module includes elements from H(1) through
Uuu(113) and isotopes of hydrogen: deuterium and tritium. 

%prep
%setup -q -n %{pdir}/%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Chemistry/MolecularMass.pm
%{perl_vendorarch}/auto/Chemistry/MolecularMass/MolecularMass.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Chemistry/MolecularMass/MolecularMass.so
%{_mandir}/man3/*
