import yaml
import paramiko
import time

def load_yaml(file_path):
    with open(file_path) as f:
        return yaml.safe_load(f)

def ssh_connect_and_config(ip, username, password, commands):
    try:
        print(f"Connecting to {ip}...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
        shell = ssh.invoke_shell()
        
        shell.send("enable\n")  # Enter enable mode if needed
        time.sleep(1)
        shell.send("configure terminal\n")  # Enter config mode
        time.sleep(1)
        
        shell.send("terminal length 0\n")  # Disable paging
        time.sleep(0.5)

        for cmd in commands:
            shell.send(cmd["command"] + "\n")  # Send command with newline
            time.sleep(0.5)  # Give the device time to process

        shell.send("end\n")  # Exit config mode
        time.sleep(0.5)
        shell.send("write memory\n")  # Save config
        time.sleep(1)

        output = shell.recv(9999).decode()
        print(f"[{ip}] Configuration complete.")
        # print(output)  # You can optionally print output to verify
        ssh.close()
    except Exception as e:
        print(f"Error on {ip}: {e}")

if __name__ == "__main__":
    inventory = load_yaml("23. ansible_style_python_automation/inventory.yaml")
    tasks = load_yaml("23. ansible_style_python_automation/config_tasks.yaml")["tasks"]

    for device in inventory["devices"]:
        ssh_connect_and_config(device["ip"], device["username"], device["password"], tasks)
