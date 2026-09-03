# Target Architecture: Threat Intelligence Platform

This document describes the conceptual architecture for the Threat Intelligence Platform extension of the SOC lab.

## Conceptual Data Flow

```
MISP / OTX / abuse.ch / VirusTotal
               │
               ▼ (API / RSS)
       Python TI Collector
       (collect_feeds.py)
               │
               ▼
       IOC Normalization
       (normalize_iocs.py)
               │
               ▼
         Deduplication
      (deduplicate_iocs.py)
               │
               ▼
          Enrichment
        (enrich_iocs.py)
               │
               ▼
       IOC Database / Storage
               │
               ▼
     Wazuh IOC Integration
     (export_wazuh_iocs.py)
               │
               ▼
   Wazuh Detection / Correlation
               │
               ▼
          Wazuh Alerts
               │
               ▼
         Wazuh Dashboard
```

## Supported IOC Types
- IPv4 / IPv6
- Domain / URL
- File Hashes (SHA256, SHA1, MD5)
- Malware Family / Threat Actor Context

*Note: This architecture is "Planned" and represents the target state for integrating external threat intelligence into the Wazuh environment.*
