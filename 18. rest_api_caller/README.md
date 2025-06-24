# REST API Caller for Network Devices

This project demonstrates how to call REST APIs from network devices such as Cisco's RESTCONF/YANG-enabled platforms or mock API servers.

---

## ✅ Features

- Sends REST API GET request to retrieve device information
- Supports basic authentication
- Parses JSON responses
- Can be adapted for Cisco DevNet Sandbox (e.g., IOS XE)

---

## 📁 Files

- `api_caller.py` — Main script to call device REST APIs
- `config.json` — API endpoint and credentials
- `requirements.txt` — Required libraries

---

## 🛠️ Requirements

- Python 3.x
- `requests` library

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python api_caller.py
```

---

## 🌐 Example Device Configuration (Cisco DevNet Sandbox)

You can use:
- [IOS XE on CSR1000v sandbox](https://developer.cisco.com/site/ios-xe/)

Example:
- URL: `https://sandbox-iosxe-latest-1.cisco.com`
- Username: `developer`
- Password: `C1sco12345`

---

## 📤 Output

Returns JSON data like hostname, interfaces, etc. Example:
```json
{
  "ietf-interfaces:interface": [
    {
      "name": "GigabitEthernet1",
      "enabled": true,
      "ietf-ip:ipv4": {
        "address": [
          {"ip": "10.10.20.48", "netmask": "255.255.255.0"}
        ]
      }
    }
  ]
}
```

---
