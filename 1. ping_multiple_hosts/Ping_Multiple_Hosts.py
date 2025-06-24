import subprocess
import platform

def ping_host(ip):
    # Decide the command based on the OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return True, result.stdout.splitlines()[0]
        else:
            return False, result.stderr if result.stderr else result.stdout.splitlines()[0]
    except Exception as e:
        return False, str(e)

def main():
    try:
        with open("1. ping_multiple_hosts/hosts.txt", "r") as file:
            ips = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("hosts.txt file not found. Please create it with one IP per line.")
        return

    print("\n--- Ping Results ---\n")
    for ip in ips:
        reachable, message = ping_host(ip)
        status = "✅ Reachable" if reachable else "❌ Unreachable"
        print(f"{ip:15} --> {status} | Info: {message}")

if __name__ == "__main__":
    main()
