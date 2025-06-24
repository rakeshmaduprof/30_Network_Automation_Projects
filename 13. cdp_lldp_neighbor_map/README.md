# CDP/LLDP Neighbor Discovery Map

This project connects to Cisco network devices via SSH, runs CDP/LLDP neighbor discovery commands, and visualizes the network topology using Python graph libraries.

---

## ✅ Features

- Discover neighbors using `show cdp neighbors` or `show lldp neighbors`
- Visualize network topology using `networkx` and `matplotlib`
- Export the graph as an image

---

## 🗂️ Project Files

- `devices.yaml` — Device credentials and IPs
- `neighbor_mapper.py` — SSH logic, neighbor parsing, and visualization
- `requirements.txt` — Required Python packages

---

## 🛠️ Prerequisites

```bash
pip install -r requirements.txt
```

Ensure that:
- Devices support and have CDP or LLDP enabled
- SSH is configured and accessible
- The username/password/IPs in `devices.yaml` are correct

---

## 🧾 Example Output

A graph of devices connected based on neighbor relationships is shown in a popup window and saved as `network_topology.png`.

---

## ▶️ Run the Project

```bash
python neighbor_mapper.py
```

---

## 🔐 Security Note

Do not hardcode passwords in production. Use environment variables or secure vaults instead.
