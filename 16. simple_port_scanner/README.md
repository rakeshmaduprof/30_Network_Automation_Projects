# Simple Python Port Scanner

This Python-based port scanner allows you to scan a specific IP address across a given range of ports to identify which are open and which are closed.

---

## ✅ Features

- Scans TCP ports
- Easy to configure IP and port range
- Reports open and closed ports
- Optionally logs results to a file

---

## 🗂️ Project Files

- `port_scanner.py` — The main scanning script
- `requirements.txt` — No external dependencies

---

## 🛠️ Requirements

- Python 3.x
- Internet or network access to the target IP

---

## ▶️ How to Run

```bash
python port_scanner.py
```

You'll be prompted to enter:
- Target IP
- Start and end ports to scan

---

## 📤 Output

Sample terminal output:
```
Scanning 192.168.1.1 from port 20 to 25...
Port 20: Closed
Port 21: Open
Port 22: Open
Port 23: Closed
Port 24: Closed
Port 25: Open
```

Logs are saved to `scan_results.txt`.

---

## ⚠️ Note

- Make sure you have permission to scan the target host.
- Firewall or IDS systems may block or log scans.

