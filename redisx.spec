%global upstream_version        1.0.1-rc2

Name:                   redisx
Version:                1.0.1~rc2
Release:                %autorelease
Summary:                An independent C/C++ Redis/Valkey client library and toolkit
License:                Unlicense
URL:                    https://smithsonian.github.io/redisx
Source0:                https://github.com/Smithsonian/redisx/archive/refs/tags/v%{upstream_version}.tar.gz
Requires:		libxchange%{_isa} >= 1.0.1
Requires:               openssl%{_isa}
Requires:               popt%{_isa}
Requires:               readline%{_isa}
BuildRequires:          gcc
BuildRequires:          sed
BuildRequires:          doxygen >= 1.9.0
BuildRequires:          libxchange-devel%{_isa} >= 1.0.1
BuildRequires:          libomp-devel%{_isa}
BuildRequires:          openssl-devel%{_isa}
BuildRequires:          popt-devel%{_isa}
BuildRequires:          readline-devel%{_isa}
BuildRequires:          libbsd-devel%{_isa}

%description

RedisX is a free, light-weight Redis / Valkey client library for C/C++. It 
supports both interactive and batch Redis queries, managing and processing 
subscriptions, atomic execution blocks, and LUA script loading. It can be used 
with multiple Redis servers simultaneously also. RedisX is free to use, in any 
way you like, without licensing restrictions.

%package devel
Summary:                C development files for the RedisX C/C++ library
Requires:               %{name}%{_isa} = %{version}-%{release}
Requires:               libxchange-devel%{_isa} >= 1.0.1
Requires:               libomp-devel%{_isa}
Requires:               openssl-devel%{_isa}
Requires:               popt-devel%{_isa}
Requires:               readline-devel%{_isa}
Requires:               libbsd-devel%{_isa}

%description devel
This sub-package provides C headers and non-versioned shared library symbolic 
links for the RedisX C/C++ library.

%package doc
Summary:                Documentation for the RedisX C/C++ library
BuildArch:              noarch

%description doc
This package provides HTML documentation and examples for the RedisX C/C++ 
library. The HTML API documentation can also be used with the Eclipse IDE.

%prep
%setup -q -n redisx-%{upstream_version}

%build

make %{?_smp_mflags}

%check

export LD_LIBRARY_PATH=$(pwd)/lib
make test

%install

make DESTDIR=%{buildroot} libdir=%{_libdir} install

%files
%license LICENSE
%doc CHANGELOG.md
%{_libdir}/lib%{name}.so.1{,.*}
%{_bindir}/%{name}-cli
%{_mandir}/man1/%{name}-cli.1.gz

%files devel
%doc CONTRIBUTING.md
%doc examples/*
%{_includedir}/*
%{_libdir}/libredisx.so

%files doc
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/redisx.tag
%doc %{_docdir}/%{name}/html

%changelog
%autochangelog

