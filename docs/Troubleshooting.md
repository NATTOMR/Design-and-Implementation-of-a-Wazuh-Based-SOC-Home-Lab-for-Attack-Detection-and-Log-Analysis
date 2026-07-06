# Troubleshooting Guide

This document summarizes the common issues encountered during the deployment of the Wazuh-based SOC Home Lab and the solutions used to resolve them.

---

# Table of Contents

- Wazuh Dashboard Issues
- Wazuh Manager Issues
- Wazuh Indexer Issues
- Windows Agent Issues
- Sysmon Issues
- Network Issues
- VirtualBox Issues
- Common Linux Commands
- Conclusion

---

# Wazuh Dashboard Issues

## Problem

Unable to access the dashboard.

```
https://<SERVER-IP>
```

### Possible Causes

- Dashboard service stopped
- Firewall blocking HTTPS
- Incorrect server IP
- Browser certificate warning

### Solution

Check the dashboard service.

```bash
sudo systemctl status wazuh-dashboard
```

Restart the service.

```bash
sudo systemctl restart wazuh-dashboard
```

Verify the service.

```bash
sudo systemctl status wazuh-dashboard
```

---

# Wazuh Manager Issues

## Problem

Manager service not running.

### Solution

Check the status.

```bash
sudo systemctl status wazuh-manager
```

Restart.

```bash
sudo systemctl restart wazuh-manager
```

View logs.

```bash
sudo journalctl -u wazuh-manager
```

---

# Wazuh Indexer Issues

## Problem

Indexer failed to start.

### Solution

Check service.

```bash
sudo systemctl status wazuh-indexer
```

Restart.

```bash
sudo systemctl restart wazuh-indexer
```

Check logs.

```bash
sudo journalctl -u wazuh-indexer
```

---

# Windows Agent Issues

## Problem

Windows agent shows **Disconnected**.

### Solution

Verify service.

```powershell
Get-Service WazuhSvc
```

Restart.

```powershell
NET STOP WazuhSvc

NET START WazuhSvc
```

Verify server IP in:

```
C:\Program Files (x86)\ossec-agent\ossec.conf
```

---

# Sysmon Issues

## Problem

No Sysmon events appear in Wazuh.

### Solution

Check the Sysmon service.

```powershell
Get-Service Sysmon64
```

Verify the Event Viewer log.

```
Applications and Services Logs

Microsoft

Windows

Sysmon

Operational
```

Restart Sysmon if necessary.

---

# Network Issues

## Problem

Windows cannot communicate with the Wazuh Server.

### Solution

Verify the IP address.

Linux

```bash
ip a
```

Windows

```cmd
ipconfig
```

Ping the server.

```cmd
ping <SERVER_IP>
```

Ping the Windows endpoint from Ubuntu.

```bash
ping <WINDOWS_IP>
```

Ensure all virtual machines are connected to the same VirtualBox network.

---

# VirtualBox Issues

## Problem

Virtual machine cannot start.

### Possible Causes

- Insufficient RAM
- Missing virtual disk
- Corrupted VM configuration

### Solution

- Verify RAM allocation.
- Confirm the virtual disk is attached.
- Check VirtualBox settings.
- Restore the VM configuration if needed.

---

## Problem

VM has no network connectivity.

### Solution

Check VirtualBox network settings.

Recommended mode:

```
NAT Network
```

Verify connectivity using:

```bash
ping <TARGET_IP>
```

---

# Dashboard Displays No Alerts

### Possible Causes

- Agent disconnected
- Sysmon not configured
- Rules not triggered

### Solution

Verify:

- Agent status
- Sysmon events
- Wazuh Manager
- Dashboard connection

Generate a test event.

---

# Useful Linux Commands

Update packages.

```bash
sudo apt update
sudo apt upgrade -y
```

Check services.

```bash
sudo systemctl status wazuh-manager

sudo systemctl status wazuh-indexer

sudo systemctl status wazuh-dashboard
```

Restart services.

```bash
sudo systemctl restart wazuh-manager

sudo systemctl restart wazuh-indexer

sudo systemctl restart wazuh-dashboard
```

View logs.

```bash
sudo journalctl -xe
```

---

# Useful Windows Commands

Check IP.

```cmd
ipconfig
```

Ping server.

```cmd
ping <SERVER_IP>
```

Restart Wazuh Agent.

```cmd
NET STOP WazuhSvc

NET START WazuhSvc
```

Check services.

```powershell
Get-Service WazuhSvc

Get-Service Sysmon64
```

---

# Lessons Learned

During the implementation of this SOC Home Lab, several challenges were encountered, including service failures, agent connectivity problems, and VirtualBox networking issues.

Systematic troubleshooting using service status checks, log analysis, and network verification helped identify and resolve these problems. These experiences improved understanding of Linux administration, Windows endpoint management, and SIEM deployment.

---

# Conclusion

Troubleshooting is an essential part of SOC operations. Understanding how to identify service failures, analyze logs, verify network connectivity, and resolve endpoint issues ensures the Wazuh platform operates reliably and continues to detect and monitor security events effectively.

---

# References

- Wazuh Documentation
- Ubuntu Server Documentation
- Microsoft Sysmon Documentation
- Oracle VirtualBox Documentation