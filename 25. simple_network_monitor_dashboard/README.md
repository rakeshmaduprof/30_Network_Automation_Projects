# Simple Network Monitoring Dashboard

This project creates a basic Flask web dashboard that monitors:
- CPU utilization
- Interface status
- Uptime

Data is fetched via SNMP from configured network devices.

---

## 🧾 Files

- `app.py` - Flask web app
- `snmp_utils.py` - SNMP polling logic
- `devices.yaml` - List of devices to monitor
- `templates/dashboard.html` - Dashboard UI
- `requirements.txt` - Python packages required

---

## 📦 Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure your devices in `devices.yaml`:
```yaml
devices:
  - name: Router1
    ip: 192.168.1.1
    community: public
  - name: Switch1
    ip: 192.168.1.2
    community: public
```

3. Run the app:
```bash
python app.py
```

4. Open browser and go to: `http://127.0.0.1:5000`

---

## 🔧 SNMP Configuration on Devices

Ensure devices have SNMP enabled. Example for Cisco IOS:
```
snmp-server community public RO
```

---

## 📊 Output

A simple web dashboard showing:
- Device name
- CPU usage
- Uptime
- Interface count (up/down)

