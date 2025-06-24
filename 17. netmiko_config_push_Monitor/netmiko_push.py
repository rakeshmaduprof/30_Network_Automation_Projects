"""
Netmiko Configuration Push Tool (Enhanced)
------------------------------------------
Pushes CLI configs to multiple devices using SSH/Telnet with:
- Per-device logging
- Execution timing
- Optional dry-run mode
- Pretty output using 'rich'
"""

import csv
import os
import time
from datetime import datetime
from netmiko import ConnectHandler
from rich.console import Console
from rich.table import Table

CONFIG_FILE = "17. Netmiko_config_push_Monitor/config.txt"
DEVICE_FILE = "17. Netmiko_config_push_Monitor/devices.csv"
LOG_DIR = "logs"
DRY_RUN = False  # Set to True to skip pushing commands

console = Console()

# Make sure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def push_config(device, commands):
    start_time = time.time()
    log_file_path = os.path.join(LOG_DIR, f"{device['ip']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    try:
        conn = ConnectHandler(**device)
        conn.set_base_prompt()  # Helps detect prompt cleanly
        conn.enable()
        # prompt = conn.find_prompt()
        # print(f"Connected. Prompt detected: {prompt}")

        output = ""
        if DRY_RUN:
            output = f"[Dry Run] Connected to {device['ip']} ({device['device_type']})\n"
        else:
            output += f"Connected to {device['ip']} - Pushing config...\n"
            output += conn.send_config_set(commands)
            output += "\n" + conn.save_config()

        conn.disconnect()

        # Write log
        with open(log_file_path, "w") as f:
            f.write(output)

        elapsed = time.time() - start_time
        return (True, f"{elapsed:.2f}s", log_file_path)

    except Exception as e:
        return (False, "N/A", str(e))

def load_commands(path):
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]

def load_devices(path):
    with open(path) as f:
        return list(csv.DictReader(f))

def main():
    devices = load_devices(DEVICE_FILE)
    commands = load_commands(CONFIG_FILE)

    table = Table(title="Configuration Push Report")
    table.add_column("IP", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Time", style="magenta")
    table.add_column("Details", style="white")

    for row in devices:
        # Support both SSH and Telnet using Netmiko
        device = {
            "device_type": row.get("device_type", "cisco_ios"),  # cisco_ios, cisco_ios_telnet
            "ip": row["ip"],
            "username": row["username"],
            "password": row["password"],
            "secret": row.get("secret", row["password"]),
        }

        success, time_taken, details = push_config(device, commands)
        if success:
            table.add_row(device["ip"], "[green]Success", time_taken, details)
        else:
            table.add_row(device["ip"], "[red]Failed", "-", details)

    console.print(table)

if __name__ == "__main__":
    main()
