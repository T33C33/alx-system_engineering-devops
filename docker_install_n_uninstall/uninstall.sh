#!/usr/bin/env bash

# Stop and remove all Docker containers
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)

# Uninstall Docker
sudo apt-get purge -y docker-engine docker docker.io docker-ce docker-ce-cli
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce

# Remove Docker data
sudo rm -rf /var/lib/docker

# Remove Docker configuration files
sudo rm -rf /etc/docker
sudo rm -f /etc/default/docker
sudo rm -f /etc/init.d/docker
sudo rm -f /etc/systemd/system/docker.service
sudo rm -f /etc/systemd/system/multi-user.target.wants/docker.service

# Verify removal
if ! command -v docker &> /dev/null; then
    echo "Docker has been successfully uninstalled."
else
    echo "Docker uninstallation failed."
fi