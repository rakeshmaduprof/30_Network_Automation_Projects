"""
IP Reachability & Latency Checker
"""

import subprocess
import platform
import csv
from datetime import datetime

# List of IPs to check
devices = ["192.168.35.134", "192.168.94.138", "8.8.8.8", "1.1.1.1", "24.54.65.23"]

# Report file
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
report_file = f"ping_report_{timestamp}.csv"

def ping_device(ip):
    # Ping command based on OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        output = subprocess.check_output(
            ["ping", param, "4", ip],   # 4 pings for better avg
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        if platform.system().lower() == "windows":
            # Extract Average latency from Windows output
            if "Average" in output:
                latency_line = [line for line in output.splitlines() if "Average" in line][0]
                latency = latency_line.split("Average =")[-1].strip()
                return True, latency

        else:
            # Extract avg latency from Linux output
            if "rtt min/avg/max" in output:
                latency_line = [line for line in output.splitlines() if "rtt min/avg/max" in line][0]
                avg_value = latency_line.split("=")[1].split("/")[1]  # second value is avg
                latency = avg_value.strip() + " ms"
                return True, latency

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
