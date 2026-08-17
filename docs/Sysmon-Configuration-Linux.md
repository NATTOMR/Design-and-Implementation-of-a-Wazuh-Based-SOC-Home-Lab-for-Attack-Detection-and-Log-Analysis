# Sysmon Configuration for Linux

This document describes how **Microsoft Sysmon for Linux (`sysmonforlinux`)** was installed and configured on Linux endpoints (Ubuntu Server / Kali Linux) to provide advanced eBPF-based endpoint telemetry for the Wazuh SIEM platform.

---

# Table of Contents

- [Introduction](#introduction)
- [Why Sysmon for Linux?](#why-sysmon-for-linux)
- [Prerequisites](#prerequisites)
- [Add Microsoft Repository](#add-microsoft-repository)
- [Install Sysmon for Linux](#install-sysmon-for-linux)
- [Download & Prepare Linux Configuration](#download--prepare-linux-configuration)
- [Apply Configuration & Start Service](#apply-configuration--start-service)
- [Verify Installation & Telemetry](#verify-installation--telemetry)
- [Configure Wazuh Agent for Sysmon Ingestion](#configure-wazuh-agent-for-sysmon-ingestion)
- [Important Sysmon for Linux Event IDs](#important-sysmon-for-linux-event-ids)
- [Testing & Generating Telemetry](#testing--generating-telemetry)
- [Verify in Wazuh Dashboard](#verify-in-wazuh-dashboard)
- [Troubleshooting](#troubleshooting)
- [Verification Checklist](#verification-checklist)
- [Conclusion](#conclusion)

---

# Introduction

**Sysmon for Linux** is an open-source tool developed by Microsoft that leverages the extended Berkeley Packet Filter (**eBPF**) kernel technology to monitor, capture, and log system activities across Linux environments.

Unlike traditional Linux logging, Sysmon for Linux provides unified telemetry schema similar to Windows Sysmon events, capturing:

- Process Creation with full command-line arguments and parent process tracking
- Network Connections (outbound and inbound TCP/UDP)
- Process Termination
- Raw Disk and Device Access
- File Creation and Deletion
- Configuration Changes

These events are written to the Linux system log (`syslog` / `journald`) and ingested by the Wazuh Agent for SIEM correlation, alert generation, and threat hunting.

---

# Why Sysmon for Linux?

Standard Linux logging mechanisms (such as basic `syslog` or unconfigured `auditd`) can leave gaps in process hierarchy and network socket correlation:

| Feature | Default Linux Logs | Linux Auditd | Sysmon for Linux (eBPF) |
|---|---|---|---|
| **Process Tree Tracking** | ❌ Minimal | ⚠️ Complex rule tuning | ✅ Native parent/child process correlation |
| **Network Socket to Process** | ❌ No | ⚠️ High performance overhead | ✅ Real-time PID-to-Socket mapping |
| **Configuration Model** | ⚠️ Decentralized | ⚠️ Complex audit rules | ✅ Structured XML configuration |
| **SIEM Compatibility** | ⚠️ Inconsistent formats | ⚠️ Multi-line audit records | ✅ Consistent Event ID taxonomy |
| **Kernel Overhead** | ✅ Low | ⚠️ Medium to High under load | ✅ Highly efficient eBPF hooks |

---

# Prerequisites

Before installing Sysmon for Linux:

- **Operating System:** Ubuntu Server 24.04 / 22.04 LTS or Kali Linux / Debian 11+
- **Linux Kernel:** Kernel version `5.4` or higher with eBPF support enabled (`CONFIG_BPF=y`, `CONFIG_BPF_SYSCALL=y`)
- **Privileges:** `sudo` / Root administrative privileges
- **Wazuh Agent:** Installed and connected to the Wazuh Manager

---

# Add Microsoft Repository

Microsoft packages Sysmon for Linux in its official Linux software repository.

### 1. Update Package Index & Install Prerequisites

```bash
sudo apt update
sudo apt install -y wget gpg software-properties-common apt-transport-https
```

### 2. Download and Register the Microsoft GPG Key

```bash
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null
```

### 3. Add the Microsoft Linux Package Repository

For **Ubuntu 24.04 / 22.04**:
```bash
sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list)"
```

For **Debian / Kali Linux**:
```bash
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/microsoft.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" | sudo tee /etc/apt/sources.list.d/microsoft-prod.list
```

### 4. Refresh Package Lists

```bash
sudo apt update
```

---

# Install Sysmon for Linux

Install `sysmonforlinux` using the APT package manager:

```bash
sudo apt install -y sysmonforlinux
```

Expected confirmation:
```text
Setting up sysmonforlinux ...
Created symlink /etc/systemd/system/multi-user.target.wants/sysmon.service → /lib/systemd/system/sysmon.service.
```

---

# Download & Prepare Linux Configuration

Sysmon requires an XML configuration file to define filtering rules and event collection parameters.

Create or download the Sysmon Linux configuration file (e.g. `sysmonconfig-linux.xml`):

```bash
sudo mkdir -p /etc/sysmon
```

Create `/etc/sysmon/sysmonconfig-linux.xml`:

```xml
<Sysmon schemaversion="4.90">
  <EventFiltering>
    <!-- Event ID 1: Process Create -->
    <RuleGroup name="ProcessCreate" groupRelation="or">
      <ProcessCreate onmatch="exclude">
        <!-- Exclude noisy system daemons -->
        <Image condition="is">/usr/bin/uptime</Image>
      </ProcessCreate>
    </RuleGroup>

    <!-- Event ID 3: Network Connection -->
    <RuleGroup name="NetworkConnect" groupRelation="or">
      <NetworkConnect onmatch="include">
        <DestinationPort condition="is">22</DestinationPort>
        <DestinationPort condition="is">80</DestinationPort>
        <DestinationPort condition="is">443</DestinationPort>
        <DestinationPort condition="is">4444</DestinationPort>
        <DestinationPort condition="is">8080</DestinationPort>
        <DestinationPort condition="is">9001</DestinationPort>
      </NetworkConnect>
    </RuleGroup>

    <!-- Event ID 5: Process Terminate -->
    <RuleGroup name="ProcessTerminate" groupRelation="or">
      <ProcessTerminate onmatch="include">
        <Image condition="contains">nc</Image>
        <Image condition="contains">nmap</Image>
      </ProcessTerminate>
    </RuleGroup>

    <!-- Event ID 11: File Create -->
    <RuleGroup name="FileCreate" groupRelation="or">
      <FileCreate onmatch="include">
        <TargetFilename condition="begin with">/tmp/</TargetFilename>
        <TargetFilename condition="begin with">/dev/shm/</TargetFilename>
        <TargetFilename condition="begin with">/etc/</TargetFilename>
      </FileCreate>
    </RuleGroup>

    <!-- Event ID 23: File Delete -->
    <RuleGroup name="FileDelete" groupRelation="or">
      <FileDelete onmatch="include">
        <TargetFilename condition="begin with">/tmp/</TargetFilename>
      </FileDelete>
    </RuleGroup>
  </EventFiltering>
</Sysmon>
```

---

# Apply Configuration & Start Service

### 1. Load Configuration File into Sysmon

Load the configuration using the `sysmon` CLI with the `-i` flag and accept the EULA (`-accepteula`):

```bash
sudo sysmon -accepteula -i /etc/sysmon/sysmonconfig-linux.xml
```

Expected output:
```text
System Monitor for Linux v1.3.0 - System activity monitor
By Mark Russinovich, Thomas Garnier and Kevin Sheldrake
Copyright (C) 2021-2024 Microsoft Corporation
Using libxml2. libxml2 is Copyright (C) 1998-2012 Daniel Veillard. All Rights Reserved.
Sysinternals - www.sysinternals.com

Loading configuration file with schema version 4.90
Sysmon schema version: 4.90
Configuration file validated.
Configuration updated.
```

### 2. Enable and Start the Systemd Service

```bash
sudo systemctl enable --now sysmon
```

---

# Verify Installation & Telemetry

### 1. Check Service Status

```bash
sudo systemctl status sysmon
```

Expected status:
```text
● sysmon.service - Sysmon for Linux
     Loaded: loaded (/lib/systemd/system/sysmon.service; enabled; preset: enabled)
     Active: active (running) since Tue 2026-08-18 03:20:00 UTC; 1min ago
   Main PID: 12345 (sysmon)
      Tasks: 4 (limit: 4613)
     Memory: 48.2M
        CPU: 125ms
     CGroup: /system.slice/sysmon.service
             └─12345 /opt/sysmon/sysmon
```

### 2. Inspect Live Sysmon Logs locally

View recent events streamed to system logs:

```bash
sudo journalctl -u sysmon -f
```

or filter `/var/log/syslog`:

```bash
sudo tail -f /var/log/syslog | grep -i sysmon
```

---

# Configure Wazuh Agent for Sysmon Ingestion

To forward Sysmon for Linux events into the Wazuh SIEM platform, add the syslog / journald log collection block to `/var/ossec/etc/ossec.conf`.

### 1. Edit `/var/ossec/etc/ossec.conf`

```bash
sudo nano /var/ossec/etc/ossec.conf
```

Add the following `<localfile>` configuration block within the `<ossec_config>` section:

```xml
  <!-- Sysmon for Linux Log Collection -->
  <localfile>
    <location>/var/log/syslog</location>
    <log_format>syslog</log_format>
  </localfile>
```

*(On systems using `systemd-journald` without `rsyslog`, use journald collection):*

```xml
  <localfile>
    <location>journald</location>
    <log_format>journald</log_format>
    <filter_field>_SYSTEMD_UNIT:sysmon.service</filter_field>
  </localfile>
```

### 2. Restart the Wazuh Agent

```bash
sudo systemctl restart wazuh-agent
```

Verify the agent status:

```bash
sudo systemctl status wazuh-agent
```

---

# Important Sysmon for Linux Event IDs

Sysmon for Linux generates structured events corresponding to the standard Sysinternals schema:

| Event ID | Event Name | Description | Example Security Use Case |
|---|---|---|---|
| **1** | `ProcessCreate` | A new Linux process is executed | Detects reverse shells, suspicious binary executions (`/tmp/exploit`), unauthorized CLI commands |
| **3** | `NetworkConnect` | Outbound/Inbound TCP/UDP network connection | Detects C2 beaconing, port scanning, unauthorized outbound data exfiltration |
| **5** | `ProcessTerminate` | Process lifecycle termination | Tracks persistence lifetime, malware self-termination |
| **9** | `RawAccessRead` | Raw reading of storage block devices (`/dev/sda`, memory) | Detects rootkits, credential scraping, dumping partition tables |
| **11** | `FileCreate` | Creation of files in monitored paths | Identifies dropper files, web shells placed in `/var/www/` or `/tmp/` |
| **16** | `SysmonConfigStateChanged` | Sysmon configuration was modified | Detects tampering with detection telemetry |
| **23** | `FileDelete` | File deleted from system | Detects malware anti-forensic evidence wiping |

---

# Testing & Generating Telemetry

To verify end-to-end detection, generate test events on the Linux endpoint:

### 1. Test Process Creation (Event ID 1)
```bash
curl -s http://example.com/test-telemetry
```

### 2. Test File Creation in Monitored Directory (Event ID 11)
```bash
echo "test_payload" | sudo tee /tmp/suspicious_script.sh
```

### 3. Test Network Connection (Event ID 3)
```bash
nc -zv 10.0.2.15 80
```

---

# Verify in Wazuh Dashboard

1. Log in to the **Wazuh Dashboard** (`https://<WAZUH_SERVER_IP>`).
2. Navigate to **Modules** &rarr; **Security Events** (or **Threat Hunting** &rarr; **Events**).
3. Filter by Linux Agent:
   ```text
   agent.name: "ubuntu-server" OR agent.name: "kali-attacker"
   ```
4. Filter by Sysmon Provider / Log Message:
   ```text
   full_log: *sysmon* OR rule.groups: sysmon_linux
   ```
5. Confirm that **Process Creation**, **Network Connections**, and **File Activity** events are indexed and correlated.

---

# Troubleshooting

### 1. Sysmon Service Fails to Start (`eBPF not supported`)
- **Check Kernel Version:**
  ```bash
  uname -r
  ```
  Ensure kernel is $\ge 5.4$.
- **Verify BPF filesystem is mounted:**
  ```bash
  mount | grep bpf
  ```

### 2. No Events Appearing in `/var/log/syslog`
- Check if `rsyslog` is installed and running:
  ```bash
  sudo systemctl status rsyslog
  ```
- If using `journalctl`:
  ```bash
  sudo journalctl -u sysmon --no-pager -n 50
  ```

### 3. Updating Configuration
To reload changes after editing `sysmonconfig-linux.xml`:
```bash
sudo sysmon -c /etc/sysmon/sysmonconfig-linux.xml
```

---

# Verification Checklist

- [x] Microsoft package repository and GPG key registered
- [x] `sysmonforlinux` package installed
- [x] XML configuration file validated and applied (`sysmon -i`)
- [x] `sysmon.service` active and running via systemd
- [x] Local telemetry streaming in `journalctl` / `/var/log/syslog`
- [x] Wazuh Agent configured to collect Sysmon log channel
- [x] Events visible and searchable in Wazuh Dashboard

---

# Conclusion

Deploying **Sysmon for Linux** extends the SOC Home Lab's detection capabilities with deep eBPF-driven kernel visibility. Paired with Windows Sysmon, it establishes unified, cross-platform telemetry ingestion across both Linux and Windows endpoints into the Wazuh SIEM platform.
