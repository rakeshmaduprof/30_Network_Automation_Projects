import paramiko
import time

devices = [
    {"ip": "192.168.35.136", "username": "admin", "password": "admin", "hostname": "Switch"},
]

TFTP_SERVER_IP = "192.168.94.128"

def backup_config(device):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(device["ip"], username=device["username"], password=device["password"], look_for_keys=False, allow_agent=False)
    shell = ssh.invoke_shell()
    time.sleep(1)
    shell.send("terminal length 0\n")
    time.sleep(1)
    shell.send("copy running-config tftp:\n")
    time.sleep(1)
    shell.send(f"{TFTP_SERVER_IP}\n")  # TFTP server IP
    time.sleep(1)
    shell.send(f"{device['hostname']}_backup.cfg\n")  # filename
    time.sleep(2)  # give it time to transfer
    output = shell.recv(5000).decode()
    print(output)
    ssh.close()

for dev in devices:
    backup_config(dev)
