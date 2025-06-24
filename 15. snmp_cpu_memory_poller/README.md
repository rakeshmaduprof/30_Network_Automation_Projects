# SNMP Poller for CPU and Memory

This project polls network devices via SNMP to retrieve CPU and memory usage, then visualizes the data using matplotlib.

---

## ✅ Features

- Poll multiple devices using SNMP
- Collect CPU and memory usage data
- Visualize metrics with graphs

---

## 📁 Files

- `devices.yaml` — List of devices with SNMP community and IPs
- `poller.py` — SNMP polling and plotting logic
- `requirements.txt` — Python package dependencies

---

## 🛠️ Prerequisites

Install required libraries:

```bash
pip install -r requirements.txt
```

Ensure SNMP is enabled and accessible on all devices with the correct community string.

---

## 🌐 Sample Device Configuration (Cisco)

```
conf t
snmp-server community public RO
```

---

## ▶️ Run the Poller

```bash
python poller.py
```

---

## 📊 Output

CPU and Memory utilization graphs will be shown and saved as images:

- `cpu_usage.png`
- `memory_usage.png`

