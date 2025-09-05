# IP Reachability & Latency Checker

## 📌 Project Description
This project automates the process of checking reachability and latency of multiple devices (network devices or servers) using **ICMP ping**.  
The script will:
- Ping a list of IP addresses.
- Collect results (Reachable/Unreachable + Latency).
- Save the results into a **CSV report** with a timestamp.

This is a common use case in network monitoring and troubleshooting.

---

## ⚙️ Requirements
- Python 3.7+
- Libraries:
  - `subprocess` (built-in)
  - `platform` (built-in)
  - `csv` (built-in)
  - `datetime` (built-in)

No third-party packages are required.

---

## 📂 Files
- `ping_checker.py` → Main script  
- `requirements.txt` → Dependencies list  
- `README.md` → Project documentation  
- `ping_report_YYYYMMDD-HHMMSS.csv` → Generated CSV report  

---

## 🚀 Usage

1. Clone or download the project.
2. Edit the IP list inside the script:
   ```python
   devices = ["192.168.35.136", "192.168.35.138", "8.8.8.8", "1.1.1.1"]
