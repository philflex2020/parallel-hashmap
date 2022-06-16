%global __strip /bin/true # turn off binary stripping
%define debug_package %{nil} # do not preserve debug information

%define source %{_name}-%{_version}-%{_release}
%define bin_dir /usr/local/bin
%define lib_dir /usr/local/lib
%define include_dir /usr/local/include
%define systemd_dir /usr/lib/systemd/system
%define opt_dir /opt/flexgen/
%define node_dir /usr/lib/node_modules
%define go_dir /usr/lib/golang/src

Summary:    parallel-hashmap
License:    MIT License
Name:       %{_name}
Version:    %{_version}
Release:    %{_release}
Source:     %{source}.tar.gz
BuildRoot:  %{_topdir}
Provides:   libparhash.a()(64bit)

%description
Very fast, header-only/compiled, C++ logging library.

%prep
%setup -n %{source}

%build

%install

install --directory %{buildroot}%{include_dir}
install -m 0664 parallel-hashmap-1.34.tar.gz %{buildroot}%{include_dir}

%post
echo "unpacking include/parallel-hashmap-1.34/" 
tar -xzvf %{include_dir}/parallel-hashmap-1.34.tar.gz -C %{include_dir}
rm -rf %{include_dir}/parallel-hashmap-1.34.tar.gz

%postun
rm -rf %{include_dir}/parallel-hashmap-1.34

%clean
rm -rf %{buildroot}

%files
%{include_dir}/parallel-hashmap-1.34.tar.gz

%changelog