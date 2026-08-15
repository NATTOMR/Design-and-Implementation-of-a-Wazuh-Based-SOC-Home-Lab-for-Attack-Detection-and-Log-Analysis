# 🐧 Ubuntu Server 24.04 LTS Installation & Setup

This document describes the deployment, network configuration, and server preparation of the **Ubuntu Server 24.04 LTS** virtual machine. In this SOC Home Lab, the Ubuntu Server acts as the core SIEM host running the Wazuh Manager, Wazuh Indexer, and Wazuh Dashboard.

---

# Table of Contents

- Overview
- Lab Architecture Role
- System Requirements
- Step-by-Step Installation
  - 1. Create VirtualBox Machine
  - 2. Install Ubuntu Server
  - 3. Post-Installation System Update
- Network & Firewall Configuration
  - 1. Verify IP Address
  - 2. Firewall Port Configuration (UFW)
- Verification Checklist
- Screenshots
- Next Steps

---

# Overview

The Ubuntu Server host is the central nervous system of the SOC Home Lab. It receives security telemetry from endpoints (Windows 11 with Sysmon), parses logs through the decoder and rules engine, indexes security events, and presents the security alerts via the web-based Wazuh Dashboard.

---

# Lab Architecture Role

| Component | Specification |
| :--- | :--- |
| **Operating System** | Ubuntu Server 24.04 LTS (64-bit) |
| **Role** | SIEM Server (Wazuh Manager, Indexer, Dashboard) |
| **Default IP** | `10.0.2.15` (VirtualBox NAT Network) |
| **Services Running** | OpenSSH (`22`), Wazuh Agent Comm (`1514`), Agent Reg (`1515`), Dashboard (`443`) |

---

# System Requirements

Before creating the Virtual Machine in VirtualBox, ensure the host machine meets these minimum resource requirements:

- **RAM**: 4 GB minimum (8 GB recommended for optimal Elasticsearch/Indexer performance)
- **Processors**: 2 to 4 CPU Cores
- **Storage**: 50 GB Dynamically Allocated Storage
- **Network Mode**: VirtualBox NAT Network (or Bridged Adapter)

---

# Step-by-Step Installation

### 1. Create VirtualBox Machine
1. Open **Oracle VirtualBox** and click **New**.
2. Name the VM: `Wazuh-Server-Ubuntu`.
3. Select Type: `Linux`, Version: `Ubuntu (64-bit)`.
4. Allocate Base Memory (**4096 MB** or **8192 MB**) and **2–4 CPUs**.
5. Create a Virtual Hard Disk: **50 GB** (VDI, Dynamically allocated).
6. Under VM **Settings ➔ Network**, set Adapter 1 to **NAT Network**.

### 2. Install Ubuntu Server
1. Mount the `ubuntu-24.04-live-server-amd64.iso` in the virtual optical drive.
2. Start the VM and choose **Try or Install Ubuntu Server**.
3. Select your language, keyboard layout, and choose **Ubuntu Server (default)** installation.
4. Configure network interface (DHCP or static IP in the `10.0.2.0/24` range).
5. Partition storage: Choose **Use an entire disk** (LVM enabled).
6. Profile setup:
   - Your name: `socadmin`
   - Server name: `wazuh-server`
   - Username: `socadmin`
   - Password: `<Secure_Password>`
7. SSH Setup: Check **Install OpenSSH server**.
8. Complete installation, unmount the ISO, and reboot the system.

### 3. Post-Installation System Update
Log into the server terminal via console or SSH and update all system packages:

```bash
sudo apt update && sudo apt upgrade -y
```

Install essential utility packages:
```bash
sudo apt install -y curl wget net-tools ufw git tar software-properties-common
```

---

# Network & Firewall Configuration

### 1. Verify IP Address
Display system IP details:
```bash
ip a
```
*Take note of the assigned IP address (e.g., `10.0.2.15`).*

### 2. Firewall Port Configuration (UFW)
Configure Uncomplicated Firewall (UFW) to allow necessary communication ports for Wazuh management and endpoint agents:

```bash
# Allow SSH for remote terminal access
sudo ufw allow 22/tcp

# Allow Wazuh Agent communication
sudo ufw allow 1514/tcp

# Allow Wazuh Agent registration
sudo ufw allow 1515/tcp

# Allow Wazuh Dashboard HTTPS web access
sudo ufw allow 443/tcp

# Enable Firewall
sudo ufw enable
```

Verify firewall status:
```bash
sudo ufw status verbose
```

---

# Verification Checklist

- [x] Ubuntu Server 24.04 LTS installed cleanly
- [x] System updated with `apt update && apt upgrade`
- [x] OpenSSH service active and listening on port 22
- [x] UFW firewall configured with ports 22, 1514, 1515, and 443
- [x] Connectivity tested via `ping` to Windows victim VM (`10.0.2.20`) and Kali VM (`10.0.2.30`)

---

# Screenshots

Capture and save the following screenshots in the [`screenshots/`](../screenshots/) directory:
1. `04-ubuntu-installation.png`: Ubuntu Server ISO boot & installation screen.
2. `05-ubuntu-login.png`: Successful command-line login prompt.
3. `06-system-update.png`: Running `sudo apt update && sudo apt upgrade` output.

---

# Next Steps

Once the Ubuntu Server is installed and configured, proceed to deploy the Wazuh SIEM stack using the **[Wazuh Installation Guide](../wazuh/README.md)** or **[docs/Wazuh-Installation.md](../docs/Wazuh-Installation.md)**.
