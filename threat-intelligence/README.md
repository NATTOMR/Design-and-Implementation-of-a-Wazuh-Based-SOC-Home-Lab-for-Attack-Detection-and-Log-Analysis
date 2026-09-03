# Threat Intelligence Pipeline

This module represents Part 2 of the Wazuh SOC Home Lab project. It is designed to fetch, normalize, and integrate external threat intelligence into Wazuh.

## Directory Structure
- `collectors/`: Scripts to pull data from MISP, OTX, abuse.ch.
- `normalizers/`: Scripts to convert feed data into a standard JSON schema.
- `deduplication/`: Scripts to prevent redundant IOCs.
- `enrichment/`: Scripts to query VirusTotal or other sources for context.
- `ioc/`: Export scripts for Wazuh CDB lists.
- `config/`: Environment variables (`.env.example`).
- `database/`: Scripts for local IOC storage (e.g., PostgreSQL).

## Usage
*Note: This component is currently in the planning/placeholder phase. Do not execute these scripts in a production environment without proper testing and configuration.*

1. Copy `config/.env.example` to `config/.env`.
2. Add your API keys.
3. (Planned) Run `collect_feeds.py` to initiate the pipeline.
