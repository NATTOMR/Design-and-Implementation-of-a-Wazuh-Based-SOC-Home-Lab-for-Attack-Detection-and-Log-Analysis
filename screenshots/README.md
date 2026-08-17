```screenshots/
│
├── 01-host-machine.png
├── 02-virtualbox-home.png
├── 03-nat-network-settings.png
│
├── 04-ubuntu-installation.png
├── 05-ubuntu-login.png
├── 06-system-update.png
├── 07-wazuh-installation.png
├── 08-wazuh-installation-complete.png
├── 09-wazuh-manager-status.png
├── 10-wazuh-indexer-status.png
├── 11-wazuh-dashboard-status.png
├── 12-wazuh-dashboard-login.png
├── 13-wazuh-dashboard-home.png
│
├── 14-windows11-desktop.png
├── 15-windows-agent-installer.png
├── 16-windows-agent-installation.png
├── 17-wazuh-agent-service.png
├── 18-agent-registered.png
├── 18a-agent-pending.png
├── 19-active-agents.png
├── 19a-failed-logon-test.png
├── 19b-failed-logon-events.png
├── 19c-dashboard-events-overview.png
├── 19d-dashboard-failed-logon.png
├── 20-kali-agent-threat-hunting.png
├── 21-kali-agent-log-telemetry.png
├── 21a-kali-auth-pam-events.png
├── 22-agent-threat-hunting-events.png
├── Screenshot 2026-08-17 010853.png
├── Screenshot 2026-08-17 012801.png
├── Screenshot 2026-08-17 014722.png
│
├── 20-sysmon-download.png
├── 21-sysmon-installation.png
├── 22-sysmon-service.png
├── 23-event-viewer-sysmon.png
├── 24a-ossec-sysmon-config.png
├── 24b-wazuh-service-restart.png
├── 24-sysmon-events-dashboard.png
├── 24c-sysmon-linux-events-dashboard.png
├── 24d-windows-sysmon-threat-hunting.png
│
├── 25-kali-desktop.png
├── 26-kali-ip-address.png
├── 27-ping-windows.png
├── 28-ping-wazuh-server.png
├── 29-nmap-host-discovery.png
├── 30-nmap-port-scan.png
├── 31-nmap-service-scan.png
├── 32-nmap-os-detection.png
├── 33-nmap-aggressive-scan.png
│
├── 34-security-events.png
├── 35-alert-details.png
├── 36-rule-information.png
├── 37-mitre-attck-mapping.png
├── 38-dashboard-threat-hunting.png
├── 39-dashboard-overview.png
│
├── 40-ossec-conf.png
├── 41-local-rules.png
├── 42-local-decoder.png
├── 43-sysmon-config.png
│
├── 44-filebeat-status.png
├── 45-systemctl-services.png
├── 46-agent-control-list.png
│
├── 47-final-dashboard.png
├── 48-project-architecture.png
└── 49-final-alert.png

```

