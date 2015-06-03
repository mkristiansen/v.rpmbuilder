# This is a sample spec file for tds_license

%define _topdir	 	/home/vagrant/rpmbuild
%define name		isds_license
%define release		0
%define version 	0.1.2
%define buildroot %{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary: 		ISDS License
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source0: 		license.tar.gz
Prefix: 		/usr/local
Group: 			ISDS
Requires:		ksh

%description
Provides and accepts license file for IBM Security Director Server

#%clean
#rm -rf %{buildroot}

%prep
%setup -q -n license

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/isds/license
mv * %{buildroot}/usr/local/isds/license

%post
/usr/local/isds/license/idsLicense -q

%files
%defattr(-,root,root)
%dir /usr/local/isds/license
/usr/local/isds/license/*
