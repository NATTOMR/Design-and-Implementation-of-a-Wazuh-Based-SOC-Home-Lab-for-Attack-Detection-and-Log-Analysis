# Kali Linux Attack Simulation

This document describes the attack simulations performed from the Kali Linux virtual machine against the Windows 11 endpoint. The objective is to generate security events that are collected by the Wazuh Agent and analyzed by the Wazuh SIEM platform.

---

# Table of Contents

- Introduction
- Lab Environment
- Network Verification
- Attack Scenarios
- Detection in Wazuh
- MITRE ATT&CK Mapping
- Screenshots
- Conclusion

---

# Introduction

The Kali Linux virtual machine acts as the attacker in this SOC Home Lab.

Several common attacks are executed to evaluate Wazuh's detection capabilities and verify that security events are successfully collected and analyzed.

---

# Lab Environment

| Machine | Operating System | Role |
|----------|------------------|------|
| Ubuntu Server | Ubuntu Server 24.04 LTS | Wazuh Server |
| Windows 11 | Windows 11 Pro | Victim |
| Kali Linux | Kali Linux | Attacker |

---

# Verify Network Connectivity

Before beginning the attacks, verify communication.

## Find Kali IP

```bash
ip a
```

---

## Ping Windows

```bash
ping <WINDOWS_IP>
```

Example

```bash
ping 10.0.2.20
```

---

## Ping Wazuh Server

```bash
ping <SERVER_IP>
```

Example

```bash
ping 10.0.2.15
```

---

# Attack Scenario 1

# Network Discovery

Identify active hosts.

```bash
nmap -sn <NETWORK>
```

Example

```bash
nmap -sn 10.0.2.0/24
```

Purpose

- Host Discovery
- Network Enumeration

Expected Detection

- Network Scan
- ICMP Activity

---

# Attack Scenario 2

# TCP Port Scan

```bash
nmap -sS <WINDOWS_IP>
```

Example

```bash
nmap -sS 10.0.2.20
```

Purpose

Discover open ports.

Expected Detection

- Port Scan
- Suspicious Network Activity

---

# Attack Scenario 3

# Service Enumeration

```bash
nmap -sV <WINDOWS_IP>
```

Purpose

Identify running services.

Example

```bash
nmap -sV 10.0.2.20
```

---

# Attack Scenario 4

# Operating System Detection

```bash
sudo nmap -O <WINDOWS_IP>
```

Example

```bash
sudo nmap -O 10.0.2.20
```

Purpose

Operating system fingerprinting.

---

# Attack Scenario 5

# Aggressive Scan

```bash
sudo nmap -A <WINDOWS_IP>
```

Purpose

Collect

- OS
- Services
- Scripts
- Traceroute

---

# Attack Scenario 6

# Full TCP Scan

```bash
nmap -p- <WINDOWS_IP>
```

Purpose

Scan every TCP port.

---

# Optional Attack

# Hydra Brute Force

Example

```bash
hydra -l administrator -P passwords.txt rdp://<WINDOWS_IP>
```

Purpose

Generate authentication failures.

Expected Detection

- Failed Login
- Brute Force Attempts

---

# Optional Attack

# Netcat Test

Start listener

```bash
nc -lvnp 4444
```

---

# Detection in Wazuh

Open

```
Dashboard

Threat Hunting

Security Events
```

Search for

```
nmap
```

or

```
scan
```

Verify alerts appear.

---

# Example Detection Flow

```
Kali Attack

↓

Windows Network Activity

↓

Sysmon

↓

Wazuh Agent

↓

Wazuh Manager

↓

Rules Engine

↓

Dashboard Alert
```

---

# MITRE ATT&CK Mapping

| Attack | Technique |
|----------|-----------|
| Network Discovery | T1016 |
| Port Scan | T1046 |
| Service Enumeration | T1046 |
| Brute Force | T1110 |
| PowerShell | T1059 |
| Command Execution | T1059 |

---

# Verification Checklist

- Kali Network Connected

- Ping Successful

- Port Scan Completed

- Services Enumerated

- Alerts Generated

- Dashboard Updated

---

# Screenshots

### 1. Kali Linux Agent — Threat Hunting Ingestion
![Kali Threat Hunting Overview](../screenshots/20-kali-agent-threat-hunting.png)
*Initial telemetry and SCA metrics ingested into Wazuh Dashboard for Kali Linux agent (`hacker01` / `004`).*

---

### 2. Multi-Source Log Ingestion & Rule Groups
![Kali Log Telemetry](../screenshots/21-kali-agent-log-telemetry.png)
*Multi-source log ingestion (dpkg, syslog, config_changed, sca, ossec) showing 214 security events captured for the Kali agent.*

---

### 3. Kali Authentication & PAM Privileged Activity
![Kali PAM Auth Events](../screenshots/21a-kali-auth-pam-events.png)
*Wazuh Alerts index (`wazuh-alerts-*`) capturing authentication and privilege telemetry (`/var/log/auth.log` Rule 5502: PAM login session for `root`).*

---

### 4. Real-Time Threat Hunting Events Detail View
![Agent Events Detail View](../screenshots/22-agent-threat-hunting-events.png)
*Real-time Threat Hunting event table showing rule descriptions, rule IDs (61104, 60642, 19009, 61102), severity levels, and CIS benchmarks.*

---

# Conclusion

The Kali Linux attack simulations successfully generated security events that were detected by the Wazuh SIEM platform. These exercises demonstrate how offensive security techniques can be used to validate defensive monitoring and incident detection within a SOC environment.