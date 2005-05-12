%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	JSON library for Ruby
Summary(pl):	Biblioteka JSON dla jêzyka Ruby
Name:		ruby-json
Version:	1.1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/json/%{name}-%{version}.tar.gz
# Source0-md5:	bdd95a1806ac08c965d225d0d7b1c49f
Source1:	setup.rb
URL:		http://sourceforge.net/projects/json/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON library for Ruby.

%description -l pl
Biblioteka JSON dla jêzyka Ruby.

%prep
%setup -q -n %{name}

%build
mkdir lib
mv json lib
install %{SOURCE1} setup.rb
ruby setup.rb config \
	--siterubyverdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/json
# Does not merge well with others.
%{ruby_ridir}/JSON
%{ruby_ridir}/*/*json*
