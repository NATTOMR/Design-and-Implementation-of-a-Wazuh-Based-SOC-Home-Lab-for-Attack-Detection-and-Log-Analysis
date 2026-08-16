# 🛡️ Design and Implementation of a Wazuh-Based SOC Home Lab for Attack Detection and Log Analysis

![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-VirtualBox-blue)
![OS](https://img.shields.io/badge/OS-Ubuntu%2024.04%20%7C%20Windows%2011-orange)
![Wazuh](https://img.shields.io/badge/Wazuh-4.x-0052CC)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📖 Project Overview

This project demonstrates the design and implementation of a Security Operations Center (SOC) Home Lab using the **Wazuh SIEM platform**. The lab simulates real-world cyberattacks and security monitoring in a controlled virtual environment.

The environment consists of:

- 🖥️ Ubuntu Server running Wazuh Manager
- 💻 Windows 11 Endpoint with Sysmon and Wazuh Agent
- 🐉 Kali Linux Attacker Machine

The objective is to detect malicious activities, collect security events, analyze logs, and generate alerts through the Wazuh Dashboard.



---

# 🎯 Objectives

- Deploy a complete Wazuh SIEM environment
- Monitor Windows endpoint activity
- Detect network reconnaissance
- Detect brute-force attacks
- Detect suspicious PowerShell execution
- Collect Sysmon telemetry
- Create a professional SOC Home Lab
- Document the entire deployment process

---

# 🏗️ Lab Architecture

```
                   Internet
                        │
                VirtualBox NAT Network
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      │                 │                 │
 Ubuntu Server      Windows 11        Kali Linux
(Wazuh Server)      (Victim)          (Attacker)
      │                 │                 │
      │                 │                 │
      └──────────── Wazuh Agent ──────────┘
                    Security Logs
                         │
                  Wazuh Manager
                         │
                Wazuh Dashboard
```

---

# 💻 Virtual Machines

| Machine | Operating System | Purpose |
|----------|------------------|---------|
| Wazuh Server | Ubuntu Server 24.04 LTS | SIEM Platform |
| Windows Endpoint | Windows 11 Pro | Victim Machine |
| Attacker | Kali Linux | Attack Simulation |

---

# 🛠 Technologies Used

## Operating Systems

- Ubuntu Server 24.04 LTS
- Windows 11 Pro
- Kali Linux

## Security Tools

- Wazuh
- Sysmon
- Windows Event Logs
- Filebeat
- OpenSearch
- Wazuh Dashboard

## Offensive Security

- Nmap
- Hydra
- Netcat
- Metasploit
- CrackMapExec (Optional)

## Networking

- VirtualBox
- NAT Network

---

# 📂 Repository Structure

```
.
├── README.md
├── LICENSE
├── .gitignore
├── docs/
├── configs/
├── detection/
├── kali/
├── ubuntu/
├── windows11/
├── wazuh/
├── screenshots/
└── reports/
```

---

# 📚 Documentation

| Document | Description |
|----------|-------------|
| docs/Architecture.md | Lab architecture |
| docs/Ubuntu-Installation.md | Ubuntu Server 24.04 installation |
| docs/Wazuh-Installation.md | Complete Wazuh installation |
| docs/Windows11-Agent.md | Windows Agent installation |
| docs/Kali-Attack-Simulation.md | Attack simulations |
| docs/Sysmon-Configuration.md | Sysmon deployment |
| docs/Detection-Rules.md | Detection rules |
| docs/Troubleshooting.md | Common issues |

---

# 🔥 Attack Simulations

The following attacks were simulated and detected.

- Network Scanning (Nmap)
- SSH Brute Force
- RDP Brute Force
- Failed Logon Attempts
- PowerShell Execution
- Sysmon Process Creation
- Service Installation
- Registry Modification
- File Integrity Monitoring

---

# 📊 Detection Workflow

```
Attack
   │
   ▼
Windows Event Logs
   │
Sysmon
   │
Wazuh Agent
   │
Wazuh Manager
   │
Rules Engine
   │
Alert Generation
   │
Dashboard
```

---

# 📸 Screenshots

The complete screenshots are available inside

```
screenshots/
```

Example screenshots include

- Wazuh Dashboard
- Agent Registration
- Nmap Detection
- Sysmon Events
- Alert Dashboard
- Security Overview

---

# 🚀 Installation Guide

Detailed installation instructions are available in

```
docs/Wazuh-Installation.md
```

---

# 📑 Project Report

The complete project report is available in

```
reports/Final_Report.pdf
```

---

# 📚 References

- [Project Video Demonstration on YouTube](https://youtu.be/duEibRGYMHo?si=kfcGcQ_OzSiN8hRz)

---

# 👨‍💻 Author

**Natto Muni Chakma**

B.Tech Computer Science and Engineering

Andhra University College of Engineering

Specialization:
- Cybersecurity
- Security Operations Center (SOC)
- Threat Detection
- Digital Forensics

GitHub:
https://github.com/NATTOMR

---

# ⭐ Future Improvements

- Integrate Suricata IDS
- Integrate VirusTotal API
- YARA Rule Detection
- Sigma Rule Integration
- MITRE ATT&CK Mapping
- TheHive Integration
- Shuffle SOAR Automation

---

# 📜 License

This project is licensed under the MIT License.