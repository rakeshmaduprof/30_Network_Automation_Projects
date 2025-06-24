# Simple Python-Based Syslog Server

This project implements a basic Syslog server using Python's socket module. It listens for incoming syslog messages (UDP 514 by default) and writes them to a log file.

---

## ✅ Features

- Lightweight and easy to run
- Stores logs with timestamps
- Customizable port and log file

---

## 🗂️ Project Files

- `syslog_server.py` — Main Python script
- `requirements.txt` — (Optional, only standard library is used)
- `logs/syslog.log` — Log file where messages are saved (created after first run)

---

## 🛠️ Requirements

Python 3.x (no third-party libraries required)

---

## 🚀 How to Run

```bash
python syslog_server.py
```

The server will listen on `0.0.0.0:514` by default.

---

## 📡 Configure Network Devices

Point your network devices to the server's IP and port 514:

Example (Cisco):
```
conf t
logging host <SERVER_IP>
logging trap informational
```

---

## 📤 Output

Incoming logs are printed on the console and saved in `logs/syslog.log` like:

```
[2025-06-08 16:35:22] 192.168.1.10: %SYS-5-CONFIG_I: Configured from console by console
```

---

## ⚠️ Note

- Run as root/admin if binding to port < 1024 on some systems.
- Customize port or output path by editing the script.

