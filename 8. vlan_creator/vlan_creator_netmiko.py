import json
from netmiko import ConnectHandler

def load_config(path="8. vlan_creator/vlan_config.json"):
    with open(path) as f:
        return json.load(f)

def push_vlans(cfg):
    switch = cfg["switch"]
    vlans = cfg["vlans"]

    print(f"[INFO] Connecting to {switch['ip']}...")
    net_connect = ConnectHandler(**switch)
    net_connect.enable()
    print("[INFO] Entered enable mode.")

    for vlan in vlans:
        print(f"[INFO] Creating VLAN {vlan['id']} - {vlan['name']}")
        config_commands = [
            f"vlan {vlan['id']}",
            f"name {vlan['name']}"
        ]
        output = net_connect.send_config_set(config_commands)
        print(output.strip())

    print("[INFO] Showing VLANs...")
    vlan_output = net_connect.send_command("show vlan brief")
    print("\n--- VLAN TABLE ---")
    print(vlan_output.strip())

    net_connect.disconnect()
    print("[INFO] Disconnected from switch.")

if __name__ == "__main__":
    config = load_config()
    push_vlans(config)