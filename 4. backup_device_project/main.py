import yaml
from datetime import datetime
from netmiko import ConnectHandler
from pathlib import Path

def load_devices(file_path='4. backup_device_project/devices.yaml'):
    with open(file_path) as f:
        return yaml.safe_load(f)['devices']

def backup_device(device):
    print(f"Connecting to {device['name']} ({device['ip']})...")
    try:
        conn = ConnectHandler(
            ip=device['ip'],
            username=device['username'],
            password=device['password'],
            device_type=device['device_type']
        )
        output = conn.send_command("show running-config")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{device['ip']}_{timestamp}.txt"
        backup_path = Path("backup")
        backup_path.mkdir(exist_ok=True)
        with open(backup_path / filename, "w") as f:
            f.write(output)
        print(f"Backup saved to backup/{filename}")
        conn.disconnect()
    except Exception as e:
        print(f"Failed to backup {device['name']} - {e}")

def main():
    devices = load_devices()
    for device in devices:
        backup_device(device)

if __name__ == "__main__":
    main()
