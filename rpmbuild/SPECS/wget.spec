# This is a sample spec file for wget

%define _topdir	 	/home/vagrant/rpmbuild
%define name			wget 
%define release		1
%define version 	1.16.1
%define buildroot %{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary: 		GNU wget
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/usr/local
Group: 			Development/Tools

%description
The GNU wget program downloads files from the Internet using the command-line.

%prep
%setup -q

%build
./configure --with-ssl=openssl
make clean
make

%install
make install prefix=$RPM_BUILD_ROOT/usr/local

%files
%defattr(-,root,root)
/usr/local/bin/wget

%doc %attr(0444,root,root) /usr/local/share/man/man1/wget.1
/usr/local/etc/wgetrc
/usr/local/share/locale/
/usr/local/share/info/dir
/usr/local/share/info/wget.info