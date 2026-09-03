# Part 1 — Threat Hunting Lab

## Goal
Build a realistic multi-host threat-hunting environment where controlled security events are generated and collected by Wazuh.

## Overview
This section focuses on the native Wazuh SIEM capabilities, endpoint monitoring, and attack simulation to generate security alerts.

## Target Architecture
The architecture comprises a Kali Linux attack machine and monitored endpoints (Windows and Ubuntu) reporting telemetry (Sysmon, Auditd, Event Logs) to the Wazuh Manager.

See [Architecture](architecture.md) for detailed diagrams.

## Documentation
- [Architecture](architecture.md)
- [Attack Scenarios](attack-scenarios.md)
- [Threat Hunting](threat-hunting.md)
- [Detection Matrix (MITRE ATT&CK)](detection-matrix.md)
