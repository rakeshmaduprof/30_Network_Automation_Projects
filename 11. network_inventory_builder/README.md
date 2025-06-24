# Network Inventory Builder

This project connects to Cisco-like network devices via SSH using `netmiko` and collects inventory information such as:

- Hostname
- IOS Version
- Serial Number
- Model

---

## ✅ Requirements

- Python 3.8+
- SSH access to network devices
- `netmiko` library

### 📦 Install Requirements

```bash
pip install -r requirements.txt
```

---

## 📁 Files

- `devices.yaml` – List of devices and credentials
- `inventory_collector.py` – Main script to collect inventory
- `inventory_output.csv` – Output file with inventory info
- `README.md` – This guide

---

## 📡 Device Configuration

Ensure the following:
- SSH is enabled on devices
- Devices are reachable from the machine running the script
- Correct credentials and IPs are entered in `devices.yaml`

---

## 🛠️ Usage

```bash
python inventory_collector.py
```

---

## 🧾 Sample Output (CSV)

```
hostname,ip,model,serial,version
R1,192.168.1.1,Cisco ISR4331,FGL2101X1AB,16.9.3
```

---

## 🧪 Notes

The script uses `show version` and parses the necessary fields. It supports Cisco IOS-style output.

Extendable for Juniper, HP, etc., with proper parsing logic.

