# Log Analyzer for Config Changes

This tool compares two versions of network device configurations or logs to identify changes.

---

## ✅ Features

- Compares two configuration files using Python's `difflib`
- Highlights added, removed, or modified lines
- Saves the diff output to a readable text file

---

## 📁 Files

- `diff_analyzer.py` — Main script
- `config_old.txt` — Sample old configuration
- `config_new.txt` — Sample new configuration
- `requirements.txt` — No external dependencies

---

## ▶️ How to Run

```bash
python diff_analyzer.py
```

---

## 📤 Output

The script outputs:
- Side-by-side unified diff to console
- A file called `diff_output.txt` for saving results

---

## 🔧 Use Case

Ideal for:
- Detecting unauthorized changes
- Troubleshooting after outages
- Auditing network configuration drift

---

## 📦 Example Device Configuration Backup

Export Cisco configuration:
```
copy running-config tftp
```

Download the config from the device and store as `config_old.txt` and `config_new.txt`.
