# Network Device Emulator (Mock CLI)

This tool emulates a basic network device CLI to help with test automation. It simulates common network commands like `show ip interface brief`, `show version`, and more.

---

## 📁 Files

- `emulator.py` — Main mock CLI script
- `mock_data/commands.yaml` — YAML file storing command output mappings
- `requirements.txt` — Required packages

---

## ⚙️ Setup & Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the CLI:
```bash
python emulator.py
```

3. Type mock commands such as:
```
show ip interface brief
show version
exit
```

---

## 💡 Notes

You can customize command outputs in `mock_data/commands.yaml`.
