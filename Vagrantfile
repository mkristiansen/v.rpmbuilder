# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

# Configuration parameters
ram = 2048                            # Ram in MB for each VM
secondaryStorage = 80                 # Size in GB for the secondary virtual HDD
privateNetworkIp = "10.10.10.50"      # IP for the private network between VMs

# Do not edit below this line
# --------------------------------------------------------------
privateSubnet = privateNetworkIp.split(".")[0...3].join(".")
privateStartingIp = privateNetworkIp.split(".")[3].to_i

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Choose whether to use vaggrant-vbguest plugin to update VirtualBox Guest Additions.
  if Vagrant.has_plugin?("vagrant-vbguest")  
    config.vbguest.auto_update = false
  end

  # Use vaggrant-cachier - Configure cached packages to be shared between instances of the same base box.
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end

  config.vm.box = "parallels/centos-6.6"
  config.vm.box_url = "localhost"

  config.vm.define "rpmbuilder" do |master|
    master.vm.network :public_network
    master.vm.network :private_network, ip: "#{privateSubnet}.#{privateStartingIp}"
    master.vm.hostname = "rpmbuilder"
    master.vm.synced_folder "./rpmbuild", "/home/vagrant/rpmbuild"
    master.vm.synced_folder "~/Sites", "/opt/ieu94897/Sites"

    master.vm.provision :shell, path: "provision.sh", privileged: false
  end
end