"""
IP Reachability & Latency Checker
"""

import subprocess
import platform
import csv
from datetime import datetime

# List of IPs to check
devices = ["192.168.35.134", "192.168.94.138", "8.8.8.8", "1.1.1.1"]

# Report file
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
report_file = f"ping_report_{timestamp}.csv"

def ping_device(ip):
    # Ping command based on OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        output = subprocess.check_output(
            ["ping", param, "2", ip],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        if "time=" in output:
            latency = output.split("time=")[1].split()[0]
            return True, latency
        else:
            return True, "N/A"
    except subprocess.CalledProcessError:
        return False, None

# Write results to CSV
with open(report_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP Address", "Reachable", "Latency (ms)"])

    for ip in devices:
        reachable, latency = ping_device(ip)
        writer.writerow([ip, "Yes" if reachable else "No", latency if latency else "-"])
        print(f"{ip} --> {'Reachable' if reachable else 'Unreachable'} | Latency: {latency}")

print(f"\nPing results saved to {report_file}")
