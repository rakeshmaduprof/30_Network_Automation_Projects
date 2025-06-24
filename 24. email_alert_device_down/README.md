# Email Alert System for Device Down

This Python project monitors device availability by pinging IPs and sends an email alert when any device becomes unreachable.

---

## 📁 Files

- `devices.txt` - List of device IPs to monitor
- `alert_config.yaml` - SMTP server and email settings
- `monitor.py` - Main monitoring script
- `requirements.txt` - Python package requirements

---

## 📤 Output

- Terminal shows ping status.
- Sends an email if a device is not reachable.

---

## 🛠️ Setup

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Edit `devices.txt`**:
```
192.168.1.1
192.168.1.2
```

3. **Edit `alert_config.yaml`**:
```yaml
email_settings:
  smtp_server: smtp.gmail.com
  smtp_port: 587
  sender_email: youremail@gmail.com
  sender_password: yourpassword
  receiver_email: admin@example.com
```

4. **Run the script**:
```bash
python monitor.py
```

---

## 💡 Tips

- Use app-specific passwords for Gmail or SMTP accounts.
- Run it periodically with `cron` or a loop with `sleep`.

