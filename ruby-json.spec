#
# Conditional build:
%bcond_with	tests		# build without tests

%define pkgname json
Summary:	JSON library for Ruby
Summary(pl.UTF-8):	Biblioteka JSON dla języka Ruby
Name:		ruby-%{pkgname}
Version:	2.19.2
Release:	1
License:	Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	8b15a88cd3af9b3ac5882c0dfaf3f840
URL:		http://flori.github.com/json
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
%if %{with tests}
BuildRequires:	ruby-permutation
BuildRequires:	ruby-sdoc < 0.4
BuildRequires:	ruby-sdoc >= 0.3.16
%endif
Obsoletes:	ruby-json-rubyforge
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a JSON implementation as a Ruby extension in C.

%description -l pl.UTF-8
Biblioteka JSON dla języka Ruby.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4
BuildArch:	noarch

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby
BuildArch:	noarch

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

cd ext/json/ext/generator
%{__ruby} extconf.rb
%{__make}
cd ../parser
%{__ruby} extconf.rb
%{__make}
cd ../../../..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_vendorarchdir}/json/ext,%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
install -p ext/json/ext/generator/generator.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}/json/ext
install -p ext/json/ext/parser/parser.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}/json/ext

cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md README.md COPYING BSDL LEGAL
%{ruby_vendorlibdir}/json
%{ruby_vendorlibdir}/json.rb
%dir %{ruby_vendorarchdir}/json
%dir %{ruby_vendorarchdir}/json/ext
%attr(755,root,root) %{ruby_vendorarchdir}/json/ext/generator.so
%attr(755,root,root) %{ruby_vendorarchdir}/json/ext/parser.so
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

#%files rdoc
#%defattr(644,root,root,755)
#%{ruby_rdocdir}/%{name}-%{version}

#%files ri
#%defattr(644,root,root,755)
#%{ruby_ridir}/JSON
