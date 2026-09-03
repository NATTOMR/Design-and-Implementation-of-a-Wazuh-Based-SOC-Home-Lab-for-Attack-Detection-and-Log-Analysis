# SOC Dashboard Metrics

This document defines the target visualizations for the planned SOC Operations Dashboard.

## Target Visualizations

### 1. Alert Summary
- **Open Alerts:** Total count and trend over time.
- **Alerts by Severity:** Breakdown by Critical, High, and Medium severity levels.

### 2. Timeline Analysis
- **Alert Timeline:** Histogram of alerts over the last 24 hours to identify spikes in activity.

### 3. Threat Landscape
- **Top Alert Types:** Frequent alerts (e.g., Failed Login Attempts, Malware Detection, Suspicious PowerShell, Port Scan).
- **MITRE ATT&CK:** Top Tactics and Techniques observed in the environment.

### 4. Environment Health
- **Endpoint Health:** Status of Wazuh agents (Online, Offline, Unhealthy).

## MTTR Calculation
**Status:** Planned

*Mean Time To Respond (MTTR) will only be calculated once a verified source for incident acknowledgement/resolution time (such as a ticketing system or SOAR platform integration) is implemented. Currently, there is no reliable response-time dataset to calculate accurate MTTR values.*