```
## Host Machine

![Host Machine](../screenshots/01-host-machine.png)

---

## VirtualBox Home

![VirtualBox Home](../screenshots/02-virtualbox-home.png)

---

## NAT Network Settings

![NAT Network Settings](../screenshots/03-nat-network-settings.png)

---

## Ubuntu Installation

![Ubuntu Installation](../screenshots/04-ubuntu-installation.png)

---

## Ubuntu Login

![Ubuntu Login](../screenshots/05-ubuntu-login.png)

---

## System Update

![System Update](../screenshots/06-system-update.png)

---

## Wazuh Installation

![Wazuh Installation](../screenshots/07-wazuh-installation.png)

---

## Wazuh Installation Complete

![Wazuh Installation Complete](../screenshots/08-wazuh-installation-complete.png)

---

## Wazuh Manager Status

![Wazuh Manager Status](../screenshots/09-wazuh-manager-status.png)

---

## Wazuh Indexer Status

![Wazuh Indexer Status](../screenshots/10-wazuh-indexer-status.png)

---

## Wazuh Dashboard Status

![Wazuh Dashboard Status](../screenshots/11-wazuh-dashboard-status.png)

---

## Wazuh Dashboard Login

![Wazuh Dashboard Login](../screenshots/12-wazuh-dashboard-login.png)

---

## Wazuh Dashboard Home

![Wazuh Dashboard Home](../screenshots/13-wazuh-dashboard-home.png)

---

## Windows 11 Desktop

![Windows 11 Desktop](../screenshots/14-windows11-desktop.png)

---

## Wazuh Agent Installer

![Wazuh Agent Installer](../screenshots/15-windows-agent-installer.png)

---

## Windows Agent Installation

![Windows Agent Installation](../screenshots/16-windows-agent-installation.png)

---

## Wazuh Agent Service

![Wazuh Agent Service](../screenshots/17-wazuh-agent-service.png)

---

## Agent Registered

![Agent Registered](../screenshots/18-agent-registered.png)

---

## Active Agents

![Active Agents](../screenshots/19-active-agents.png)

---

## Kali Linux Agent (004) — Threat Hunting Overview

![Kali Threat Hunting Overview](../screenshots/20-kali-agent-threat-hunting.png)
*Initial telemetry and SCA metrics ingested into Wazuh Dashboard for Kali Linux agent (`hacker01` / `004`).*

---

## Kali Linux Agent (004) — Comprehensive Log Telemetry & Rule Groups

![Kali Log Telemetry](../screenshots/21-kali-agent-log-telemetry.png)
*Multi-source log ingestion (dpkg, syslog, config_changed, sca, ossec) showing 214 security events captured for the Kali agent.*

---

## Kali Linux Agent (004) — Authentication & PAM Logs

![Kali PAM Auth Events](../screenshots/21a-kali-auth-pam-events.png)
*Wazuh Alerts index (`wazuh-alerts-*`) capturing authentication and privilege telemetry (`/var/log/auth.log` Rule 5502: PAM login session for `root`).*

---

## Agent Threat Hunting Events Detail View

![Agent Events Detail View](../screenshots/22-agent-threat-hunting-events.png)
*Real-time Threat Hunting event table showing rule descriptions, rule IDs (61104, 60642, 19009, 61102), severity levels, and CIS benchmarks.*

---

## Sysmon Download & Working Directory Setup

![Sysmon Download](../screenshots/20-sysmon-download.png)
*Extracted Sysmon binaries (`Sysmon64.exe`) and configuration XML (`sysmonconfig-export.xml`) placed in `C:\Sysmon`.*

---

## Sysmon Installation via PowerShell

![Sysmon Installation](../screenshots/21-sysmon-installation.png)
*PowerShell Administrator execution: `.\Sysmon64.exe -accepteula -i sysmonconfig-export.xml` with schema version 4.91 validation.*

---

## Sysmon Service Status

![Sysmon Service](../screenshots/22-sysmon-service.png)
*Verification of `Sysmon64` service in `Running` status using `Get-Service Sysmon64`.*

---

## Event Viewer - Sysmon Operational Logs

![Event Viewer Sysmon](../screenshots/23-event-viewer-sysmon.png)
*Windows Event Viewer navigated to `Microsoft-Windows-Sysmon/Operational` capturing real-time Event ID 1 (Process Create).*

---

## Wazuh Agent ossec.conf Sysmon Configuration

![Wazuh ossec.conf Sysmon](../screenshots/24a-ossec-sysmon-config.png)
*Wazuh Agent configuration (`ossec.conf`) enabling Sysmon event channel log collection.*

---

## Wazuh Agent Service Restart

![Wazuh Service Restart](../screenshots/24b-wazuh-service-restart.png)
*Restarting `WazuhSvc` service (`NET STOP WazuhSvc` & `NET START WazuhSvc`) to begin forwarding Sysmon logs.*

---

## Sysmon Events Telemetry in Wazuh Dashboard (Windows 11)

![Sysmon Events Dashboard](../screenshots/24-sysmon-events-dashboard.png)
*Wazuh Discover interface showing 1,400+ Sysmon telemetry events ingested from the Windows 11 endpoint (`hackme` / `003`).*

---

## Sysmon for Linux Telemetry Ingestion (10,000+ Events)

![Sysmon for Linux Events Dashboard](../screenshots/24c-sysmon-linux-events-dashboard.png)
*Wazuh Discover querying `sysmon` on `wazuh-archives-*` showing 10,135 ingested events from Kali Linux endpoint (`agent.name: kali`, `agent.id: 004`, `192.168.100.6`), capturing `Linux-Sysmon` process termination (`EventID 5`) via `/var/log/syslog`.*

---

## Windows Sysmon Filtered Threat Hunting View

![Windows Sysmon Threat Hunting](../screenshots/24d-windows-sysmon-threat-hunting.png)
*Wazuh Discover filtered query `agent.id:003 AND sysmon` isolating 1,290+ endpoint telemetry hits from Windows agent.*

---

## Kali Desktop

![Kali Desktop](../screenshots/25-kali-desktop.png)

---

## Kali IP Address

![Kali IP Address](../screenshots/26-kali-ip-address.png)

---

## Ping Windows

![Ping Windows](../screenshots/27-ping-windows.png)

---

## Ping Wazuh Server

![Ping Wazuh Server](../screenshots/28-ping-wazuh-server.png)

---

## Nmap Host Discovery

![Nmap Host Discovery](../screenshots/29-nmap-host-discovery.png)

---

## Nmap Port Scan

![Nmap Port Scan](../screenshots/30-nmap-port-scan.png)

---

## Nmap Service Scan

![Nmap Service Scan](../screenshots/31-nmap-service-scan.png)

---

## Nmap OS Detection

![Nmap OS Detection](../screenshots/32-nmap-os-detection.png)

---

## Nmap Aggressive Scan

![Nmap Aggressive Scan](../screenshots/33-nmap-aggressive-scan.png)

---

## Security Events

![Security Events](../screenshots/34-security-events.png)

---

## Alert Details

![Alert Details](../screenshots/35-alert-details.png)

---

## Rule Information

![Rule Information](../screenshots/36-rule-information.png)

---

## MITRE ATT&CK Mapping

![MITRE ATT&CK Mapping](../screenshots/37-mitre-attck-mapping.png)

---

## Dashboard Threat Hunting

![Dashboard Threat Hunting](../screenshots/38-dashboard-threat-hunting.png)

---

## Dashboard Overview

![Dashboard Overview](../screenshots/39-dashboard-overview.png)

---

## ossec.conf

![ossec.conf](../screenshots/40-ossec-conf.png)

---

## Local Rules

![Local Rules](../screenshots/41-local-rules.png)

---

## Local Decoder

![Local Decoder](../screenshots/42-local-decoder.png)

---

## Sysmon Configuration

![Sysmon Configuration](../screenshots/43-sysmon-config.png)

---

## Filebeat Status

![Filebeat Status](../screenshots/44-filebeat-status.png)

---

## Systemctl Services

![Systemctl Services](../screenshots/45-systemctl-services.png)

---

## Agent Control List

![Agent Control List](../screenshots/46-agent-control-list.png)

---

## Final Dashboard

![Final Dashboard](../screenshots/47-final-dashboard.png)

---

## Project Architecture

![Project Architecture](../screenshots/48-project-architecture.png)

---

## Final Alert

![Final Alert](../screenshots/49-final-alert.png)
```

```
| Document                      | Screenshot Numbers     |
| ----------------------------- | ---------------------- |
| **README.md**                 | 13, 19, 39, 47, 48, 49 |
| **Architecture.md**           | 2, 3, 48               |
| **Wazuh-Installation.md**     | 4–13                   |
| **Windows11-Agent.md**              | 14–19                  |
| **Sysmon-Configuration-Windows.md** | 20–24b                 |
| **Sysmon-Configuration-Linux.md**   | Linux eBPF telemetry   |
| **Kali-Attack-Simulation.md**       | 25–39                  |
| **Detection-Rules.md**              | 34–39, 49              |
| **Troubleshooting.md**              | 45–46                  |


```
