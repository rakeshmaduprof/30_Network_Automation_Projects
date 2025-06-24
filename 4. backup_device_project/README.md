# Backup Device Configuration

## 📌 Description
This script connects to network devices and backs up their configuration via SSH.

## 📁 Folder Structure
- `devices.yaml`: Contains list of devices to connect
- `main.py`: Main script to run the backup
- `backup/`: Folder where all config files will be saved

## 🔧 Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Update Device List
Edit `devices.yaml` to include your devices.

### 3. Run the Script
```bash
python main.py
```

## 🖥️ Device Configuration
Ensure:
- SSH is enabled
- Devices are reachable from your PC
- Username and password are correct
- IP whitelisting allows access from your machine

## ✅ Output
- Configuration files will be saved in the `backup/` folder
- Files named as: `[ip]_[timestamp].txt`
