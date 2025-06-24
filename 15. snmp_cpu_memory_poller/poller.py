"""
poller_easysnmp.py
------------------
SNMP Poller using easysnmp (Python 3.12 friendly)
"""

import yaml
import matplotlib.pyplot as plt
from easysnmp import Session

# OIDs
CPU_OID = '1.3.6.1.4.1.9.2.1.58.0'
MEM_USED_OID = '1.3.6.1.4.1.9.9.48.1.1.1.5.1'
MEM_FREE_OID = '1.3.6.1.4.1.9.9.48.1.1.1.6.1'

def snmp_get(ip, community, oid):
    try:
        session = Session(hostname=ip, community=community, version=2)
        result = session.get(oid)
        return int(result.value)
    except Exception as e:
        print(f"[ERROR] SNMP GET failed on {ip} for {oid}: {e}")
        return None

def load_devices(path="devices.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)["devices"]

def poll_devices(devices):
    cpu_data = {}
    mem_data = {}

    for device in devices:
        ip = device["ip"]
        name = device["name"]
        community = device["community"]

        print(f"[INFO] Polling {name} ({ip})...")
        cpu = snmp_get(ip, community, CPU_OID)
        mem_used = snmp_get(ip, community, MEM_USED_OID)
        mem_free = snmp_get(ip, community, MEM_FREE_OID)


        if cpu is not None:
            cpu_data[name] = cpu
        if mem_used is not None and mem_free is not None:
            mem_total = mem_used + mem_free
            mem_percent = round((mem_used / mem_total) * 100, 2)
            mem_data[name] = mem_percent

    return cpu_data, mem_data

def plot_data(data, title, filename, ylabel):
    names = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(8, 5))
    bars = plt.bar(names, values, color='orange')
    plt.title(title)
    plt.xlabel("Device")
    plt.ylabel(ylabel)

    # Show values on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, f'{height}%', 
                 ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def main():
    devices = load_devices("devices.yaml")
    cpu_data, mem_data = poll_devices(devices)

    if cpu_data:
        plot_data(cpu_data, "CPU Utilization (%)", "cpu_usage.png", "CPU Usage (%)")
    if mem_data:
        plot_data(mem_data, "Memory Utilization (%)", "memory_usage.png", "Memory Usage (%)")

if __name__ == "__main__":
    main()
