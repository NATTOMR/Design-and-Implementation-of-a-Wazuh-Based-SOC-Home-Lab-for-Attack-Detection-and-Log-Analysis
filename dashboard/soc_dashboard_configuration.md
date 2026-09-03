# SOC Operations Dashboard Configuration

This document provides the exact OpenSearch queries, visualizations, and aggregations required to build the SOC Operations Dashboard in the Wazuh UI. 

Since raw NDJSON exports can be difficult to adapt across different environments, follow these manual configuration steps in your Wazuh Dashboard -> OpenSearch Dashboards -> Visualize menu.

---

## 1. Open Alerts & Alert Trends
**Visualization Type:** Metric
**Index Pattern:** `wazuh-alerts-*`
**Query/Filter:** `rule.level: >= 3`

**Metrics:**
- Y-Axis: Count

**Options:**
- Display as: Metric
- Add a secondary visualization (Line Chart) over a Date Histogram (X-Axis: `@timestamp`) to show the Trend.

---

## 2. Alerts by Severity
**Visualization Type:** Pie Chart
**Index Pattern:** `wazuh-alerts-*`
**Query/Filter:** `*`

**Metrics:**
- Slice Size: Count
- Buckets (Split Slices): Terms -> Field: `rule.level`
- Custom Label: Group levels (e.g., 12-15 = Critical, 8-11 = High, 4-7 = Medium).

---

## 3. 24-Hour Alert Timeline
**Visualization Type:** Vertical Bar Chart
**Index Pattern:** `wazuh-alerts-*`
**Query/Filter:** `@timestamp >= "now-24h"`

**Metrics:**
- Y-Axis: Count
- X-Axis: Date Histogram -> Field: `@timestamp` -> Interval: Auto or Hourly

---

## 4. Top Alert Types
**Visualization Type:** Data Table
**Index Pattern:** `wazuh-alerts-*`
**Query/Filter:** `rule.level: >= 5`

**Metrics:**
- Metric: Count
- Buckets (Split Rows): Terms -> Field: `rule.description` -> Size: 10

---

## 5. Failed Login Attempts
**Visualization Type:** Vertical Bar Chart or Metric
**Index Pattern:** `wazuh-alerts-*`
**Query/Filter:** `rule.groups: "authentication_failed" OR rule.id: "4625" OR rule.id: "5716"`

**Metrics:**
- Y-Axis: Count
- X-Axis (if Bar Chart): Date Histogram -> Field: `@timestamp`
- Split Series: Terms -> Field: `data.srcip` (to track attacker IPs)

---

## 6. Malware Detection
**Visualization Type:** Data Table
**Index Pattern:** `wazuh-alerts-*`
**Query/Filter:** `rule.groups: "malware" OR rule.groups: "virus" OR rule.id: "100002"` *(adjust custom rule ID if applicable)*

**Metrics:**
- Metric: Count
- Buckets (Split Rows): Terms -> Field: `data.win.eventdata.image` (for executable name) OR `data.file`

---

## 7. Suspicious PowerShell
**Visualization Type:** Horizontal Bar Chart
**Index Pattern:** `wazuh-alerts-*`
**Query/Filter:** `data.win.eventdata.image: "*powershell.exe" AND rule.level >= 7`

**Metrics:**
- X-Axis: Count
- Y-Axis: Terms -> Field: `data.win.eventdata.commandLine` -> Size: 10

---

## 8. Port Scan Detection
**Visualization Type:** Line Chart
**Index Pattern:** `wazuh-alerts-*`
**Query/Filter:** `rule.groups: "reconnaissance" OR rule.description: "*nmap*"`

**Metrics:**
- Y-Axis: Count
- X-Axis: Date Histogram -> Field: `@timestamp`
- Split Series: Terms -> Field: `data.srcip`

---

## 9. MITRE ATT&CK Tactics
**Visualization Type:** Tag Cloud
**Index Pattern:** `wazuh-alerts-*`
**Query/Filter:** `rule.mitre.tactic: *`

**Metrics:**
- Tag Size: Count
- Tags: Terms -> Field: `rule.mitre.tactic`

---

## 10. MITRE ATT&CK Techniques
**Visualization Type:** Data Table
**Index Pattern:** `wazuh-alerts-*`
**Query/Filter:** `rule.mitre.id: *`

**Metrics:**
- Metric: Count
- Buckets (Split Rows): Terms -> Field: `rule.mitre.id`
- Add Sub-bucket (Split Rows): Terms -> Field: `rule.mitre.technique`

---

## 11. Endpoint & Agent Health
**Visualization Type:** Pie Chart or Metric
**Index Pattern:** `wazuh-monitoring-*` *(Note: requires monitoring index)*
**Query/Filter:** `*`

**Metrics:**
- Slice Size: Count
- Buckets (Split Slices): Terms -> Field: `status` (Online, Disconnected, Never connected)

---

## Mean Time To Respond (MTTR)
**Status:** Planned
*Note: MTTR cannot be visualized using standard Wazuh alerts alone. It requires integration with a ticketing system (e.g., Jira, TheHive) or a SOAR platform to track incident creation and closure times. Once integrated, a custom index (e.g., `incident-metrics-*`) can be used to visualize MTTR using a Metric visualization (Aggregation: Average -> Field: `resolution_time_minutes`).*
