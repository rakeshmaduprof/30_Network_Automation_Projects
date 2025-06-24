"""
mac_filter.py
-------------
Filter parsed MAC table by MAC address or port.
"""

import argparse
from parser import parse_mac_table

def filter_entries(entries, mac=None, port=None):
    results = []
    for entry in entries:
        if mac and entry["mac"] == mac.lower():
            results.append(entry)
        elif port and entry["port"].lower() == port.lower():
            results.append(entry)
    return results

def display_results(results):
    if not results:
        print("No matching entries found.")
        return
    print(f"Found {len(results)} matching entries:")
    for e in results:
        print(f"VLAN: {e['vlan']}, MAC: {e['mac']}, Type: {e['type']}, Port: {e['port']}")

def main():
    parser = argparse.ArgumentParser(description="Filter MAC table by MAC or port.")
    parser.add_argument("--mac", help="MAC address to filter")
    parser.add_argument("--port", help="Port/interface to filter (e.g., Gi1/0/1)")
    args = parser.parse_args()

    entries = parse_mac_table()
    results = filter_entries(entries, mac=args.mac, port=args.port)
    display_results(results)

if __name__ == "__main__":
    main()
