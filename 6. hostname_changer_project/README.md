# Hostname Changer Script

## 📌 Description
This script connects to Cisco devices via SSH and updates their hostnames based on a YAML configuration.

## 📁 Files
- `main.py`: Script to execute hostname changes.
- `devices.yaml`: Contains the list of devices with new hostnames.
- `requirements.txt`: Required Python packages.

## 🛠️ Setup

### 1. Install Python & Packages
```bash
pip install -r requirements.txt
```

### 2. Device Preparation
Ensure:
- SSH is enabled and accessible from your system.
- Username/password and IPs are correct in `devices.yaml`.

### 3. Run the Script
```bash
python main.py
```

## ✅ Output
- Displays connection status and config change output in terminal.
- Device hostname will be changed immediately.
