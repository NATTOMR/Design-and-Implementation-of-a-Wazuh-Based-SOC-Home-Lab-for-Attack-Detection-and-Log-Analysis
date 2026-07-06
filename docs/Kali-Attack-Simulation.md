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

Capture

1. Kali Desktop

2. IP Address

3. Ping Test

4. Nmap Ping Scan

5. TCP Scan

6. Service Enumeration

7. OS Detection

8. Aggressive Scan

9. Wazuh Alert

10. Dashboard Security Events

11. Active Agents

12. Threat Hunting Page

---

# Conclusion

The Kali Linux attack simulations successfully generated security events that were detected by the Wazuh SIEM platform. These exercises demonstrate how offensive security techniques can be used to validate defensive monitoring and incident detection within a SOC environment.