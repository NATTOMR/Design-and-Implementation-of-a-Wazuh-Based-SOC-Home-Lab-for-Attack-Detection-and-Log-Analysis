# Threat Hunting Procedures

This document outlines the standard threat hunting workflows implemented in the Wazuh SOC Home Lab.

## 1. Network Connections & Port Scanning
- Query: `rule.id: "netcat" OR rule.id: "nmap"`
- Target: Detect anomalous network reconnaissance activities originating from internal or external subnets.

## 2. Authentication Monitoring
- Query: `rule.groups: "authentication_failed" AND data.win.system.eventID: "4625"`
- Target: Identify persistent brute-force attacks via RDP or SSH against Windows and Ubuntu endpoints.

## 3. Process Monitoring & Suspicious Execution
- Query: `rule.groups: "sysmon_process_creation" AND (data.win.eventdata.image: "*powershell.exe" OR data.win.eventdata.image: "*cmd.exe")`
- Target: Detect unauthorized living-off-the-land (LotL) execution and potentially encoded payload launches.

## 4. File Integrity Monitoring (FIM)
- Query: `rule.groups: "syscheck" AND syscheck.event: "added"`
- Target: Monitor for unexpected binary droppers in common directories like `C:\Users\Public` or `/tmp`.

## 5. Registry Modifications
- Query: `data.win.system.eventID: "12" OR data.win.system.eventID: "13"`
- Target: Detect persistence mechanisms via AutoRun or service modification registry keys.

These procedures are mapped against the MITRE ATT&CK framework in the `detection-matrix.md` file.
