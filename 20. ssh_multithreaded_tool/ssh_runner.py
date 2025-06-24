import csv
import paramiko
import threading
import time
import os

DEVICE_FILE = "20. ssh_multithreaded_tool/devices.csv"
COMMAND_FILE = "20. ssh_multithreaded_tool/commands.txt"
LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

def load_devices():
    with open(DEVICE_FILE) as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_commands():
    with open(COMMAND_FILE) as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def ssh_worker(device, commands):
    ip = device["ip"]
    username = device["username"]
    password = device["password"]
    print(f"[+] Connecting to {ip}...")

    start_time = time.time()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ip, username=username, password=password, timeout=10,
                    look_for_keys=False, allow_agent=False)
    except Exception as conn_error:
        print(f"[✘] Failed to connect {ip}: {type(conn_error).__name__}: {conn_error}")
        return

    try:
        shell = ssh.invoke_shell()
        time.sleep(1)
        shell.recv(1000)  # Clear welcome banner
        shell.send('terminal len 0'+"\n")
        with open(f"{LOG_DIR}/{ip}_output.txt", "w") as log_file:
            for cmd in commands:
                shell.send(cmd + "\n")
                time.sleep(2)  # Wait for command to execute
                output = shell.recv(5000).decode(errors='ignore')
                log_file.write(f"Command: {cmd}\n{output}\n{'-'*40}\n")

        ssh.close()
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        print(f"[✔] Completed {ip} in {duration} seconds")
    except Exception as e:
        print(f"[✘] Error while executing commands on {ip}: {e}")
        ssh.close()



def main():
    devices = load_devices()
    commands = load_commands()
    threads = []

    for device in devices:
        t = threading.Thread(target=ssh_worker, args=(device, commands))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n✅ All SSH tasks completed.")

if __name__ == "__main__":
    main()
