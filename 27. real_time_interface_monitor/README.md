# Real-Time Interface Status Monitor

This tool connects to network devices via SSH every 30 seconds and monitors interface status (up/down). If a status change is detected, it logs the event and can optionally send alerts.

---

## 📁 Files

- `monitor.py` - Main monitoring script
- `devices.yaml` - List of devices to monitor
- `logs/` - Stores interface status logs
- `requirements.txt` - Required Python packages

---

## ⚙️ Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add your devices to `devices.yaml`

3. Run the monitor:
```bash
python monitor.py
```

---

## 🖥️ Output

- Status changes are printed to console
- All logs are written to `logs/interface_status_<device>.log`
