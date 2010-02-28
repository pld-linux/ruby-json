Summary:	JSON library for Ruby
Summary(pl.UTF-8):	Biblioteka JSON dla języka Ruby
Name:		ruby-json
Version:	1.1.9
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/json-%{version}.gem
# Source0-md5:	b29ddb63ba1c0d3a9ecdaf944df61157
URL:		http://json.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	setup.rb = 3.4.1
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-json-rubyforge
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON library for Ruby.

%description -l pl.UTF-8
Biblioteka JSON dla języka Ruby.

%prep
%setup -q -c 
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
install %{_datadir}/setup.rb .

%build
mv ext/json/ext/generator ext/json/generator
mv ext/json/ext/parser ext/json/parser
touch ext/json/{parser,generator}/MANIFEST

ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
#rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

#cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/json
%{ruby_rubylibdir}/json.rb
%dir %{ruby_archdir}/json
%attr(755,root,root) %{ruby_archdir}/json/generator.so
%attr(755,root,root) %{ruby_archdir}/json/parser.so
