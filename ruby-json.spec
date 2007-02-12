Summary:	JSON library for Ruby
Summary(pl.UTF-8):   Biblioteka JSON dla języka Ruby
Name:		ruby-json
Version:	1.1
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/json/%{name}-%{version}.tar.gz
# Source0-md5:	bdd95a1806ac08c965d225d0d7b1c49f
Source1:	setup.rb
URL:		http://sourceforge.net/projects/json/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON library for Ruby.

%description -l pl.UTF-8
Biblioteka JSON dla języka Ruby.

%prep
%setup -q -n %{name}
mkdir lib
mv json lib
install %{SOURCE1} setup.rb

%build
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
