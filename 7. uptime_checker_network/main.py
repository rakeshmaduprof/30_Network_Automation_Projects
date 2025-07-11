import json
import time
from datetime import datetime
import subprocess
import platform

def load_config():
    with open("7. uptime_checker_network/devices.json", "r") as f:
        return json.load(f)

def check_device(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def log_status(message):
    print(message)
    with open("7. uptime_checker_network/uptime_log.txt", "a") as log_file:
        log_file.write(message + "\n")

def main():
    config = load_config()
    interval = config["interval"]
    devices = config["devices"]
    print(devices)

    while True:
        for device in devices:
            is_up = check_device(device)
            status = "UP" if is_up else "DOWN"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_status(f"[{timestamp}] Device {device} is {status}")
        time.sleep(interval)

if __name__ == "__main__":
    main()
