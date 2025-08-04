Vagrant.configure("2") do |c|
  c.vm.box = "ubuntu/focal64"
  c.vm.network "public_network"
  c.vm.provision "shell", inline: <<-S
    apt-get update && apt-get install -y aircrack-ng
  S
end