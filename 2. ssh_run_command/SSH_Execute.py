import paramiko
import time
import re

def ssh_to_device(ip, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, timeout=10, look_for_keys=False, allow_agent=False)

        # Start shell
        channel = ssh.invoke_shell()
        time.sleep(1)

        output = ""
        # Clear the initial banner
        if channel.recv_ready():
            output += channel.recv(9999).decode()

        # Send command
        channel.send(command + '\n')
        time.sleep(2)  # Give time for command to execute

        # Receive output
        command_output = ""
        while channel.recv_ready():
            command_output += channel.recv(9999).decode()
            time.sleep(0.5)

        ssh.close()

        # Clean output
        command_output = re.sub(r'\r', '', command_output)
        command_output = re.sub(r'\x1b\[[0-9;]*[mK]', '', command_output)  # Remove ANSI codes
        return True, command_output.strip()

    except Exception as e:
        return False, str(e)


def main():
    try:
        with open("2. ssh_run_command/devices.txt", "r") as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("devices.txt file not found.")
        return

    print("\n--- SSH Command Execution Results ---\n")
    for line in lines:
        try:
            ip, user, pwd, cmd = line.split(",", 3)
        except ValueError:
            print(f"Invalid entry: {line}")
            continue

        success, result = ssh_to_device(ip, user, pwd, cmd)
        status = "✅ Success" if success else "❌ Failed"
        print(f"{ip:15} --> {status}")
        print(f"Output:\n{result}\n")

if __name__ == "__main__":
    main()
