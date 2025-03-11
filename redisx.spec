%global upstream_version        1.0.0-rc2

Name:                   redisx
Version:                1.0.0~rc2
Release:                %autorelease
Summary:                An independent C/C++ Redis/Valkey client library and toolkit.
License:                Unlicense
URL:                    https://smithsonian.github.io/redisx
Source0:                https://github.com/Smithsonian/redisx/archive/refs/tags/v%{upstream_version}.tar.gz
Requires:               libxchange
Requires:               libomp
Requires:               openssl
Requires:               popt
Requires:               readline
Requires:               libbsd
BuildRequires:          gcc
BuildRequires:          libxchange-devel
BuildRequires:          libomp-devel
BuildRequires:          openssl-devel
BuildRequires:          popt-devel
BuildRequires:          readline-devel
BuildRequires:          libbsd-devel
BuildRequires:          sed
BuildRequires:          valkey
BuildRequires:          doxygen >= 1.9.0

%description

RedisX is a free, light-weight Redis client library for C/C++. As such, it 
should work with Redis forks / clones like Dragonfly or Valkey also. It 
supports both interactive and pipelined Redis queries, managing and processing 
subscriptions, atomic execution blocks, and LUA scripts loading. It can be 
used with multiple Redis servers simultaneously also. RedisX is free to use, 
in any way you like, without licensing restrictions.

%package devel
Summary:                C development files for the RedisX C/C++ library
Requires:               %{name}%{_isa} = %{version}-%{release}
Requires:               libxchange-devel
Requires:               libomp-devel
Requires:               openssl-devel
Requires:               popt-devel
Requires:               readline-devel
Requires:               libbsd-devel

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

# TODO simplify to one line with upstream changes...
make %{?_smp_mflags} shared
make tools
make local-dox

%check

# Just check that the client is functional
export LD_LIBRARY_PATH=$(pwd)/lib
bin/redisx-cli --help

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
%{_includedir}/*
%{_libdir}/libredisx.so

%files doc
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/redisx.tag
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/*.c

%changelog
%autochangelog

