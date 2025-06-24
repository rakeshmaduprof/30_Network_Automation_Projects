"""
Simple Syslog Server using Python Sockets
"""

import socket
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "syslog.log")
LISTEN_IP = "0.0.0.0"
PORT = 1514

def ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def log_message(address, message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} {address[0]}: {message}\n"
    print(log_entry.strip())
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def main():
    ensure_log_dir()
    print(f"Syslog server listening on {LISTEN_IP}:{PORT}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind((LISTEN_IP, PORT))
    except PermissionError:
        print("Permission denied: Run as administrator/root for port 514.")
        return

    while True:
        data, addr = sock.recvfrom(4096)
        log_message(addr, data.decode(errors="ignore"))

if __name__ == "__main__":
    main()
