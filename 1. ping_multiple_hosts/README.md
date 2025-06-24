# Project: Ping Multiple Hosts

## Description
This project checks the availability of multiple IP addresses by pinging them using Python's subprocess module.

## Files
- `ping_hosts.py`: Main Python script to execute.
- `hosts.txt`: Text file containing a list of IP addresses to ping.
- `README.md`: Documentation and instructions.

## Requirements
- Python 3.x installed
- Works on Windows, Linux, and macOS

## How to Run

1. Clone or download the folder.
2. Edit `hosts.txt` to add your list of IPs to test.
3. Open terminal in the project folder and run:

```bash
python ping_hosts.py
```

> You should see output like:

```
--- Ping Results ---

127.0.0.1       --> ✅ Reachable | Info: Pinging 127.0.0.1 with 32 bytes of data:
8.8.8.8         --> ✅ Reachable | Info: Pinging 8.8.8.8 with 32 bytes of data:
192.168.1.1     --> ❌ Unreachable | Info: Request timed out.
10.10.10.10     --> ❌ Unreachable | Info: Destination host unreachable.
```

## Notes
- You can add private IPs from your network (e.g., your router’s IP, gateway, or another machine).
- For unreachable devices, it may take a few seconds before timeout.

## Use Cases
- Network health checks
- Reachability tests during device rollout
- Teaching basic Python + networking logic
