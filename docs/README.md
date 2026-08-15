# 📚 Documentation

Welcome to the documentation for the **Design and Implementation of a Wazuh-Based SOC Home Lab for Attack Detection and Log Analysis** project.

This directory contains all technical documentation, installation guides, architecture descriptions, attack simulations, detection rules, and troubleshooting procedures used throughout the project.

---

# Documentation Structure

| Document | Description |
|----------|-------------|
| [Architecture.md](Architecture.md) | Overview of the SOC Home Lab architecture and network design. |
| [Ubuntu-Installation.md](Ubuntu-Installation.md) | Installation and setup of Ubuntu Server 24.04 LTS. |
| [Wazuh-Installation.md](Wazuh-Installation.md) | Step-by-step installation of the Wazuh SIEM platform. |
| [Windows11-Agent.md](Windows11-Agent.md) | Installation and configuration of the Wazuh Agent on Windows 11. |
| [Sysmon-Configuration.md](Sysmon-Configuration.md) | Deployment and configuration of Microsoft Sysmon. |
| [Kali-Attack-Simulation.md](Kali-Attack-Simulation.md) | Offensive security activities performed from Kali Linux. |
| [Detection-Rules.md](Detection-Rules.md) | Explanation of Wazuh detection rules and alert generation. |
| [Troubleshooting.md](Troubleshooting.md) | Common deployment issues and solutions. |

---

# Documentation Workflow

```
Start

↓

Architecture

↓

Install Ubuntu Server

↓

Install Wazuh

↓

Install Windows Agent

↓

Configure Sysmon

↓

Attack Simulation

↓

Detection Rules

↓

Troubleshooting

↓

Project Complete
```

---

# Project Directory

```
.
├── README.md
├── docs/
│   ├── README.md
│   ├── Architecture.md
│   ├── Ubuntu-Installation.md
│   ├── Wazuh-Installation.md
│   ├── Windows11-Agent.md
│   ├── Sysmon-Configuration.md
│   ├── Kali-Attack-Simulation.md
│   ├── Detection-Rules.md
│   └── Troubleshooting.md
│
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

# Recommended Reading Order

If you are reproducing this lab, follow the documents in this order:

1. Architecture
2. Ubuntu Installation
3. Wazuh Installation
4. Windows 11 Agent
5. Sysmon Configuration
6. Kali Attack Simulation
7. Detection Rules
8. Troubleshooting

---

# Related Directories

## configs/

Contains:

- ossec.conf
- local_rules.xml
- local_decoder.xml
- sysmonconfig.xml

---

## screenshots/

Contains screenshots demonstrating:

- Wazuh Dashboard
- Active Agents
- Sysmon Events
- Attack Detection
- Alert Details

---

## reports/

Contains the final academic project report.

---

# Technologies Used

## Operating Systems

- Ubuntu Server 24.04 LTS
- Windows 11 Pro
- Kali Linux

## Security Platforms

- Wazuh
- Sysmon

## Offensive Security Tools

- Nmap
- Hydra
- Netcat
- Metasploit

## Virtualization

- Oracle VirtualBox

---

# Objectives

This documentation enables readers to:

- Deploy an Ubuntu Server host environment
- Deploy a Wazuh SIEM environment
- Connect Windows endpoints
- Configure Sysmon
- Simulate cyberattacks
- Analyze security events
- Understand Wazuh detection rules
- Troubleshoot common deployment issues

---

# License

This project is licensed under the MIT License.

---

# Author

**Natto Muni Chakma**

B.Tech Computer Science and Engineering

Andhra University College of Engineering

Cybersecurity | SOC | SIEM | Threat Detection