# Firewall Rule Checker Script

This tool parses firewall Access Control Lists (ACLs) from device configuration files and allows validation against expected security policies.

---

## 📁 Files

- `acl_parser.py` — Main script to parse and validate ACL rules
- `sample_config.txt` — Example router/switch config with ACLs
- `policy.yaml` — Defines expected security rules
- `requirements.txt` — Required packages

---

## ⚙️ Setup & Usage

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Add your ACL config to `sample_config.txt`.

3. Define validation rules in `policy.yaml`.

4. Run the script:
```bash
python acl_parser.py
```

---

## 🖥️ Output

- Parsed ACLs and validation results will be shown in the terminal.
