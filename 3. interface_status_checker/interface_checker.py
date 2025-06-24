import paramiko
import time

def ssh_and_check_interfaces(ip, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, timeout=5, allow_agent=False, look_for_keys=False)

        remote_conn = ssh.invoke_shell()
        remote_conn.send("terminal length 0\n")  # Prevents paging
        remote_conn.send("show ip interface brief\n")
        time.sleep(2)  # Wait for the command to execute

        output = remote_conn.recv(5000).decode('utf-8')
        ssh.close()

        return True, output
    except Exception as e:
        return False, f"Error connecting to {ip}: {str(e)}"

def main():
    devices_file = "3. interface_status_checker/devices.txt"

    try:
        with open(devices_file, "r") as file:
            devices = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"❌ File not found: {devices_file}")
        return
    except Exception as e:
        print(f"❌ Error reading file: {str(e)}")
        return

    print("\n--- Interface Status Report ---\n")

    for device in devices:
        try:
            ip, username, password = device.split(",", 2)
        except ValueError:
            print(f"⚠️  Invalid line in devices file (expected 'ip,username,password'): {device}")
            continue

        success, result = ssh_and_check_interfaces(ip, username, password)
        status = "✅ Success" if success else "❌ Failed"
        print(f"{ip:15} --> {status}\n{result}\n{'-'*60}")

if __name__ == "__main__":
    main()
