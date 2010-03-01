%define pkgname json
Summary:	JSON library for Ruby
Summary(pl.UTF-8):	Biblioteka JSON dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.1.9
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	b29ddb63ba1c0d3a9ecdaf944df61157
URL:		http://json.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	setup.rb >= 3.4.1
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-json-rubyforge
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON library for Ruby.

%description -l pl.UTF-8
Biblioteka JSON dla języka Ruby.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c 
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}

install %{_datadir}/setup.rb .

%build
mv ext/json/ext/generator ext/json/generator
mv ext/json/ext/parser ext/json/parser
touch ext/json/{parser,generator}/MANIFEST

ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc lib
rdoc --ri -o ri lib/*
rm ri/created.rid
rm -r ri/{Class,Date,DateTime,Enumerable,Exception,Kernel,Object} \
	ri/{Range,Regexp,Struct,Symbol,Time}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/json
%{ruby_rubylibdir}/json.rb
%dir %{ruby_archdir}/json
%attr(755,root,root) %{ruby_archdir}/json/generator.so
%attr(755,root,root) %{ruby_archdir}/json/parser.so

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/JSON
