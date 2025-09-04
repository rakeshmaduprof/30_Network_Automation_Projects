"""
Netmiko Configuration Push Tool (Safe for Old Netmiko)
-------------------------------------------------------
Pushes CLI configs to multiple devices using SSH/Telnet with:
- Per-device logging
- Execution timing
- Optional dry-run mode
- Pretty output using 'rich'
- Uses send_config_from_file() for compatibility
"""

import csv
import os
import time
from datetime import datetime
from netmiko import ConnectHandler
from rich.console import Console
from rich.table import Table

# ======================
# File Paths
# ======================
CONFIG_FILE = "17. netmiko_config_push_Monitor/config.txt"
DEVICE_FILE = "17. netmiko_config_push_Monitor/devices.csv"
LOG_DIR = "logs"
DRY_RUN = False  # Set True for testing (no actual push)

console = Console()


# ======================
# Functions
# ======================
def push_config(device, config_file):
    start_time = time.time()
    os.makedirs(LOG_DIR,exist_ok=True)
    log_file_path = os.path.join(LOG_DIR, f"{device['ip']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    try:
        conn = ConnectHandler(**device)

        conn.enable()
        prompt = conn.find_prompt()
        console.print(f"[yellow]Connected to {device['ip']}, Prompt: {prompt}[/yellow]")

        output = ""
        if DRY_RUN:
            output = f"[Dry Run] Connected to {device['ip']} ({device['device_type']})\n"
        else:
            output += f"Connected to {device['ip']} - Pushing config...\n"

            # Use send_config_from_file for older Netmiko (safer than looping commands)
            output += conn.send_config_from_file(config_file)

            # Try saving config if supported
            try:
                output += "\n" + conn.save_config()
            except Exception:
                output += "\n[Warning] Save config not supported on this platform.\n"

        conn.disconnect()

        # Write per-device log
        with open(log_file_path, "w") as f:
            f.write(output)

        elapsed = time.time() - start_time
        return (True, f"{elapsed:.2f}s", log_file_path)

    except Exception as e:
        return (False, "N/A", str(e))


def load_devices(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def main():
    devices = load_devices(DEVICE_FILE)

    table = Table(title="Configuration Push Report")
    table.add_column("IP", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Time", style="magenta")
    table.add_column("Details", style="white")

    for row in devices:
        device = {
            "device_type": row.get("device_type", "cisco_ios"),
            "ip": row["ip"],
            "username": row["username"],
            "password": row["password"],
            "secret": row.get("secret", row["password"]),
        }
    

        success, time_taken, details = push_config(device, CONFIG_FILE)
        if success:
            table.add_row(device["ip"], "[green]Success", time_taken, details)
        else:
            table.add_row(device["ip"], "[red]Failed", "-", details)

    console.print(table)


if __name__ == "__main__":
    main()
