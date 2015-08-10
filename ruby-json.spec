#
# Conditional build:
%bcond_with	tests		# build without tests

%define pkgname json
Summary:	JSON library for Ruby
Summary(pl.UTF-8):	Biblioteka JSON dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.8.1
Release:	2
License:	Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	d53582f76c34719aa815b0336beeb0a9
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q
cp -p %{_datadir}/setup.rb .

%build
%__gem_helper spec

%{__ruby} setup.rb config \
	--rbdir=%{ruby_vendorlibdir} \
	--sodir=%{ruby_vendorarchdir}

%{__ruby} setup.rb setup

rdoc -o rdoc lib
rdoc --ri -o ri lib/*
rm ri/created.rid
rm ri/cache.ri
# system libs
rm -r ri/{Class,Date,DateTime,Exception,Kernel} \
	ri/{Range,Regexp,Struct,Symbol,Time,BigDecimal,Complex,OpenStruct,Rational}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{ruby_ridir},%{ruby_rdocdir}}
%{__ruby} setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

rmdir $RPM_BUILD_ROOT%{ruby_vendorlibdir}/json/ext

# huh?
%{__rm} $RPM_BUILD_ROOT%{_datadir}/{example.json,index.html,prototype.js}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* TODO
%{ruby_vendorlibdir}/json
%{ruby_vendorlibdir}/json.rb
%dir %{ruby_vendorarchdir}/json
%dir %{ruby_vendorarchdir}/json/ext
%attr(755,root,root) %{ruby_vendorarchdir}/json/ext/generator.so
%attr(755,root,root) %{ruby_vendorarchdir}/json/ext/parser.so
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/JSON
