# Automated Network Topology Generator

This project connects to network devices (Cisco), collects CDP/LLDP neighbor information, and builds a live network topology diagram.

---

## ✅ Features

- Connects to devices using SSH
- Collects CDP neighbor details
- Uses NetworkX and Matplotlib to generate a visual topology

---

## 📁 Files

- `topology_builder.py` — Main script to collect CDP data and generate topology
- `devices.csv` — List of devices with SSH credentials
- `requirements.txt` — Required Python packages

---

## 🛠️ Requirements

- Python 3.x
- Libraries: `paramiko`, `networkx`, `matplotlib`

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python topology_builder.py
```

---

## 📤 Output

- A pop-up window showing the live topology diagram of connected devices.

---

## 📁 devices.csv Format

```
ip,username,password
192.168.1.1,admin,cisco
192.168.1.2,admin,cisco
```

---

## ℹ️ Notes

- Only devices that support CDP (or LLDP if added) and are accessible via SSH will appear.
- Ensure `cdp run` and `cdp enable` are configured on Cisco interfaces.

