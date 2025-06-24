# TFTP Server with Auto Config Backup

This project implements a basic TFTP server in Python and automates backing up device configurations to it.

---

## 📂 Files

- `tftp_server.py` - Simple Python-based TFTP server
- `backup_trigger.py` - Script to initiate backup (e.g., via SSH)
- `tftp_config/` - Directory where backed up configs are stored
- `requirements.txt` - Required Python packages

---

## ⚙️ Setup

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run TFTP Server**:
```bash
python tftp_server.py
```

3. **Trigger Device Backup**:
```bash
python backup_trigger.py
```

> Make sure devices are configured to send their running config via TFTP.

---

## 📡 Device Configuration Example (Cisco IOS):
```
copy running-config tftp:
Address or name of remote host []? <TFTP_SERVER_IP>
Destination filename [router-confg]? R1_backup.cfg
```

---

## 🗂 Output

- Backups will be saved in the `tftp_config/` directory.
- You will see console messages on transfers.

