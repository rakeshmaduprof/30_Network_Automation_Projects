# Network Device Uptime Checker

This tool checks the uptime or reachability of network devices using ICMP (ping) and logs the results.

## Features
- Uses Python and `ping3` to check device status.
- Can monitor routers, switches, firewalls, or any IP-based network devices.
- Logs uptime results to a text file.
- Configurable check interval and list of devices.

## Requirements
- Python 3.7+
- `ping3` module

## Setup & Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure your devices in `devices.json`.

3. Run the checker:
```bash
python main.py
```

## Output
- Console output for each device status.
- Log file `uptime_log.txt` with timestamped entries.

## Network Setup
- Devices should respond to ICMP (ping).
- Ensure your network/firewall allows outbound ICMP from your monitoring machine.
