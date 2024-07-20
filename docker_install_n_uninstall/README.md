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




## Step-by-Step Guide to Install Docker Desktop on Linux

1. **Check System Requirements**: Before installing Docker Desktop, ensure that your Linux host meets the following requirements:
    - 64-bit kernel and CPU support for virtualization.
    - KVM virtualization support. You can check if the KVM kernel modules are enabled and how to provide access to the KVM device by following the KVM virtualization support instructions.
    - QEMU version 5.2 or later. It is recommended to upgrade to the latest version.
    - systemd init system.
    - Gnome, KDE, or MATE Desktop environment. Note that for some Linux distros, the Gnome environment may not support tray icons. To add support for tray icons, you can install a Gnome extension like AppIndicator.
    - At least 4 GB of RAM.
    - Enable configuring ID mapping in user namespaces (see File sharing).
    - Recommended: Initialize pass for credentials management.

2. **Download and Install Docker Desktop**: Follow these steps to download and install Docker Desktop on your Linux distribution:
    - Download the correct package for your Linux distribution (e.g., .deb for Ubuntu, .rpm for Red Hat Enterprise Linux) from the Docker website.
    - Install the downloaded package using the corresponding package manager for your distribution.
    - By default, Docker Desktop is installed at `/opt/docker-desktop`.

3. **Start Docker Desktop**: Once installed, you can start Docker Desktop by following these steps:
    - Open your Applications menu in the Gnome/KDE Desktop environment.
    - Search for "Docker Desktop" and select it.
    - Docker Desktop will start, and the Docker menu (whale menu) will appear.
    - Accept the Docker Subscription Service Agreement to continue. Docker Desktop will start after accepting the terms. Note that Docker Desktop will not run if you do not agree to the terms.
 