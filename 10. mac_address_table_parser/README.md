# MAC Address Table Parser

This project parses the output of the `show mac address-table` command from Cisco-like network switches and allows filtering by MAC address or interface.

---

## 🛠️ Requirements

- Python 3.6+
- No external libraries needed (uses Python standard library)

---

## 📂 Files

- `mac_table.txt` — Sample raw command output
- `parser.py` — Main parser script
- `mac_filter.py` — Utility to filter by MAC or port
- `sample_output.txt` — Example filtered output
- `README.md` — This documentation

---

## 🔧 Configuration

You can copy and paste real `show mac address-table` output into `mac_table.txt`, or use the sample provided.

---

## 🚀 How to Run

### 1. Filter by MAC address:
```bash
python mac_filter.py --mac 000a.f3ff.12a4
```

### 2. Filter by port/interface:
```bash
python mac_filter.py --port Gi1/0/1
```

---

## 🧾 Example Output

```
Found 1 matching entries:
VLAN: 10, MAC: 000a.f3ff.12a4, Type: DYNAMIC, Port: Gi1/0/1
```

---

## ✅ Sample MAC Table Format (Cisco Style)

```
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    000a.f3ff.12a4    DYNAMIC     Gi1/0/1
  20    000b.f2ee.34b5    DYNAMIC     Gi1/0/2
 100    000c.abcd.56ef    STATIC      Gi1/0/3
```

---

## 🧪 Testing

Feel free to expand `mac_table.txt` with additional entries and test the filters.

