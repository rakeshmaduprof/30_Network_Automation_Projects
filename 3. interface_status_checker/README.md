# Project: Interface Status Checker

## Description
This Python script connects to network devices via SSH and runs the `show ip interface brief` command to display the interface status.

## Files Included
- `interface_checker.py`: Python script to execute.
- `devices.txt`: File listing the device IPs and credentials.
- `README.md`: Documentation with setup instructions.

## Requirements
- Python 3.x
- `paramiko` library (`pip install paramiko`)
- Devices must support SSH and allow CLI command execution.

## Format of devices.txt
```
IP_ADDRESS,USERNAME,PASSWORD
```

### Example:
```
192.168.1.1,admin,password123
192.168.1.2,admin,password123
```

## How to Run

1. Update `devices.txt` with your device IPs and credentials.
2. Run the script using:

```bash
python interface_checker.py
```

## Example Output
```
--- Interface Status Report ---

192.168.1.1     --> ✅ Success
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     192.168.1.1     YES manual up                    up
GigabitEthernet0/1     unassigned      YES unset  administratively down down
--------------------------------------------------

192.168.1.2     --> ❌ Failed
Authentication failed.
--------------------------------------------------
```

## Use Cases
- Quickly check the operational state of interfaces on routers/switches.
- Detect down or misconfigured ports in the network.
- Great for audit and validation during network rollouts.
