"""
Simple TCP Port Scanner
"""

import socket
from datetime import datetime

def scan_port(ip, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            return result == 0
    except Exception:
        return False

def main():
    target_ip = input("Enter target IP address: ").strip()
    start_port = int(input("Enter start port: ").strip())
    end_port = int(input("Enter end port: ").strip())

    print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")

    with open("scan_results.txt", "w") as log_file:
        log_file.write(f"Scan Results for {target_ip} ({datetime.now()}):\n")
        for port in range(start_port, end_port + 1):
            status = "Open" if scan_port(target_ip, port) else "Closed"
            result_line = f"Port {port}: {status}"
            print(result_line)
            log_file.write(result_line + "\n")

if __name__ == "__main__":
    main()
