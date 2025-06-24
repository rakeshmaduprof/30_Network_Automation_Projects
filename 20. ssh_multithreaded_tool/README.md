# SSH Multi-Threaded Tool

This tool connects to multiple network devices over SSH concurrently using Python threading.

---

## ✅ Features

- Connects to multiple devices using SSH
- Executes commands concurrently using threads
- Logs outputs for each device separately

---

## 📁 Files

- `ssh_runner.py` — Main script to connect and execute
- `devices.csv` — List of devices and credentials
- `commands.txt` — Commands to run on each device
- `requirements.txt` — Required libraries
- `logs/` — Directory where logs will be saved

---

## 🛠️ Requirements

- Python 3.x
- `paramiko`

Install with:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python ssh_runner.py
```

---

## 📤 Output

- Output per device is saved to `logs/<ip>_output.txt`
- Status is printed to the terminal

---

## 📁 devices.csv Format

```
ip,username,password
192.168.1.1,admin,cisco
192.168.1.2,admin,cisco
```

---

## 📄 commands.txt Format

```
show version
show ip interface brief
```

---
