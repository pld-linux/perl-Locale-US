#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	US
Summary:	Two letter codes for state identification in the United States and vice versa
Summary(pl.UTF-8):	Dwuliterowe kody do identyfikacji stanów w USA
Name:		perl-Locale-US
Version:	1.2
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Locale/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d748870d0b657f78d7ea044cbf35eacc
URL:		http://search.cpan.org/dist/Locale-US/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains a module which can be used to process USPS
two letter codes for states in the United States and surrounding
territories.

%description -l pl.UTF-8
Ten pakiet zawiera moduł służący do przetwarzania dwuliterowych kodów
USPS dla stanów USA i otaczających terytoriów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Locale/US.pm
%{perl_vendorlib}/Locale/kruft2codes.pl
%{_mandir}/man3/Locale::US.3pm*
