# TODO: Name vs spec filename
Summary:	JSON library for Ruby
Summary(pl.UTF-8):	Biblioteka JSON dla języka Ruby
Name:		ruby-json-rubyforge
Version:	0.4.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/12676/json-%{version}.tgz
# Source0-md5:	be791c67c5d7b405c9f9f7dfd9475e45
URL:		http://json.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	setup.rb = 3.3.1
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON library for Ruby.

%description -l pl.UTF-8
Biblioteka JSON dla języka Ruby.

%prep
%setup -q -n json-%{version}
#mkdir lib
#mv json lib
install %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{_bindir}/*.rb
%{ruby_rubylibdir}/json
%{ruby_rubylibdir}/json.rb
# Does not merge well with others.
%{ruby_ridir}/JSON
%{ruby_ridir}/*/*json*
