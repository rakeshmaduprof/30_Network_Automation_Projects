# Project: SSH into a Device and Run a Command

## Description
This project connects to network devices via SSH and runs specified commands using Python's `paramiko` library.

## Files
- `ssh_execute.py`: Main Python script to run.
- `devices.txt`: A file containing device IPs, credentials, and commands.
- `README.md`: Documentation and instructions.

## Requirements
- Python 3.x
- `paramiko` library (install with `pip install paramiko`)
- SSH enabled on the target devices

## How to Configure Devices
- Enable SSH on your network devices (Cisco, Juniper, Linux machines, etc.).
- Ensure username and password-based authentication is enabled.
- Allow your PC’s IP to access these devices on port 22.

## Format of devices.txt
```
IP_ADDRESS,USERNAME,PASSWORD,COMMAND
```

### Example:
```
192.168.1.1,admin,password123,show version
192.168.1.2,admin,password123,show ip interface brief
```

## How to Run

1. Edit `devices.txt` with your actual IPs and credentials.
2. Run the script using:

```bash
python ssh_execute.py
```

## Output Example

```
--- SSH Command Execution Results ---

192.168.1.1     --> ✅ Success | Output:
Cisco IOS Software, C800 Software (C800-UNIVERSALK9-M), Version 15.6(3)M2, RELEASE SOFTWARE (fc2)

192.168.1.2     --> ❌ Failed | Output:
Authentication failed.
```

## Use Cases
- Automated command execution across multiple network devices.
- Backup script, configuration checks, or compliance audits.
