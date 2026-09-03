# Wazuh SOC & Threat Hunting Lab

![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-VirtualBox-blue)
![OS](https://img.shields.io/badge/OS-Ubuntu%2024.04%20%7C%20Windows%2011-orange)
![Wazuh](https://img.shields.io/badge/Wazuh-4.x-0052CC)

---

## 📖 Project Overview

A three-part Wazuh-based Security Operations Center lab for threat detection, threat intelligence integration, threat hunting, and SOC monitoring using Windows, Linux, Sysmon, MITRE ATT&CK, and external threat intelligence sources.

### Three Implementation Layers:

1. **Part 1 — Threat Hunting Lab** (✅ Implemented / In Progress)
2. **Part 2 — Threat Intelligence Platform** (🔵 Planned / Partially implemented)
3. **Part 3 — SOC Operations Dashboard** (🔵 Planned / Partially implemented)

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
├── .github/
├── README.md
├── LICENSE
├── .gitignore
├── configs/
├── detection/
├── docs/
│   ├── part-1-threat-hunting/
│   ├── part-2-threat-intelligence/
│   └── part-3-soc-dashboard/
├── kali/
├── ubuntu/
├── windows11/
├── wazuh/
├── threat-intelligence/
├── dashboard/
├── scripts/
├── screenshots/
└── reports/
```

---

# 📚 Documentation

| Document | Description |
|:---|:---|
| [docs/part-1-threat-hunting/README.md](docs/part-1-threat-hunting/README.md) | Part 1 Overview |
| [docs/part-2-threat-intelligence/README.md](docs/part-2-threat-intelligence/README.md) | Part 2 Overview |
| [docs/part-3-soc-dashboard/README.md](docs/part-3-soc-dashboard/README.md) | Part 3 Overview |
| [docs/Ubuntu-Installation.md](docs/Ubuntu-Installation.md) | Ubuntu Server 24.04 LTS deployment |
| [docs/Wazuh-Installation.md](docs/Wazuh-Installation.md) | Complete Wazuh SIEM platform installation |
| [docs/Windows11-Agent.md](docs/Windows11-Agent.md) | Windows 11 Wazuh Agent deployment |
| [docs/Sysmon-Configuration-Windows.md](docs/Sysmon-Configuration-Windows.md) | Microsoft Sysmon deployment on Windows 11 |
| [docs/Sysmon-Configuration-Linux.md](docs/Sysmon-Configuration-Linux.md) | Microsoft Sysmon for Linux (`sysmonforlinux`) eBPF telemetry |
| [docs/Troubleshooting.md](docs/Troubleshooting.md) | SOC lab deployment troubleshooting |
| [docs/WAZUH_COMMAND_REFERENCE.md](docs/WAZUH_COMMAND_REFERENCE.md) | Complete Wazuh command cheatsheet |

---

# 🔥 Attack Simulations

The following attack scenarios and tactics were simulated and detected in this lab:

- **Network Reconnaissance & Port Scanning** (Nmap TCP Syn / Service / Aggressive scans)
- **Authentication & Brute Force** (Hydra RDP/SSH & Windows Event 4625 failed logons)
- **Suspicious Process Execution** (PowerShell, `curl`, `netcat`, and suspicious binaries)
- **Advanced Endpoint Telemetry** (Sysmon Process Creation `EventID 1`, Network Connect `EventID 3`, Process Terminate `EventID 5`)
- **Persistence & Configuration Changes** (Windows Registry modifications & Linux `/etc/` file changes)
- **File Integrity Monitoring (FIM)** (Real-time file creation and tampering detection)

---

# 📊 Detection Workflow

```mermaid
flowchart TD
    A["⚔️ Cyber Attack / Simulation (Kali Linux)"] --> B["🖥️ Monitored Endpoint (Windows 11 / Linux)"]
    B --> C["📋 Windows Event Logs / Syslog"]
    B --> D["🔍 Microsoft Sysmon (eBPF / Drivers)"]
    C --> E["📡 Wazuh Agent"]
    D --> E
    E -->|Encrypted Stream :1514| F["🛡️ Wazuh Manager (Ubuntu Server)"]
    F --> G["⚙️ Decoders & Rules Engine"]
    G --> H["🚨 Alert Indexing (OpenSearch Indexer)"]
    H --> I["📊 Wazuh Dashboard Visualization"]
```

---

# 📸 Key Visual Evidence & Dashboards

![Wazuh Dashboard Home](screenshots/13-wazuh-dashboard-home.png)
*Centralized Wazuh Dashboard home interface presenting aggregate security alerts.*

![Active Agents Overview](screenshots/19-active-agents.png)
*Multi-platform active endpoint monitoring in Wazuh Dashboard.*

![Sysmon Telemetry Ingestion](screenshots/24-sysmon-events-dashboard.png)
*Live endpoint telemetry and Sysmon process events indexed in Wazuh.*

> Complete screenshot gallery available in **[screenshots/README.md](screenshots/README.md)**.

---

# 🚀 Installation Guide

Step-by-step installation instructions are available in:
- **[Wazuh Installation Guide](docs/Wazuh-Installation.md)**
- **[Windows 11 Agent Guide](docs/Windows11-Agent.md)**
- **[Sysmon Windows Guide](docs/Sysmon-Configuration-Windows.md)**
- **[Sysmon Linux Guide](docs/Sysmon-Configuration-Linux.md)**

---

# 📑 Project Report

The complete academic project report is available in:
- **[`reports/Final_Report.pdf`](reports/Final_Report.pdf)**
- **[Report Summary Documentation](reports/README.md)**

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