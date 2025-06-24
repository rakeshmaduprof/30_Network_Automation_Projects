import yaml
from netmiko import ConnectHandler

def load_devices(file_path='5. send_config_commands_project/devices.yaml'):
    with open(file_path) as f:
        return yaml.safe_load(f)['devices']

def load_commands(file_path='5. send_config_commands_project/commands.txt'):
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip()]

def send_config(device, commands):
    print(f"Connecting to {device['name']} ({device['ip']})...")
    try:
        conn = ConnectHandler(
            ip=device['ip'],
            username=device['username'],
            password=device['password'],
            device_type=device['device_type']
        )
        output = conn.send_config_set(commands)
        print(f"Configuration output from {device['name']}:{output}")
        conn.save_config()
        conn.disconnect()
    except Exception as e:
        print(f"Failed to configure {device['name']} - {e}")

def main():
    devices = load_devices()
    commands = load_commands()
    for device in devices:
        send_config(device, commands)

if __name__ == "__main__":
    main()
