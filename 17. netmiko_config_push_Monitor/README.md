# 🚀 Netmiko Configuration Push Tool (Enhanced)

This Python script automates the process of connecting to multiple network devices (Cisco) and pushing configuration commands using **Netmiko** over **SSH or Telnet**.

> ⚠️ Uses Netmiko, not deprecated telnetlib. Adds logging, rich output, timing, and more.

---

## 🧠 Features

- ✅ Supports SSH and Telnet (via Netmiko)
- 📁 Loads device info from `devices.csv`
- 🧾 Loads commands from `config.txt`
- 📂 Saves per-device logs in the `logs/` directory
- ⏱️ Shows time taken per device
- 🖼️ Uses [Rich](https://github.com/Textualize/rich) for colored terminal output
- 🚫 Optional dry-run mode for testing

---

## 📁 File Structure

