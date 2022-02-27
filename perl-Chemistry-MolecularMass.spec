#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Chemistry
%define		pnam	MolecularMass
Summary:	Chemistry::MolecularMass - calculating molecular mass of a chemical compound given its chemical formula
Summary(pl.UTF-8):	Chemistry::MolecularMass - obliczanie masy cząsteczkowej związków zadanych wzorem chemicznym
Name:		perl-Chemistry-MolecularMass
Version:	0.1
Release:	15
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d0d56e49920ca0f18237ef81ef946ca6
URL:		http://search.cpan.org/dist/Chemistry-MolecularMass/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chemistry::MolecularMass is an Object Oriented Perl module for
calculating molecular mass of chemical compounds implemented with Perl
and C. Molecular masses of elements stored in the module follow
recommendations of IUPAC (1995). The module includes elements from
H(1) through Uuu(113) and isotopes of hydrogen: deuterium and tritium.

%description -l pl.UTF-8
Chemistry::MolecularMass to obiektowo zorientowany moduł Perla do
obliczania masy cząsteczkowej związków chemicznych zaimplementowany w
Perlu i C. Masy cząsteczkowe pierwiastków są zapisane w module zgodnie
z zaleceniami IUPAC (1995). Moduł zawiera pierwiastki od H(1) do
Uuu(113) oraz izotopy wodoru: deuter i tryt.

%prep
%setup -q -n %{pdir}/%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
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
%dir %{perl_vendorarch}/auto/Chemistry/MolecularMass
%attr(755,root,root) %{perl_vendorarch}/auto/Chemistry/MolecularMass/MolecularMass.so
%{_mandir}/man3/*
