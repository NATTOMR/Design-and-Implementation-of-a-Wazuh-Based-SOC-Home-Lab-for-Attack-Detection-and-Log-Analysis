# 🐉 Kali Linux Attack Simulation

This directory contains resources and operational procedures for executing controlled attack simulations from the **Kali Linux Virtual Machine** against the monitored Windows 11 endpoint.

---

## 📖 Key Documentation

- **[Kali Attack Simulation Guide](../docs/Kali-Attack-Simulation.md)**: Full walkthrough of network discovery, port scanning, service enumeration, OS detection, and brute-force simulations.

---

## 🚀 Simulated Attack Vectors & Commands

### 1. Network Discovery & Host Sweeping
Identify active hosts on the VirtualBox NAT network (`10.0.2.0/24`):
```bash
nmap -sn 10.0.2.0/24
```

### 2. TCP Port Scanning & Service Enumeration
Scan open ports and discover active service versions on the Windows endpoint (`10.0.2.20`):
```bash
# TCP SYN Stealth Scan
nmap -sS 10.0.2.20

# Service & Version Detection
nmap -sV 10.0.2.20

# Aggressive Scan (OS, Version, Scripts, Traceroute)
sudo nmap -A 10.0.2.20
```

### 3. Password Attacks & Brute Force Simulation
Simulate authentication failures using Hydra against RDP or SMB:
```bash
hydra -l administrator -P passwords.txt rdp://10.0.2.20
```

### 4. Reverse Shell & Netcat Connectivity Test
Test network listener connection:
```bash
nc -lvnp 4444
```

---

## 📊 Verification Matrix

Each attack executed on Kali Linux is tracked across Windows Event Logs, Sysmon telemetry, and Wazuh Dashboard alerts. Refer to [Kali-Attack-Simulation.md](../docs/Kali-Attack-Simulation.md) for full execution logs and screenshots.
