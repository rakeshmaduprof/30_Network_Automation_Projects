# Basic Nmap Integration with Python

This project integrates **Nmap** with Python using the `python-nmap` library to scan target hosts or networks and report open ports.

---

## ✅ Features

- Scan single IP or subnet range
- View open TCP ports, service names, and states
- Save results to a text file

---

## 🛠️ Requirements

- Python 3.8+
- `nmap` installed on your system
- Python modules: `python-nmap`

### 📦 Install Requirements

```bash
sudo apt install nmap        # Linux
# OR
brew install nmap            # macOS

pip install -r requirements.txt
```

---

## 🔧 Configuration

Edit `targets.json` to specify scan targets:

```json
{
  "targets": [
    "127.0.0.1",
    "192.168.1.1",
    "scanme.nmap.org"
  ]
}
```

---

## 🚀 Usage

```bash
python scan.py
```

This will:
- Scan each IP/host using Nmap
- Print open ports and service info
- Save results to `scan_results.txt`

---

## 📤 Output Example

```
Scanning 127.0.0.1...
Host: 127.0.0.1 (localhost)
  Open port: 22/tcp (ssh)
  Open port: 80/tcp (http)
  Open port: 443/tcp (https)

Results saved to scan_results.txt
```

---

## ⚠️ Notes

- Ensure Nmap is in your system's PATH.
- Nmap scan types are kept basic (TCP connect) for compatibility.

---

Happy scanning! 🔍
