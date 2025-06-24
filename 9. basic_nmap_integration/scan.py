"""
scan.py
-------
Basic Nmap integration with Python using python-nmap.
Scans target hosts for open ports and service names.
"""

import json
import nmap
from datetime import datetime

def load_targets(path="9. basic_nmap_integration/targets.json"):
    with open(path, "r") as f:
        return json.load(f)["targets"]

def run_scan(target):
    scanner = nmap.PortScanner()
    print(f"Scanning {target}...")
    try:
        scanner.scan(hosts=target, arguments="-sT")
        return scanner
    except Exception as e:
        print(f"Error scanning {target}: {e}")
        return None

def parse_and_log(scanner, target, logfile):
    if target not in scanner.all_hosts():
        logfile.write(f"{target} - Host is down or unreachable\n")
        return

    logfile.write(f"Host: {target} ({scanner[target].hostname()})\n")
    for proto in scanner[target].all_protocols():
        ports = scanner[target][proto].keys()
        for port in sorted(ports):
            state = scanner[target][proto][port]["state"]
            name = scanner[target][proto][port]["name"]
            logfile.write(f"  Open port: {port}/{proto} ({name})\n")
    logfile.write("\n")

def main():
    targets = load_targets()
    with open("scan_results.txt", "w") as logfile:
        logfile.write(f"Scan started: {datetime.now()}\n\n")
        for target in targets:
            scanner = run_scan(target)
            if scanner:
                parse_and_log(scanner, target, logfile)
        logfile.write(f"Scan finished: {datetime.now()}\n")

    print("\nResults saved to scan_results.txt")

if __name__ == "__main__":
    main()
