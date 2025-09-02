"""
bulk_config.py
--------------
Applies configuration to multiple devices using CSV.
"""

import pandas as pd
from netmiko import ConnectHandler

def parse_commands(cmd_str):
    return [cmd.strip() for cmd in cmd_str.split(";") if cmd.strip()]

def main():
    df = pd.read_csv("12. bulk_device_config_csv/devices.csv")
    for _, row in df.iterrows():
        device = {
            "device_type": row["device_type"],
            "ip": row["ip"],
            "username": row["username"],
            "password": row["password"],
        }
        commands = parse_commands(row["commands"])
        print(f"\nConnecting to {device['ip']}...")
        try:
            conn = ConnectHandler(**device)
            output = conn.send_config_set(commands)
            print(f"Configuration output from {device['ip']}:{output}")
            conn.save_config()
            conn.disconnect()
        except Exception as e:
            print(f"Failed to connect or configure {device['ip']}: {e}")

if __name__ == "__main__":
    main()
