# Part 2 — Threat Intelligence Platform

## Goal
Extend Wazuh with an external threat-intelligence pipeline to enrich detection capabilities with known Indicators of Compromise (IOCs).

## Overview
This section outlines the integration of external threat intelligence feeds (MISP, OTX, abuse.ch) into Wazuh. A custom Python-based collector handles the fetching, normalization, deduplication, and export of IOCs for Wazuh integration.

## Note on Implementation
The threat intelligence pipeline is currently **Planned / Partially Implemented**. The foundational structure and Python scripts are provided, but active integration requires proper API keys and live feed access, which are excluded from the repository for security reasons.

## Documentation
- [Architecture](architecture.md)
