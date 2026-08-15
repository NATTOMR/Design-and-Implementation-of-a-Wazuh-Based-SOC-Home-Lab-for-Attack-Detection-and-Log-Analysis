# ⚙️ Configuration Files

This directory contains the core configuration files used to configure telemetry collection, log routing, custom decoders, and custom detection rules in the **Wazuh-Based SOC Home Lab**.

---

## 📂 Included Configuration Files

| File | Target Location | Description |
| :--- | :--- | :--- |
| [`ossec.conf`](ossec.conf) | `C:\Program Files (x86)\ossec-agent\ossec.conf` | Wazuh Agent configuration for Windows endpoint log channel subscriptions (Security, Sysmon, PowerShell, FIM). |
| [`sysmonconfig.xml`](sysmonconfig.xml) | `C:\Tools\Sysmon\sysmonconfig.xml` | Microsoft Sysmon XML configuration defining event filtering for process creation, network connections, file modifications, and registry events. |
| [`local_rules.xml`](local_rules.xml) | `/var/ossec/etc/rules/local_rules.xml` | Custom Wazuh detection rules for PowerShell execution, port scans, brute-force logins, and registry persistence. |
| [`local_decoder.xml`](local_decoder.xml) | `/var/ossec/etc/decoders/local_decoder.xml` | Custom log decoders for extracting custom event fields before rule matching. |

---

## 🛠️ Usage Instructions

### 1. Applying Sysmon Configuration (Windows Endpoint)
Execute in PowerShell as Administrator:
```powershell
Sysmon64.exe -i C:\Tools\Sysmon\sysmonconfig.xml
```

### 2. Updating Wazuh Agent Configuration (Windows Endpoint)
Replace `ossec.conf` in `C:\Program Files (x86)\ossec-agent\ossec.conf` and restart the agent service:
```powershell
NET STOP WazuhSvc
NET START WazuhSvc
```

### 3. Deploying Custom Rules & Decoders (Ubuntu Wazuh Manager)
Copy rules and decoders to the Wazuh Manager path and restart manager:
```bash
sudo cp local_rules.xml /var/ossec/etc/rules/local_rules.xml
sudo cp local_decoder.xml /var/ossec/etc/decoders/local_decoder.xml
sudo systemctl restart wazuh-manager
```
