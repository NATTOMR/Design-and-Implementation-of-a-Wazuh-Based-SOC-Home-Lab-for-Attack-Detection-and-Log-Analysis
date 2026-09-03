"""
Threat Intelligence Collector - Feed Fetching

This script is responsible for pulling indicators of compromise (IOCs) from various external sources
such as MISP, AlienVault OTX, and abuse.ch.

Security Note:
Do NOT hardcode API credentials in this file.
Always use environment variables or a secure configuration file (.env).
"""

import os
import sys
from dotenv import load_dotenv

# Try to import libraries, but allow graceful failure if not installed
try:
    from pymisp import ExpandedPyMISP
except ImportError:
    ExpandedPyMISP = None

try:
    from OTXv2 import OTXv2
except ImportError:
    OTXv2 = None

# Load environment variables from config/.env
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', '.env')
load_dotenv(env_path)

def fetch_misp_iocs():
    """Fetches recent network and file-hash IOCs from MISP."""
    misp_url = os.getenv('MISP_URL')
    misp_key = os.getenv('MISP_API_KEY')
    verify_cert = os.getenv('MISP_VERIFYCERT', 'False').lower() == 'true'

    if not misp_url or not misp_key:
        print("[!] MISP credentials not configured in .env")
        return []

    if not ExpandedPyMISP:
        print("[!] pymisp module not installed. Run: pip install pymisp")
        return []

    try:
        print(f"[*] Connecting to MISP at {misp_url}...")
        misp = ExpandedPyMISP(misp_url, misp_key, verify_cert, debug=False)
        
        # Search for attributes published in the last 7 days
        # Types: ip-src, ip-dst, domain, url, md5, sha1, sha256
        print("[*] Searching for recent MISP attributes...")
        result = misp.search(controller='attributes', type_attribute=['ip-src', 'ip-dst', 'domain', 'sha256'], last='7d')
        
        iocs = []
        if 'Attribute' in result:
            for attr in result['Attribute']:
                iocs.append({
                    'value': attr['value'],
                    'type': attr['type'],
                    'source': 'MISP',
                    'event_id': attr['event_id']
                })
        
        print(f"[+] Successfully fetched {len(iocs)} IOCs from MISP.")
        return iocs

    except Exception as e:
        print(f"[-] Error connecting to MISP: {e}")
        return []

def fetch_otx_iocs():
    """Fetches recent pulses and extracts IOCs from AlienVault OTX."""
    otx_key = os.getenv('OTX_API_KEY')

    if not otx_key:
        print("[!] OTX API key not configured in .env")
        return []

    if not OTXv2:
        print("[!] OTXv2 module not installed. Run: pip install OTXv2")
        return []

    try:
        print("[*] Connecting to AlienVault OTX...")
        otx = OTXv2(otx_key)
        
        # Get pulses subscribed by the user
        print("[*] Fetching subscribed pulses from OTX...")
        pulses = otx.getall()
        
        iocs = []
        # Limit to first 10 pulses for this example
        for pulse in pulses[:10]:
            if 'indicators' in pulse:
                for indicator in pulse['indicators']:
                    iocs.append({
                        'value': indicator['indicator'],
                        'type': indicator['type'],
                        'source': 'OTX',
                        'pulse_name': pulse['name']
                    })
                    
        print(f"[+] Successfully fetched {len(iocs)} IOCs from OTX.")
        return iocs

    except Exception as e:
        print(f"[-] Error connecting to OTX: {e}")
        return []

def fetch_abusech_iocs():
    """Placeholder for fetching IOCs from abuse.ch URLhaus / FeodoTracker"""
    print("[*] Fetching from abuse.ch... (Not implemented yet)")
    return []

if __name__ == "__main__":
    print("--- Threat Intelligence Collector ---")
    
    misp_iocs = fetch_misp_iocs()
    otx_iocs = fetch_otx_iocs()
    abusech_iocs = fetch_abusech_iocs()
    
    total_iocs = len(misp_iocs) + len(otx_iocs) + len(abusech_iocs)
    
    print("-------------------------------------")
    print(f"Total IOCs collected: {total_iocs}")
    print("-------------------------------------")
    if total_iocs > 0:
        print("[*] Next step: Normalize and deduplicate these IOCs.")

