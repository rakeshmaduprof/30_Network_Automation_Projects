"""
inventory_collector.py
----------------------
Connects to Cisco devices and collects:
- Hostname
- Version
- Serial number
- Model
Saves to inventory_output.csv
"""

import yaml
import csv
from netmiko import ConnectHandler

def load_devices(file="11. network_inventory_builder/devices.yaml"):
    with open(file, "r") as f:
        return yaml.safe_load(f)["devices"]

def parse_show_version(output):
    lines = output.splitlines()
    hostname = version = serial = model = "N/A"
    for line in lines:
        if "Cisco IOS Software" in line:
            version = line.split(",")[2].strip()
        if "Processor board ID" in line:
            serial = line.split()[-1].strip()
        if "Model number" in line:
            model = line.split(":")[-1].strip()
        if "uptime is" in line:
            hostname = line.split(" uptime is")[0].strip()
    return hostname, version, serial, model

def collect_inventory(devices):
    inventory = []
    for dev in devices:
        print(f"Connecting to {dev['ip']}...")
        try:
            conn = ConnectHandler(**dev)
            output = conn.send_command("show version")
            hostname, version, serial, model = parse_show_version(output)
            inventory.append({
                "hostname": hostname,
                "ip": dev["ip"],
                "model": model,
                "serial": serial,
                "version": version
            })
            conn.disconnect()
        except Exception as e:
            print(f"Failed to connect to {dev['ip']}: {e}")
    return inventory

def save_to_csv(data, filename="inventory_output.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["hostname", "ip", "model", "serial", "version"])
        writer.writeheader()
        writer.writerows(data)

def main():
    devices = load_devices()
    inventory = collect_inventory(devices)
    save_to_csv(inventory)
    print("\nInventory saved to inventory_output.csv")

if __name__ == "__main__":
    main()
