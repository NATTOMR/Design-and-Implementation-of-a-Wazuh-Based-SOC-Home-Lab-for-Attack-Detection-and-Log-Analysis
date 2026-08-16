# Wazuh SOC Home Lab — Command Reference

**Last Updated:** August 2026  
**Author:** Natto Muni Chakma  
**Project:** Design and Implementation of a Wazuh-Based SOC Home Lab for Attack Detection and Log Analysis  
**Repository:** [Design-and-Implementation-of-a-Wazuh-Based-SOC-Home-Lab-for-Attack-Detection-and-Log-Analysis](https://github.com/NATTOMR/Design-and-Implementation-of-a-Wazuh-Based-SOC-Home-Lab-for-Attack-Detection-and-Log-Analysis)

---

## 1. Lab Network

The following table details the virtual machines and endpoints operating in the active SOC Home Lab environment:

| Machine | Operating System | IP Address | Role | Wazuh Agent Name | Agent ID | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Wazuh Server** | Ubuntu Server 24.04 LTS | `192.168.100.7` | SIEM Central Manager, Indexer, Dashboard, API | `wazuh-server` *(Manager)* | `000` | Active / Hosting |
| **Kali Linux** | Kali Linux (Agent v4.14.7) | `192.168.100.6` | Attacker Machine & Monitored Linux Endpoint | `hacker01` | `004` | Active / Monitored |
| **Windows Endpoint** | Windows 11 Pro | `192.168.100.8` | Monitored Victim Endpoint (Sysmon + FIM) | `Windows11` | `001` | Active / Monitored |

> [!NOTE]
> **Subnet Addressing Notice:**
> - **Current Live Lab Subnet:** `192.168.100.0/24` (Wazuh Manager: `192.168.100.7`, Kali: `192.168.100.6`, Windows 11: `192.168.100.8`).
> - **[OLD / OUTDATED - Generic Documentation Example Subnet]:** Previous configuration walkthrough templates referenced `10.0.2.0/24` (`10.0.2.15`, `10.0.2.30`, `10.0.2.20`). The authoritative live addresses for all testing and demonstration are in the `192.168.100.0/24` subnet.

---

## 2. Ubuntu Wazuh Server Commands

The following commands are executed on the **Ubuntu Wazuh Server (`192.168.100.7`)**.

---

### Network & System Verification

#### Check IP Address & Network Interfaces
```bash
ip a
```
- **Command:** `ip a`
- **Purpose:** Display all network interface configurations, MAC addresses, and assigned IP addresses (`192.168.100.7`).
- **Expected result:** Output listing `enp0s3` (or equivalent interface) with `inet 192.168.100.7/24`.
- **When to use:** Immediately upon booting or troubleshooting communication issues.

#### Check IP Routing Table
```bash
ip route
```
- **Command:** `ip route`
- **Purpose:** Verify default gateway and local network routing for the `192.168.100.0/24` network.
- **Expected result:** `default via 192.168.100.1 dev enp0s3` and `192.168.100.0/24 dev enp0s3 proto kernel scope link src 192.168.100.7`.
- **When to use:** When endpoint traffic cannot reach the server or when verifying the default gateway.

#### Check Open Ports & Listening Sockets
```bash
sudo ss -tulpn
```
- **Command:** `sudo ss -tulpn`
- **Purpose:** Check all TCP/UDP ports listening on the server.
- **Expected result:** Ports `22` (SSH), `443` (Dashboard), `1514` (Agent Event Channel), `1515` (Agent Registration), `55000` (Wazuh API), and `9200` (Indexer) in `LISTEN` state.
- **When to use:** When an agent cannot connect or dashboard fails to load.

---

### SSH Management

#### Check SSH Service Status
```bash
sudo systemctl status ssh
```
- **Command:** `sudo systemctl status ssh`
- **Purpose:** Check whether the OpenSSH daemon is active and listening for management sessions.
- **Expected result:** `Active: active (running)` with process ID and port 22 binding.
- **When to use:** When unable to connect remotely via SSH to the Ubuntu server.

#### Restart SSH Service
```bash
sudo systemctl restart ssh
```
- **Command:** `sudo systemctl restart ssh`
- **Purpose:** Restart the SSH daemon after configuration changes.
- **Expected result:** Clean restart without errors; active status retained.
- **When to use:** After modifying `/etc/ssh/sshd_config`.

---

### Wazuh Core Services Management

#### Check Wazuh Manager Status
```bash
sudo systemctl status wazuh-manager
```
- **Command:** `sudo systemctl status wazuh-manager`
- **Purpose:** Verify that the core Wazuh Manager engine (`wazuh-analysisd`, `wazuh-remoted`, `wazuh-authd`) is running.
- **Expected result:** `Active: active (running)`.
- **When to use:** Standard health check; after rule or configuration changes.

#### Start / Stop / Restart Wazuh Manager
```bash
# Start
sudo systemctl start wazuh-manager

# Stop
sudo systemctl stop wazuh-manager

# Restart
sudo systemctl restart wazuh-manager
```
- **Command:** `sudo systemctl restart wazuh-manager`
- **Purpose:** Apply new detection rules, decoders, or configuration settings.
- **Expected result:** Services stop and start smoothly; all sub-daemons reloaded.
- **When to use:** Every time `/var/ossec/etc/ossec.conf` or `/var/ossec/etc/rules/local_rules.xml` is modified.

#### Check Wazuh Control Sub-Daemons
```bash
sudo /var/ossec/bin/wazuh-control status
```
- **Command:** `sudo /var/ossec/bin/wazuh-control status`
- **Purpose:** Display the status of every individual Wazuh internal daemon (`wazuh-modulesd`, `wazuh-monitord`, `wazuh-logcollector`, `wazuh-remoted`, `wazuh-syscheckd`, `wazuh-analysisd`, `wazuh-authd`, `wazuh-execd`).
- **Expected result:** `wazuh-modulesd is running...`, `wazuh-analysisd is running...`, etc.
- **When to use:** For granular troubleshooting when `systemctl status wazuh-manager` shows active but specific sub-tasks (like log decoding or alerts) fail.

---

### Wazuh Indexer & Dashboard Management

#### Check Wazuh Indexer Status
```bash
sudo systemctl status wazuh-indexer
```
- **Command:** `sudo systemctl status wazuh-indexer`
- **Purpose:** Verify that OpenSearch / Wazuh Indexer is running and ready to index alerts.
- **Expected result:** `Active: active (running)`.
- **When to use:** When alerts are not showing up in the Dashboard index pattern.

#### Restart Wazuh Indexer
```bash
sudo systemctl restart wazuh-indexer
```
- **Command:** `sudo systemctl restart wazuh-indexer`
- **Purpose:** Restart the indexing engine.
- **Expected result:** Indexer restarts and rebinds to port `9200`.
- **When to use:** When indexing stalls or high memory allocation causes errors.

#### Verify Indexer REST API Response
```bash
curl -k -u admin:admin https://127.0.0.1:9200
```
- **Command:** `curl -k -u admin:<password> https://127.0.0.1:9200`
- **Purpose:** Check local connectivity and cluster health of the indexer.
- **Expected result:** JSON cluster info with `"cluster_name": "wazuh-cluster"` and `"tagline": "The OpenSearch Project: https://opensearch.org/"`.
- **When to use:** To confirm the storage backend is accepting queries.

#### Check Wazuh Dashboard Status
```bash
sudo systemctl status wazuh-dashboard
```
- **Command:** `sudo systemctl status wazuh-dashboard`
- **Purpose:** Verify the web UI service is active.
- **Expected result:** `Active: active (running)`.
- **When to use:** When unable to reach `https://192.168.100.7` in the browser.

#### Restart Wazuh Dashboard
```bash
sudo systemctl restart wazuh-dashboard
```
- **Command:** `sudo systemctl restart wazuh-dashboard`
- **Purpose:** Restart the dashboard web application.
- **Expected result:** Service reboots and listens on port `443`.
- **When to use:** If the web UI crashes, freezes, or fails to render visualizations.

---

### Wazuh API Management

#### Check Wazuh API Authentication Token
```bash
curl -u wazuh-wui:wazuh-wui -k -X POST https://127.0.0.1:55000/security/user/authenticate
```
- **Command:** `curl -u <user>:<pass> -k -X POST https://127.0.0.1:55000/security/user/authenticate`
- **Purpose:** Test that the Wazuh API service is authenticating requests and issuing JSON Web Tokens (JWT).
- **Expected result:** JSON object containing a `{"data": {"token": "eyJhbGciOi..."}}`.
- **When to use:** When dashboard displays "Wazuh API unreachable" or during automated API integration testing.

---

### Wazuh Agent Management (CLI)

#### List All Registered & Active Agents
```bash
sudo /var/ossec/bin/agent_control -l
```
- **Command:** `sudo /var/ossec/bin/agent_control -l`
- **Purpose:** List all agents registered with the manager, their ID, IP, and status.
- **Expected result:**
  ```text
  Wazuh agent_control. List of available agents:
     ID: 000, Name: wazuh-server (server), IP: 127.0.0.1, Active/Local
     ID: 001, Name: Windows11, IP: 192.168.100.8, Active
     ID: 004, Name: hacker01, IP: 192.168.100.6, Active
  ```
- **When to use:** To verify that agents are active and connected.

#### Inspect Specific Agent Details
```bash
# Inspect Kali agent (ID 004)
sudo /var/ossec/bin/agent_control -i 004

# Inspect Windows agent (ID 001)
sudo /var/ossec/bin/agent_control -i 001
```
- **Command:** `sudo /var/ossec/bin/agent_control -i <AGENT_ID>`
- **Purpose:** Show detailed telemetry for an agent, including OS, version, registration IP, last keep-alive, and cryptographic key status.
- **Expected result:** Verbose agent profile indicating version `4.14.7` and `Status: Active`.
- **When to use:** To troubleshoot why an agent is disconnected or verify version sync.

#### List Agents via Manage Agents Tool
```bash
sudo /var/ossec/bin/manage_agents -l
```
- **Command:** `sudo /var/ossec/bin/manage_agents -l`
- **Purpose:** View agent key store records.
- **Expected result:** List of registered agent IDs, names, and IP constraints.
- **When to use:** To verify the client key file `/var/ossec/etc/client.keys`.

#### Remove Stale Agent
> [!CAUTION]
> Removing an agent deletes its registration key. The agent on the remote machine will not reconnect until re-registered.
```bash
sudo /var/ossec/bin/manage_agents -r 003
```
- **Command:** `sudo /var/ossec/bin/manage_agents -r <AGENT_ID>`
- **Purpose:** Remove old, orphaned, or duplicated agent registrations.
- **Expected result:** `Agent '003' removed.`
- **When to use:** When cleaning up duplicate test agents before registering fresh ones.

---

### Wazuh Alerts & Log Monitoring

#### Monitor Real-Time JSON Alerts
```bash
sudo tail -f /var/ossec/logs/alerts/alerts.json
```
- **Command:** `sudo tail -f /var/ossec/logs/alerts/alerts.json`
- **Purpose:** Stream every generated security alert in raw JSON format as it is processed by the rules engine.
- **Expected result:** Real-time stream of JSON objects containing `rule.id`, `agent.name`, `data.srcip`, `rule.description`.
- **When to use:** During live attack simulation to immediately confirm rule triggering.

#### View Recent Standard Alert Log
```bash
sudo tail -n 50 /var/ossec/logs/alerts/alerts.log
```
- **Command:** `sudo tail -n 50 /var/ossec/logs/alerts/alerts.log`
- **Purpose:** Read human-readable alert records formatted by rule level and description.
- **Expected result:** Text alert summaries displaying timestamp, Rule ID, Severity level, and matched log payload.
- **When to use:** For quick CLI inspection of recent alerts without JSON parsing.

#### View Wazuh Manager Internal Server Log
```bash
sudo tail -n 100 /var/ossec/logs/ossec.log
```
- **Command:** `sudo tail -n 100 /var/ossec/logs/ossec.log`
- **Purpose:** Review internal manager operations, agent connections, log rotation, and internal errors.
- **Expected result:** Log lines tagged `wazuh-remoted`, `wazuh-analysisd`, `wazuh-authd`.
- **When to use:** When agents fail to register or rules fail to compile.

#### Real-Time Log Testing via wazuh-logtest
```bash
sudo /var/ossec/bin/wazuh-logtest
```
- **Command:** `sudo /var/ossec/bin/wazuh-logtest`
- **Purpose:** Interactive utility to test how a raw log string is decoded and what rule triggers.
- **Expected result:** Interactive prompt `Type one log per line`. Enter a sample syslog or event log to see Phase 1 (pre-decoding), Phase 2 (decoding), and Phase 3 (rule firing).
- **When to use:** When crafting custom rules in `/var/ossec/etc/rules/local_rules.xml` or custom decoders.

---

## 3. Kali Wazuh Agent Commands

The following commands are executed on the **Kali Linux Agent (`192.168.100.6`)** (Agent Name: `hacker01`, ID: `004`, Wazuh Agent v4.14.7).

---

### Network & Host Verification

#### Check Kali IP Address
```bash
ip a
```
- **Command:** `ip a`
- **Purpose:** Confirm the local network interface IP is `192.168.100.6`.
- **Expected result:** `inet 192.168.100.6/24` under `eth0` or `enp0s3`.
- **When to use:** First step before testing or attack simulation.

#### Test Connectivity to Wazuh Manager
```bash
# ICMP ping test
ping -c 4 192.168.100.7

# Test Wazuh Agent Communication Port (1514)
nc -zvw3 192.168.100.7 1514

# Test Wazuh Agent Registration Port (1515)
nc -zvw3 192.168.100.7 1515
```
- **Command:** `ping -c 4 192.168.100.7` and `nc -zvw3 192.168.100.7 1514`
- **Purpose:** Verify basic IP routing and confirm TCP ports 1514 and 1515 are reachable without firewall filtering.
- **Expected result:** `0% packet loss` on ping and `Connection to 192.168.100.7 1514 port [tcp/*] succeeded!`.
- **When to use:** Before agent installation and when agent status shows disconnected.

---

### Agent Installation & Dependency Resolution

#### Install Wazuh Agent Package with Pre-Configured Manager
```bash
# Add Wazuh Repository GPG key and repo (if using apt)
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import && sudo chmod 644 /usr/share/keyrings/wazuh.gpg
echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee -a /etc/apt/sources.list.d/wazuh.list
sudo apt update

# Install agent with environment variables
sudo WAZUH_MANAGER='192.168.100.7' WAZUH_AGENT_NAME='hacker01' apt install -y wazuh-agent
```
- **Command:** `sudo WAZUH_MANAGER='192.168.100.7' WAZUH_AGENT_NAME='hacker01' apt install -y wazuh-agent`
- **Purpose:** Install Wazuh Agent `4.14.7` and configure the manager destination and agent name.
- **Expected result:** Package installs successfully, creating `/var/ossec/` structure.
- **When to use:** Initial endpoint deployment.

#### Fix Missing / Broken Dependencies
```bash
sudo apt-get install -f
sudo apt-get install --reinstall adduser procps
```
- **Command:** `sudo apt-get install -f` and `sudo apt-get install --reinstall adduser procps`
- **Purpose:** Resolve dependency configuration issues where `adduser` or `procps` prevented the `wazuh-agent` post-installation scripts from completing.
- **Expected result:** Dependencies configured cleanly; `dpkg` finishes without errors.
- **When to use:** If `wazuh-agent` installation fails during user/group creation.

---

### Agent Configuration & Verification

#### Edit / Verify Manager IP in Configuration
```bash
# View current manager IP block
sudo grep -A 4 "<server>" /var/ossec/etc/ossec.conf
```
- **Command:** `sudo grep -A 4 "<server>" /var/ossec/etc/ossec.conf`
- **Purpose:** Ensure `<address>192.168.100.7</address>` is configured instead of the placeholder `MANAGER_IP`.
- **Expected result:**
  ```xml
  <server>
    <address>192.168.100.7</address>
    <port>1514</port>
    <protocol>tcp</protocol>
  </server>
  ```
- **When to use:** Whenever the agent fails to start with "Invalid server address".

#### Validate Wazuh Agent Configuration Syntax
```bash
sudo /var/ossec/bin/wazuh-agentd -t
```
- **Command:** `sudo /var/ossec/bin/wazuh-agentd -t`
- **Purpose:** Test `/var/ossec/etc/ossec.conf` XML syntax before restarting the service.
- **Expected result:** Silent return (exit code 0) or `Configuration file is OK`.
- **When to use:** Before every agent restart after editing `ossec.conf`.

---

### Service Lifecycle & Status

#### Enable & Start Wazuh Agent
```bash
# Enable at boot
sudo systemctl enable wazuh-agent

# Start service
sudo systemctl start wazuh-agent
```
- **Command:** `sudo systemctl enable wazuh-agent && sudo systemctl start wazuh-agent`
- **Purpose:** Set the agent service to auto-start on boot and start it immediately.
- **Expected result:** `Synchronizing state of wazuh-agent.service...` and service active.
- **When to use:** Following installation or configuration repair.

#### Check Wazuh Agent Service Status
```bash
sudo systemctl status wazuh-agent
```
- **Command:** `sudo systemctl status wazuh-agent`
- **Purpose:** Check if `wazuh-agentd` is currently active and running.
- **Expected result:** `Active: active (running)`.
- **When to use:** Routine status check or during connectivity troubleshooting.

#### Restart Wazuh Agent Service
```bash
sudo systemctl restart wazuh-agent
```
- **Command:** `sudo systemctl restart wazuh-agent`
- **Purpose:** Reload agent daemon and re-read configuration changes.
- **Expected result:** Service stops and starts cleanly without timeout.
- **When to use:** After adding new `<localfile>` log collectors.

---

### Agent Logs & Logcollector Monitoring

#### View Real-Time Agent Logs
```bash
sudo tail -f /var/ossec/logs/ossec.log
```
- **Command:** `sudo tail -f /var/ossec/logs/ossec.log`
- **Purpose:** Monitor agent communications, connection state, keep-alive exchanges, and errors.
- **Expected result:** Lines stating `wazuh-agentd: INFO: Connected to the server (192.168.100.7:1514/tcp)`.
- **When to use:** To verify the agent successfully authenticated and connected to the manager.

#### Check Logcollector Status for auth.log
```bash
sudo grep -i "logcollector" /var/ossec/logs/ossec.log | tail -n 20
```
- **Command:** `sudo grep -i "logcollector" /var/ossec/logs/ossec.log | tail -n 20`
- **Purpose:** Confirm that the logcollector daemon is actively monitoring configured target files.
- **Expected result:** `wazuh-logcollector: INFO: Monitoring file: '/var/log/auth.log'`.
- **When to use:** To confirm new log files are being harvested.

---

### Authentication Log & SSH Configuration (Kali)

#### Enable rsyslog for Authentication Logging
```bash
sudo apt update && sudo apt install -y rsyslog
sudo systemctl enable --now rsyslog
```
- **Command:** `sudo apt install -y rsyslog && sudo systemctl enable --now rsyslog`
- **Purpose:** Kali Linux does not create `/var/log/auth.log` by default under pure systemd-journald; installing and enabling `rsyslog` generates `/var/log/auth.log` for authentication event forwarding.
- **Expected result:** `Active: active (running)` for `rsyslog.service` and `/var/log/auth.log` is created.
- **When to use:** Initial setup when `/var/log/auth.log` is missing.

#### Monitor Authentication Logs in Real Time
```bash
sudo tail -f /var/log/auth.log
```
- **Command:** `sudo tail -f /var/log/auth.log`
- **Purpose:** View local SSH/authentication attempts, sudo invocations, and session events.
- **Expected result:** Real-time log lines showing `sshd[...]: Failed password for invalid user wronguser from 192.168.100.7 port ...`.
- **When to use:** During failed login / brute force attack simulations.

#### Inspect SSH Service & Configuration
```bash
# Check SSH daemon status
sudo systemctl status ssh

# Check SSH authentication directives
sudo grep -E "PasswordAuthentication|PermitRootLogin" /etc/ssh/sshd_config /etc/ssh/sshd_config.d/* 2>/dev/null
```
- **Command:** `sudo systemctl status ssh`
- **Purpose:** Ensure SSH is active and accepting password authentication for simulation.
- **Expected result:** SSH is active and `PasswordAuthentication yes` is enabled.
- **When to use:** Before executing SSH attack simulations from Ubuntu to Kali.

---

## 4. Windows Wazuh Agent Commands

The following commands are used on the **Windows 11 Monitored Endpoint (`192.168.100.8`)**.

---

### PowerShell Commands (Run as Administrator)

#### Check Wazuh Agent Service Status
```powershell
Get-Service -Name WazuhSvc
```
- **Command:** `Get-Service -Name WazuhSvc`
- **Purpose:** Check whether the Windows Wazuh Agent service is running, stopped, or paused.
- **Expected result:** `Status: Running`, `Name: WazuhSvc`, `DisplayName: Wazuh`.
- **When to use:** Routine health check.

#### Detailed Service Property Inspection
```powershell
Get-Service -Name WazuhSvc | Select-Object Name, DisplayName, Status, StartType
```
- **Command:** `Get-Service -Name WazuhSvc | Select-Object Name, DisplayName, Status, StartType`
- **Purpose:** Verify the service startup type is set to `Automatic`.
- **Expected result:** `Status: Running`, `StartType: Automatic`.
- **When to use:** To verify the agent will survive a reboot.

#### Start / Stop / Restart Wazuh Service
```powershell
# Start
Start-Service -Name WazuhSvc

# Stop
Stop-Service -Name WazuhSvc

# Restart
Restart-Service -Name WazuhSvc
```
- **Command:** `Restart-Service -Name WazuhSvc`
- **Purpose:** Restart the agent after modifying `ossec.conf` or Sysmon logging.
- **Expected result:** Service cycles and returns to `Running`.
- **When to use:** Following configuration changes in `C:\Program Files (x86)\ossec-agent\ossec.conf`.

#### Test Network Connectivity to Wazuh Manager
```powershell
# Test Agent Event Channel Port (1514)
Test-NetConnection -ComputerName 192.168.100.7 -Port 1514

# Test Agent Registration Port (1515)
Test-NetConnection -ComputerName 192.168.100.7 -Port 1515
```
- **Command:** `Test-NetConnection -ComputerName 192.168.100.7 -Port 1514`
- **Purpose:** Validate end-to-end TCP connectivity from Windows to Ubuntu.
- **Expected result:** `TcpTestSucceeded : True`.
- **When to use:** When the Windows agent shows "Disconnected" in the Wazuh Dashboard.

#### Query Windows Security Event ID 4625 (Failed Logon)
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 5 | Format-List TimeCreated, Id, Message
```
- **Command:** `Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 5`
- **Purpose:** Inspect recent failed logon security events on the local Windows endpoint.
- **Expected result:** Formatted output showing timestamp, Account Name, Failure Reason, and Caller Process.
- **When to use:** To verify local event generation before checking if Wazuh captured it.

#### Read Wazuh Agent Windows Logs
```powershell
# Read recent 50 lines
Get-Content "C:\Program Files (x86)\ossec-agent\ossec.log" -Tail 50

# Stream logs in real time
Get-Content "C:\Program Files (x86)\ossec-agent\ossec.log" -Wait -Tail 20
```
- **Command:** `Get-Content "C:\Program Files (x86)\ossec-agent\ossec.log" -Tail 50`
- **Purpose:** View agent internal status, keep-alive signals, and event channel collection errors.
- **Expected result:** `wazuh-agent: INFO: Connected to the server (192.168.100.7:1514/tcp)`.
- **When to use:** Diagnostic troubleshooting when agent is offline.

#### Check Sysmon Service Status
```powershell
Get-Service -Name Sysmon64
```
- **Command:** `Get-Service -Name Sysmon64`
- **Purpose:** Verify Microsoft Sysmon is active and capturing process creation and network events.
- **Expected result:** `Status: Running`.
- **When to use:** When process-level telemetry is missing from Wazuh alerts.

#### Silent MSI Installation / Reinstallation via PowerShell
```powershell
msiexec.exe /i wazuh-agent-4.14.7-1.msi /q WAZUH_MANAGER="192.168.100.7" WAZUH_AGENT_NAME="Windows11" WAZUH_REGISTRATION_SERVER="192.168.100.7"
```
- **Command:** `msiexec.exe /i ...`
- **Purpose:** Perform automated silent installation of the Windows Wazuh Agent.
- **Expected result:** Agent installed silently into `C:\Program Files (x86)\ossec-agent\`.
- **When to use:** Initial setup or clean reinstallation.

---

### Command Prompt (CMD) Commands (Run as Administrator)

#### Check Service Status via SC
```cmd
sc query WazuhSvc
```
- **Command:** `sc query WazuhSvc`
- **Purpose:** Query the Windows Service Control manager directly.
- **Expected result:** `STATE : 4 RUNNING`.
- **When to use:** Quick status check from CMD.

#### Start / Stop Service via NET
```cmd
net stop WazuhSvc
net start WazuhSvc
```
- **Command:** `net stop WazuhSvc && net start WazuhSvc`
- **Purpose:** Classical command-line service restart.
- **Expected result:** `The Wazuh service was stopped successfully.` / `The Wazuh service was started successfully.`
- **When to use:** Routine agent restart.

#### Ping Manager from CMD
```cmd
ping 192.168.100.7
```
- **Command:** `ping 192.168.100.7`
- **Purpose:** Verify ICMP reachability to the Wazuh Server.
- **Expected result:** `Reply from 192.168.100.7: bytes=32 time<1ms TTL=64`.
- **When to use:** Basic network connectivity verification.

#### Query Security Log Events via Wevtutil
```cmd
wevtutil qe Security "/q:*[System[(EventID=4625)]]" /c:3 /rd:true /f:text
```
- **Command:** `wevtutil qe Security ...`
- **Purpose:** Query the 3 most recent Event ID 4625 events from CMD.
- **Expected result:** Formatted text block with event XML details.
- **When to use:** When PowerShell is restricted or unavailable.

---

## 5. Connectivity Testing Matrix

The following matrix documents the connectivity tests performed across the home lab network, showing the exact command, source, destination, and expected outcome.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           VirtualBox Subnet                             │
│                           192.168.100.0/24                              │
│                                                                         │
│   Ubuntu Wazuh Server           Kali Linux (Agent)         Windows 11   │
│     192.168.100.7                  192.168.100.6          192.168.100.8 │
│          │                              │                       │       │
│          ├────── ICMP / SSH (22) ───────┤                       │       │
│          ├────── Agent Comms (1514) ────┼───────────────────────┤       │
│          └────── Registration (1515) ───┴───────────────────────┘       │
└─────────────────────────────────────────────────────────────────────────┘
```

### Directional Test Commands

#### Direction: Ubuntu (`192.168.100.7`) ➔ Kali (`192.168.100.6`)
```bash
# 1. ICMP Ping Test
ping -c 4 192.168.100.6

# 2. SSH Port Check
nc -zvw3 192.168.100.6 22

# 3. ARP Cache Resolution
arp -n | grep 192.168.100.6
```
- **Purpose:** Verify server can reach the Kali attacker/agent machine and confirm ARP table resolution.
- **Expected Result:** Ping replies with 0% loss; port 22 open; valid MAC address resolved in ARP table.

#### Direction: Kali (`192.168.100.6`) ➔ Ubuntu Manager (`192.168.100.7`)
```bash
# 1. ICMP Ping Test
ping -c 4 192.168.100.7

# 2. Test Agent Event Port (1514)
nc -zvw3 192.168.100.7 1514

# 3. Test Agent Registration Port (1515)
nc -zvw3 192.168.100.7 1515

# 4. Test Dashboard Web Port (443)
nc -zvw3 192.168.100.7 443
```
- **Purpose:** Confirm agent communication channels to the SIEM server are open and unobstructed.
- **Expected Result:** Succeeded status on all target ports.

#### Direction: Windows (`192.168.100.8`) ➔ Ubuntu Manager (`192.168.100.7`)
```powershell
# 1. ICMP Ping Test
Test-Connection -ComputerName 192.168.100.7 -Count 4

# 2. Test TCP Port 1514
Test-NetConnection -ComputerName 192.168.100.7 -Port 1514

# 3. View ARP Table
Get-NetNeighbor -IPAddress 192.168.100.7
```
- **Purpose:** Verify Windows endpoint can forward security telemetry to the Wazuh Manager.
- **Expected Result:** `Ping succeeded`; `TcpTestSucceeded : True`; ARP neighbor in `Reachable` state.

#### Direction: Kali (`192.168.100.6`) ➔ Windows Endpoint (`192.168.100.8`)
```bash
# 1. ICMP Ping Test
ping -c 4 192.168.100.8

# 2. TCP Port Scan (Nmap SYN scan)
sudo nmap -sS -p 135,139,445,3389 192.168.100.8
```
- **Purpose:** Perform attack reconnaissance from attacker machine against the Windows victim.
- **Expected Result:** Open/Filtered port states returned; generates network alerts in Wazuh.

---

## 6. Failed Login / Attack Simulation & Event Flow

This section details the controlled attack simulations executed in the lab to generate authentication failure alerts.

---

### Step-by-Step Simulation Procedure

#### Step 1: Execute Attack from Ubuntu (or Kali) against Kali SSH
On the **Ubuntu Server (`192.168.100.7`)**, intentionally execute a failed SSH login against **Kali (`192.168.100.6`)**:
```bash
ssh wronguser@192.168.100.6
```
*(Enter an arbitrary incorrect password when prompted).*

#### Step 2: Verify Local Log on Endpoint (Kali)
On the **Kali Agent (`192.168.100.6`)**, check that `rsyslog` recorded the failure:
```bash
sudo tail -n 20 /var/log/auth.log
```
**Expected Endpoint Log Entry:**
```text
sshd[12345]: Failed password for invalid user wronguser from 192.168.100.7 port 54321 ssh2
sshd[12345]: Connection closed by invalid user wronguser 192.168.100.7 port 54321 [preauth]
```

#### Step 3: Verify Real-Time Alert Generation on Wazuh Manager
On the **Ubuntu Wazuh Server (`192.168.100.7`)**, monitor the alerts stream:
```bash
sudo tail -f /var/ossec/logs/alerts/alerts.json | grep -i "wronguser"
```
**Expected Alert Output (JSON):**
```json
{
  "timestamp": "2026-08-17T02:00:00.000+0000",
  "rule": {
    "level": 5,
    "description": "sshd: Attempt to login using a non-existent user",
    "id": "5710",
    "mitre": {
      "id": ["T1110.001"],
      "tactic": ["Credential Access"],
      "technique": ["Password Guessing"]
    }
  },
  "agent": {
    "id": "004",
    "name": "hacker01",
    "ip": "192.168.100.6"
  },
  "data": {
    "srcip": "192.168.100.7",
    "dstuser": "wronguser"
  }
}
```

#### Step 4: Windows Failed Logon Simulation (Event ID 4625)
On the **Windows 11 Endpoint (`192.168.100.8`)**, generate a failed logon via PowerShell:
```powershell
# Attempt authentication with invalid credentials
$cred = New-Object System.Management.Automation.PSCredential ("FakeUser", (ConvertTo-SecureString "WrongPass123!" -AsPlainText -Force))
Start-Process powershell -Credential $cred
```
Verify local event generation:
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 1 | Format-List
```

---

### Complete End-to-End Event Flow

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                          SOC DETECTION WORKFLOW                                │
└────────────────────────────────────────────────────────────────────────────────┘

 1. Attack / Test Generation
    └── Ubuntu / Attacker executes: ssh wronguser@192.168.100.6
        │
        ▼
 2. Endpoint Log Generation
    └── Linux: /var/log/auth.log records "Failed password for invalid user"
    └── Windows: Windows Security Event Log records Event ID 4625
        │
        ▼
 3. Wazuh Agent Collection (wazuh-logcollector)
    └── Agent reads the log file/channel and transmits event over TCP 1514 (AES encrypted)
        │
        ▼
 4. Wazuh Manager Processing (wazuh-analysisd)
    └── Phase 1: Pre-decoding (Timestamp, hostname, program_name: sshd)
    └── Phase 2: Decoding (Extracts srcip: 192.168.100.7, dstuser: wronguser)
    └── Phase 3: Rules Engine Evaluation (Rule ID 5710 / Level 5 triggers)
        │
        ▼
 5. Alert Generation & Storage
    └── Manager writes alert to /var/ossec/logs/alerts/alerts.json & alerts.log
    └── Filebeat / Indexer ingests alert into OpenSearch cluster
        │
        ▼
 6. Wazuh Dashboard Visualization
    └── Security alert appears in Threat Hunting / Security Events dashboard
    └── Mapped to MITRE ATT&CK T1110 (Brute Force / Password Guessing)
```

### Visual Verification & Dashboard Evidence

The following dashboard captures confirm real-time ingestion, threat hunting analysis, and security event categorization across endpoints:

#### 1. Kali Linux Agent (`hacker01` / `004`) — Initial Ingestion
![Kali Agent Initial Ingestion](../screenshots/20-kali-agent-threat-hunting.png)
*Initial telemetry, Security Configuration Assessment (SCA), and system metrics streaming to the Wazuh Manager.*

#### 2. Kali Linux Agent (`hacker01` / `004`) — Multi-Source Log Telemetry
![Kali Agent Log Telemetry](../screenshots/21-kali-agent-log-telemetry.png)
*Active log collection across `syslog`, `dpkg`, `sca`, and `config_changed` rule groups (214 security events captured).*

#### 3. Threat Hunting Events Breakdown
![Threat Hunting Events Breakdown](../screenshots/22-agent-threat-hunting-events.png)
*Granular event log analysis displaying Rule ID mappings (61104, 60642, 19009, 61102), service changes, and CIS security benchmarks.*

---

## 7. Diagnostic & Troubleshooting Reference

The following table summarizes the primary diagnostic tools and what failure modes they identify:

| Command | Target System | Problem / Failure Mode It Diagnoses |
| :--- | :--- | :--- |
| `sudo systemctl status wazuh-manager` | Ubuntu Server | Identifies if the core manager service is stopped, crashed, or failing systemd health checks. |
| `sudo journalctl -u wazuh-manager -xe` | Ubuntu Server | Reveals detailed kernel/system errors, missing configuration files, and stack traces on startup crash. |
| `sudo /var/ossec/bin/wazuh-control status` | Ubuntu Server | Shows which specific internal sub-daemon (`wazuh-analysisd`, `wazuh-remoted`, etc.) failed to launch. |
| `sudo /var/ossec/bin/wazuh-agentd -t` | Kali / Linux Agent | Validates XML syntax and detects illegal XML tags in `/var/ossec/etc/ossec.conf` before service start. |
| `sudo tail -f /var/ossec/logs/ossec.log` | Kali / Linux Agent | Diagnoses agent connection failures, handshake timeouts, and encryption key mismatches. |
| `sudo ss -tulpn \| grep -E '1514\|1515'` | Ubuntu Server | Confirms if Wazuh daemon is actively listening for incoming agent registration and log shipping. |
| `nc -zvw3 192.168.100.7 1514` | Kali / Linux Agent | Tests for network firewalls (UFW, iptables) blocking agent-to-manager network traffic. |
| `Test-NetConnection -Port 1514` | Windows Endpoint | Diagnoses Windows Defender Firewall or VirtualBox NAT network blocks between Windows and Ubuntu. |
| `Get-WinEvent -LogName Security` | Windows Endpoint | Validates whether Windows is generating audit events locally before checking Wazuh forwarding. |
| `sudo /var/ossec/bin/wazuh-logtest` | Ubuntu Server | Tests regex decoders and rule hierarchies against raw log samples without restarting the manager. |

---

## 8. Common Problems Encountered & Solutions

This section documents the actual technical issues encountered during the build, their root causes, and verified fixes.

---

### Problem 1: Wazuh Agent Package Dependency Failure during Installation
- **Problem:** When installing the Wazuh agent `.deb` package on Kali Linux, installation halted with dependency and configuration errors regarding `adduser` and `procps`.
- **Cause:** Kali's package database had unconfigured pre-dependency states, preventing the package post-installation script from adding the `wazuh` system user and reading process states.
- **Command used to diagnose:**
  ```bash
  sudo dpkg -i wazuh-agent_4.14.7-1_amd64.deb
  ```
- **Fix:**
  ```bash
  sudo apt-get update
  sudo apt-get install -f
  sudo apt-get install --reinstall adduser procps
  ```
- **Verification:**
  ```bash
  dpkg -l | grep wazuh-agent
  ```
  *(Status shows `ii  wazuh-agent` confirming successful installation).*

---

### Problem 2: Wazuh Agent Startup Failure (`Invalid server address found: 'MANAGER_IP'`)
- **Problem:** The `wazuh-agent` service failed to start on Kali Linux.
- **Cause:** The default configuration file `/var/ossec/etc/ossec.conf` retained the unpopulated template placeholder string `'MANAGER_IP'` instead of the actual manager IP address.
- **Command used to diagnose:**
  ```bash
  sudo systemctl status wazuh-agent
  sudo tail -n 20 /var/ossec/logs/ossec.log
  ```
- **Fix:**
  Edited `/var/ossec/etc/ossec.conf` and updated the `<address>` block:
  ```xml
  <!-- BEFORE -->
  <server>
    <address>MANAGER_IP</address>
    <port>1514</port>
    <protocol>tcp</protocol>
  </server>

  <!-- AFTER -->
  <server>
    <address>192.168.100.7</address>
    <port>1514</port>
    <protocol>tcp</protocol>
  </server>
  ```
  *Or via sed command:*
  ```bash
  sudo sed -i 's/<address>MANAGER_IP<\/address>/<address>192.168.100.7<\/address>/g' /var/ossec/etc/ossec.conf
  ```
- **Verification:**
  ```bash
  sudo /var/ossec/bin/wazuh-agentd -t
  sudo systemctl restart wazuh-agent
  sudo systemctl status wazuh-agent
  ```

---

### Problem 3: Kali Missing `/var/log/auth.log` for Authentication Monitoring
- **Problem:** Authentication attempts and failed logins on Kali Linux were not being recorded in `/var/log/auth.log`.
- **Cause:** Modern Debian/Kali installations utilize `systemd-journald` exclusively by default and do not install the traditional `rsyslog` service that writes `/var/log/auth.log`.
- **Command used to diagnose:**
  ```bash
  ls -la /var/log/auth.log
  ```
  *(Returned: `ls: cannot access '/var/log/auth.log': No such file or directory`).*
- **Fix:**
  Installed and enabled the `rsyslog` daemon:
  ```bash
  sudo apt update
  sudo apt install -y rsyslog
  sudo systemctl enable --now rsyslog
  ```
- **Verification:**
  ```bash
  sudo systemctl status rsyslog
  ls -la /var/log/auth.log
  ```
  *(File `/var/log/auth.log` is created and populated with authentication events).*

---

### Problem 4: Wazuh Agent Not Monitoring `/var/log/auth.log`
- **Problem:** Even after `auth.log` was populated on Kali, authentication failures were not appearing on the Wazuh Manager.
- **Cause:** The default `ossec.conf` on the agent did not have an active `<localfile>` block targeting `/var/log/auth.log`.
- **Command used to diagnose:**
  ```bash
  sudo grep -i "auth.log" /var/ossec/etc/ossec.conf
  ```
- **Fix:**
  Added the following `<localfile>` configuration block inside the `<ossec_config>` section of `/var/ossec/etc/ossec.conf`:
  ```xml
  <localfile>
    <log_format>syslog</log_format>
    <location>/var/log/auth.log</location>
  </localfile>
  ```
- **Verification:**
  Validated configuration and restarted the agent:
  ```bash
  # Step 1: Validate syntax
  sudo /var/ossec/bin/wazuh-agentd -t

  # Step 2: Restart agent
  sudo systemctl restart wazuh-agent

  # Step 3: Check logcollector confirmation
  sudo grep -i "auth.log" /var/ossec/logs/ossec.log
  ```
  *(Output confirms: `wazuh-logcollector: INFO: Monitoring file: '/var/log/auth.log'`)*.

---

## 9. Quick Command Cheat Sheet

A compact reference of high-frequency commands for everyday SOC lab operation:

### 🐧 Ubuntu Wazuh Server (`192.168.100.7`)
```bash
# Check status of all Wazuh stack services
sudo systemctl status wazuh-manager wazuh-indexer wazuh-dashboard

# Restart core Wazuh Manager
sudo systemctl restart wazuh-manager

# List all active/registered agents
sudo /var/ossec/bin/agent_control -l

# Stream real-time security alerts (JSON)
sudo tail -f /var/ossec/logs/alerts/alerts.json

# Test log decoding & rule triggering interactively
sudo /var/ossec/bin/wazuh-logtest
```

### 🐉 Kali Linux Agent (`192.168.100.6` | Agent: `hacker01` | ID: `004`)
```bash
# Validate agent configuration syntax
sudo /var/ossec/bin/wazuh-agentd -t

# Restart Wazuh Agent
sudo systemctl restart wazuh-agent

# Check agent service status
sudo systemctl status wazuh-agent

# Monitor local authentication log
sudo tail -20 /var/log/auth.log

# View agent connection log
sudo tail -30 /var/ossec/logs/ossec.log
```

### 💻 Windows 11 Agent (`192.168.100.8` | Agent: `Windows11` | ID: `001`)
```powershell
# PowerShell (Run as Administrator)
# Check agent service status
Get-Service WazuhSvc

# Restart agent service
Restart-Service WazuhSvc

# Test port connectivity to Manager
Test-NetConnection -ComputerName 192.168.100.7 -Port 1514

# Query latest failed logon events
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} -MaxEvents 5 | Format-Table

# View recent agent logs
Get-Content "C:\Program Files (x86)\ossec-agent\ossec.log" -Tail 30
```

```cmd
:: Command Prompt (Run as Administrator)
:: Restart agent service
net stop WazuhSvc && net start WazuhSvc

:: Query service state
sc query WazuhSvc
```

---

## 10. Documentation Rules & Standards

This command reference adheres to the following engineering and cybersecurity documentation standards:

1. **Explicit Machine Context:** Every command is strictly organized under the specific operating system and network identity where it executes.
2. **Copy-Paste Readiness:** All code blocks contain syntactically valid, copy-pasteable commands with exact lab parameters.
3. **No Destructive Operations:** Potentially disruptive operations (such as agent removal) are isolated, highlighted with markdown alert boxes (`[!CAUTION]`), and explicitly explained before execution.
4. **Authoritative Network Data:** Real lab network coordinates (`192.168.100.0/24`) are preserved; outdated placeholder subnets (`10.0.2.0/24`) are flagged with `[OLD / OUTDATED]` markers.
5. **Portfolio Integrity:** Formatted in professional GitHub Flavored Markdown with clean tables, structured workflows, and MITRE ATT&CK taxonomy for cybersecurity portfolio presentations.
