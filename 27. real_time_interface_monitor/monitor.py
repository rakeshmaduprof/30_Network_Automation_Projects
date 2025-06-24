import paramiko
import yaml
import time
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def load_devices():
    with open("27. real_time_interface_monitor/devices.yaml") as f:
        return yaml.safe_load(f)["devices"]

def ssh_get_interface_status(device):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device["ip"], username=device["username"], password=device["password"],look_for_keys=False,allow_agent=False
                    )
        shell = ssh.invoke_shell()
        shell.send("terminal length 0\n")
        shell.send("show ip interface brief\n")
        time.sleep(2)
        output = shell.recv(10000).decode()
        ssh.close()
        return output
    except Exception as e:
        return f"ERROR: {e}"

def parse_interfaces(output):
    lines = output.splitlines()
    interfaces = {}
    for line in lines:
        if "Interface" in line or "----" in line or not line.strip():
            continue
        parts = line.split()
        if len(parts) >= 6:
            interfaces[parts[0]] = parts[-1]
    return interfaces

def log_status(hostname, log_data):
    log_file = os.path.join(LOG_DIR, f"interface_status_{hostname}.log")
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {log_data}\n")

def monitor():
    devices = load_devices()
    last_status = {}

    while True:
        for device in devices:
            hostname = device["hostname"]
            print(f"Checking {hostname}...")
            output = ssh_get_interface_status(device)
            if output.startswith("ERROR"):
                print(f"[!] {output}")
                log_status(hostname, output)
                continue
            current_status = parse_interfaces(output)
            if hostname not in last_status:
                last_status[hostname] = current_status
            else:
                for iface, status in current_status.items():
                    old_status = last_status[hostname].get(iface)
                    if old_status and old_status != status:
                        msg = f"Interface {iface} changed from {old_status} to {status}"
                        print(f"[ALERT] {msg}")
                        log_status(hostname, msg)
                last_status[hostname] = current_status
        time.sleep(30)

if __name__ == "__main__":
    monitor()
