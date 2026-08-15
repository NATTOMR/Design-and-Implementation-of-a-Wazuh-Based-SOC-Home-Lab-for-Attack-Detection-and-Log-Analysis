# 🎯 Threat Detection & Security Alerting

This directory provides documentation and resources regarding security event detection, alert generation, custom Wazuh rules, and MITRE ATT&CK framework mapping in the **Wazuh-Based SOC Home Lab**.

---

## 📖 Key Documentation & References

- **[Detection Rules Documentation](../docs/Detection-Rules.md)**: Detailed breakdown of Wazuh alert levels, built-in decoders, custom XML detection rules, and alert verification steps.
- **[Custom Rules File](../configs/local_rules.xml)**: Production-ready custom rules XML deployed to the Wazuh Manager.
- **[Custom Decoders File](../configs/local_decoder.xml)**: Custom log regex decoders used to parse specialized security logs.

---

## 🛡️ Target Detection Categories

| Category | Windows Event / Sysmon ID | MITRE ATT&CK Technique | Wazuh Rule SID |
| :--- | :--- | :--- | :--- |
| **Failed Logins / Brute Force** | Event ID 4625 | [T1110 - Brute Force](https://attack.mitre.org/techniques/T1110/) | `60122`, `100003` |
| **Suspicious PowerShell** | Event ID 4688 / Sysmon ID 1 | [T1059.001 - PowerShell](https://attack.mitre.org/techniques/T1059/001/) | `61603`, `100001` |
| **Network Reconnaissance** | Sysmon ID 3 | [T1046 - Network Service Discovery](https://attack.mitre.org/techniques/T1046/) | `61605`, `100002` |
| **Registry Persistence** | Sysmon ID 12 / 13 | [T1112 - Modify Registry](https://attack.mitre.org/techniques/T1112/) | `61613`, `100004` |
| **File Integrity Changes** | Wazuh Syscheck | [T1565 - Data Manipulation](https://attack.mitre.org/techniques/T1565/) | `550`, `554` |

---

## 🔬 Testing Detection Rules

Generate a test alert by triggering a failed login or executing PowerShell on the victim VM, then navigate in the Wazuh Dashboard to:
```
Wazuh Dashboard ➔ Threat Hunting ➔ Security Events
```
Filter by `rule.id` or search for `SOC Lab` to view the generated alert metadata.
