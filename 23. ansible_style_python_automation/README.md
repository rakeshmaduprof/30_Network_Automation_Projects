# Ansible-style Python Automation

This project simulates basic Ansible functionality using Python:
- Reads a YAML inventory of devices
- Sends configuration commands via SSH

---

## 📁 Files

- `inventory.yaml` - Device inventory
- `config_tasks.yaml` - Commands to apply
- `automate.py` - Main runner script
- `requirements.txt` - Dependencies

---

## 🔧 Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Edit `inventory.yaml` with your devices:
```yaml
devices:
  - name: R1
    ip: 192.168.1.1
    username: admin
    password: cisco
```

3. Edit `config_tasks.yaml`:
```yaml
tasks:
  - command: hostname PythonRouter
  - command: interface loopback0
  - command: ip address 1.1.1.1 255.255.255.255
```

4. Run the tool:
```bash
python automate.py
```

---

## 💡 Notes

- This tool uses `paramiko` to SSH into devices.
- Tested on Cisco IOS.
