#!/bin/bash
# GitHub Project Setup Script for Wazuh SOC & Threat Hunting Lab
# Run this script after authenticating with `gh auth login`

export OWNER="NATTOMR"
export REPO="Design-and-Implementation-of-a-Wazuh-Based-SOC-Home-Lab-for-Attack-Detection-and-Log-Analysis"
export PROJECT_ID=2

echo "Setting up GitHub Project #$PROJECT_ID..."

# Update Project Title and Description
gh project edit $PROJECT_ID --owner $OWNER --title "Wazuh SOC & Threat Hunting Lab" --readme "A three-part Wazuh-based Security Operations Center lab for threat detection, threat intelligence integration, threat hunting, and SOC monitoring using Windows, Linux, Sysmon, MITRE ATT&CK, and external threat intelligence sources."

# Note: As of current gh CLI limitations, creating custom fields with specific options
# might require using the GraphQL API or manual UI setup. 
# Please manually ensure these fields exist in the project:
# - Field: Part (Options: Part 1 — Threat Hunting, Part 2 — Threat Intelligence, Part 3 — SOC Dashboard)
# - Field: Priority (Options: Critical, High, Medium, Low)
# - Field: Environment (Options: Kali, Windows, Ubuntu, Wazuh, Threat Intelligence, Dashboard, Documentation)
# - Status (Backlog, Ready, In Progress, Testing, Documentation, Done)

echo "Creating Issues..."

# Array of issues to create
declare -a issues=(
  "P1-01 — Audit Existing Wazuh Deployment|part-1,wazuh,documentation"
  "P1-02 — Verify Wazuh Manager|part-1,wazuh"
  "P1-03 — Verify Wazuh Indexer|part-1,wazuh"
  "P1-04 — Verify Wazuh Dashboard|part-1,dashboard"
  "P1-05 — Verify Windows Agent|part-1,windows"
  "P1-06 — Verify Ubuntu Agent|part-1,ubuntu"
  "P1-07 — Configure Sysmon Telemetry|part-1,sysmon"
  "P1-08 — Configure Windows Event Collection|part-1,windows"
  "P1-09 — Configure PowerShell Logging|part-1,windows"
  "P1-10 — Configure Linux Audit Monitoring|part-1,linux"
  "P1-11 — Implement Nmap Detection|part-1,detection"
  "P1-12 — Implement Authentication Attack Detection|part-1,detection"
  "P1-13 — Implement Suspicious PowerShell Detection|part-1,detection"
  "P1-14 — Implement Process Execution Detection|part-1,detection"
  "P1-15 — Implement File Integrity Detection|part-1,detection"
  "P1-16 — Implement Registry Monitoring|part-1,detection"
  "P1-17 — Map Detections to MITRE ATT&CK|part-1,mitre"
  "P1-18 — Build Threat Hunting Procedures|part-1,threat-hunting"
  "P1-19 — Validate Detection Coverage|part-1,detection"
  "P1-20 — Document Part 1|part-1,documentation"
  "P2-01 — Design Threat Intelligence Architecture|part-2,threat-intelligence,documentation"
  "P2-02 — Integrate MISP|part-2,threat-intelligence"
  "P2-03 — Integrate OTX|part-2,threat-intelligence"
  "P2-04 — Integrate abuse.ch|part-2,threat-intelligence"
  "P2-05 — Design Python TI Collector|part-2,threat-intelligence"
  "P2-06 — Implement Feed Parsing|part-2,threat-intelligence"
  "P2-07 — Implement IOC Normalization|part-2,threat-intelligence"
  "P2-08 — Implement IOC Deduplication|part-2,threat-intelligence"
  "P2-09 — Implement IOC Enrichment|part-2,threat-intelligence"
  "P2-10 — Implement IOC Storage|part-2,threat-intelligence"
  "P2-11 — Integrate IOC Data with Wazuh|part-2,threat-intelligence"
  "P2-12 — Implement IOC Detection Rules|part-2,detection,threat-intelligence"
  "P2-13 — Implement IOC Correlation|part-2,threat-intelligence"
  "P2-14 — Add Threat Intelligence Tests|part-2,threat-intelligence"
  "P2-15 — Document Threat Intelligence Pipeline|part-2,documentation,threat-intelligence"
  "P3-01 — Audit Existing Wazuh Dashboard|part-3,dashboard"
  "P3-02 — Design SOC Dashboard|part-3,dashboard"
  "P3-03 — Create Open Alerts Visualization|part-3,dashboard"
  "P3-04 — Create Severity Visualization|part-3,dashboard"
  "P3-05 — Create 24-Hour Alert Timeline|part-3,dashboard"
  "P3-06 — Create Top Alert Types|part-3,dashboard"
  "P3-07 — Create Failed Login Visualization|part-3,dashboard"
  "P3-08 — Create Malware Detection Visualization|part-3,dashboard"
  "P3-09 — Create PowerShell Detection Visualization|part-3,dashboard"
  "P3-10 — Create Port Scan Visualization|part-3,dashboard"
  "P3-11 — Create MITRE ATT&CK Dashboard|part-3,dashboard,mitre"
  "P3-12 — Create Endpoint Health Dashboard|part-3,dashboard"
  "P3-13 — Create Threat Hunting Dashboard|part-3,dashboard,threat-hunting"
  "P3-14 — Implement SOC Metrics|part-3,soc,dashboard"
  "P3-15 — Implement Verified MTTR Calculation|part-3,soc"
  "P3-16 — Create SOC Dashboard Documentation|part-3,documentation,dashboard"
)

# Loop and create issues
for issue in "${issues[@]}"; do
    TITLE="${issue%%|*}"
    LABELS="${issue##*|}"
    
    echo "Creating issue: $TITLE"
    gh issue create --repo "$OWNER/$REPO" --title "$TITLE" --body "Objective: $TITLE\n\nBackground:\n\nScope:\n\nImplementation steps:\n\nFiles/configurations involved:\n\nDependencies:\n\nAcceptance criteria:\n\nTesting method:\n\nDocumentation requirement:\n\nSecurity considerations:" --label "$LABELS"
done

echo "Issues created successfully. Please manually link them to Project #$PROJECT_ID and set their fields appropriately in the GitHub UI."
