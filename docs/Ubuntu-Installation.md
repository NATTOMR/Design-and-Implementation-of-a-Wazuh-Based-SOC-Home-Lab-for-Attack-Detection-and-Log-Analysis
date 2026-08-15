# Ubuntu Server 24.04 LTS Installation Guide

This document describes the complete installation, initial setup, and network configuration of the Ubuntu Server 24.04 LTS virtual machine hosting the Wazuh SIEM platform.

---

# Table of Contents

- Prerequisites
- Virtual Machine Hardware Specs
- Step-by-Step Installation
  - 1. VirtualBox Setup
  - 2. OS Installation
  - 3. Post-Install Updates
- Network Configuration
- Firewall Setup
- Verification
- Next Steps

---

# Prerequisites

- **Hypervisor**: Oracle VirtualBox (v7.0 or higher)
- **ISO Image**: `ubuntu-24.04-live-server-amd64.iso`
- **Network Mode**: VirtualBox NAT Network (subnet: `10.0.2.0/24`)

---

# Virtual Machine Hardware Specs

| Setting | Minimum Recommendation | Applied Setting |
| :--- | :--- | :--- |
| **Base RAM** | 4 GB | 4096 MB – 8192 MB |
| **Processors** | 2 Cores | 2 to 4 Cores |
| **Hard Disk** | 50 GB | 50 GB Dynamically Allocated VDI |
| **Network Adapter** | NAT Network | `10.0.2.15` |

---

# Step-by-Step Installation

### 1. VirtualBox Setup
1. Launch **Oracle VirtualBox** and select **New**.
2. Set Name: `Wazuh-Server-Ubuntu`, Type: `Linux`, Version: `Ubuntu (64-bit)`.
3. Allocate RAM and CPU resources.
4. Select **Create a Virtual Hard Disk Now** (50 GB size).
5. Attach the Ubuntu 24.04 ISO file to the virtual optical drive.

### 2. OS Installation
1. Start the VM and boot from ISO.
2. Select language, keyboard layout, and installation type (**Ubuntu Server**).
3. Accept default networking and proxy settings.
4. Partitioning: Select **Use an entire disk** and set up LVM.
5. Enter user profile information (`socadmin`).
6. Enable **Install OpenSSH server**.
7. Complete installation, reboot, and remove the ISO media.

### 3. Post-Install Updates
Log into the server terminal and run:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget net-tools ufw git
```

---

# Network Configuration

Check current network interfaces and IP addresses:

```bash
ip a
```

Verify connectivity to the host and external network:

```bash
ping -c 4 8.8.8.8
```

---

# Firewall Setup

Enable UFW firewall and allow required ports:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp     # SSH
sudo ufw allow 1514/tcp   # Wazuh Agent Log Stream
sudo ufw allow 1515/tcp   # Wazuh Agent Enrollment
sudo ufw allow 443/tcp    # Wazuh Dashboard HTTPS
sudo ufw enable
```

---

# Verification

Ensure services are running as expected:

```bash
sudo systemctl status ssh
sudo ufw status verbose
```

---

# Next Steps

After completing the Ubuntu Server setup, proceed to:
1. **[Wazuh Installation Guide](Wazuh-Installation.md)** to deploy Wazuh Manager, Indexer, and Dashboard.
2. **[Windows 11 Agent Installation](Windows11-Agent.md)** to connect victim endpoints.
