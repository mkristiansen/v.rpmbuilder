#!/bin/bash

# This is needed because we must sync 64 bit packages to 32 bit ones
#echo "provision.sh: Running yum update"
#sudo yum update -y
sudo yum groupinstall "Development Tools" -y

echo "provision.sh: Installing rpm creation pre-reqs"
sudo yum install rpm-build -y
sudo yum install rpmdevtools -y
sudo yum install createrepo -y

echo "provision.sh: Creating RPM directory structure"
rpmdev-setuptree
cp ~/rpmbuild/.rpmmacros ~/

rpmbuild -v -bb --clean rpmbuild/SPECS/tds_license.spec

cp rpmbuild/RPMS/x86_64/*.rpm /opt/ieu94897/Sites/repos/tds6.3.1/x86_64/
createrepo /opt/ieu94897/Sites/repos/tds6.3.1/x86_64/

