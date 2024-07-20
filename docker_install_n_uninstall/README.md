# docker_install_n_uninstall

# Docker Installation and Uninstallation

This directory contains scripts for installing and uninstalling Docker.
Note that this is for Docker CLI installation and not desktop
## Installation

To install Docker, run the following command:

```
./install.sh
```

This script will download and install the latest version of Docker on your system.

## Uninstallation

To uninstall Docker, run the following command:

```
./uninstall.sh
```

This script will remove Docker from your system.

Please note that these scripts are specific to this directory and should be used accordingly.

## General System Requirements

To install Docker Desktop successfully, your Linux host must meet the following general requirements:

- 64-bit kernel and CPU support for virtualization.
- KVM virtualization support. Follow the KVM virtualization support instructions to check if the KVM kernel modules are enabled and how to provide access to the KVM device.
- QEMU must be version 5.2 or later. We recommend upgrading to the latest version.
- systemd init system.
- Gnome, KDE, or MATE Desktop environment.
    - For many Linux distros, the Gnome environment does not support tray icons. To add support for tray icons, you need to install a Gnome extension. For example, AppIndicator.

- At least 4 GB of RAM.
- Enable configuring ID mapping in user namespaces, see File sharing.
- Recommended: Initialize pass for credentials management.