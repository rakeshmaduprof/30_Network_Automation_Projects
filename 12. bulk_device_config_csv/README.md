# Bulk Device Configuration using CSV

This project connects to multiple network devices (e.g., Cisco routers/switches) and applies configuration commands defined in a CSV file.

---

## ✅ Features

- Bulk configuration via SSH
- IP-based targeting
- Per-device command customization
- Simple CSV structure

---

## 📁 Files

- `devices.csv` — Contains device info and commands
- `bulk_config.py` — Main Python script to run configuration
- `requirements.txt` — Python package requirements

---

## 🛠️ Requirements

```bash
pip install -r requirements.txt
```

Also ensure network devices:
- Are reachable via SSH
- Have correct credentials configured in the CSV

---

## 📄 CSV Format (devices.csv)

```
ip,username,password,device_type,commands
192.168.1.1,admin,admin123,cisco_ios,"interface loopback0; ip address 1.1.1.1 255.255.255.0"
192.168.1.2,admin,admin123,cisco_ios,"hostname R2; no ip domain-lookup"
```

Use `;` to separate multiple commands in a single row.

---

## 🚀 Run the Script

```bash
python bulk_config.py
```

---

## 📤 Output

Applies configurations and prints logs to console.

---

## 🔐 Note

This script uses plaintext passwords. Secure with environment variables or vaults for production use.

