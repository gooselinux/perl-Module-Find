Name:           perl-Module-Find
Version:        0.08
Release:        3%{?dist}
Summary:        Find and use installed modules in a (sub)category

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Module-Find/
Source0:        http://www.cpan.org/authors/id/C/CR/CRENZ/Module-Find-%{version}.tar.gz
Patch0:         perl-Module-Find-changes.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  %{_bindir}/iconv
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Module::Find lets you find and use modules in categories. This can be very
useful for auto-detecting driver or plugin modules. You can differentiate
between looking in the category itself or in all subcategories.


%prep
%setup -q -n Module-Find-%{version}
%patch0 -p1

%{_bindir}/iconv -f iso8859-1 -t utf8 -o Changes.new Changes
mv Changes.new Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -empty -exec rmdir {} ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README examples/
%{perl_vendorlib}/Module/
%{_mandir}/man3/*.3pm*


%changelog
* Tue Feb 16 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.08-3
- make rpmlint happy
- Related: rhbz#543948

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-2
- rebuild against perl 5.10.1

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-1
- new upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 02 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.06-1
- update to 0.06
- add examples/

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-2
- rebuild for new perl

* Tue Dec 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-1
- First build.
