import yaml
from netmiko import ConnectHandler

def load_devices(file_path='6. hostname_changer_project/devices.yaml'):
    with open(file_path) as f:
        return yaml.safe_load(f)['devices']

def change_hostname(device):
    print(f"Connecting to {device['ip']}...")
    try:
        conn = ConnectHandler(
            ip=device['ip'],
            username=device['username'],
            password=device['password'],
            device_type=device['device_type']
        )
        new_hostname = device['new_hostname']
        commands = [f"hostname {new_hostname}"]
        output = conn.send_config_set(commands)
        conn.save_config()
        conn.disconnect()
        print(f"Hostname changed to '{new_hostname}' on {device['ip']}:{output}\n")
    except Exception as e:
        print(f"Failed to change hostname on {device['ip']} - {e}")

def main():
    devices = load_devices()
    for device in devices:
        change_hostname(device)

if __name__ == "__main__":
    main()
