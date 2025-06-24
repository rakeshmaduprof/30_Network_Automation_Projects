# Send Config Commands to Cisco Device

## 📌 Description
This project connects to Cisco devices and sends a set of configuration commands using SSH.

## 📁 Files
- `main.py`: Main script to run the configuration.
- `devices.yaml`: Contains device connection info.
- `commands.txt`: List of config commands to push.
- `requirements.txt`: Required Python packages.

## 🛠️ Setup

### 1. Install Python & Packages
```bash
pip install -r requirements.txt
```

### 2. Configure Device
Ensure:
- SSH is enabled on the Cisco device.
- Your PC has IP reachability to the device.
- Credentials are correct.

### 3. Run the Script
```bash
python main.py
```

### ✅ Output
- Script will display configuration output on terminal.
- Device will be updated with new config.
