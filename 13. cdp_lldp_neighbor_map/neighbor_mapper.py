"""
neighbor_mapper.py
------------------
Discover CDP neighbors and visualize the network with hostname + IP.
"""

import re
import yaml
from netmiko import ConnectHandler
import networkx as nx
import matplotlib.pyplot as plt


def load_devices(file="13. cdp_lldp_neighbor_map/devices.yaml"):
    """Load devices from YAML inventory"""
    with open(file, "r") as f:
        return yaml.safe_load(f)["devices"]


def parse_cdp_detail(output):
    """Extract management IPs from 'show cdp entry *' output"""
    neighbor_ips = {}
    blocks = output.split("-------------------------")
    for block in blocks:
        hostname_match = re.search(r"Device ID: (\S+)", block)
        ip_match = re.search(r"IP address: (\d+\.\d+\.\d+\.\d+)", block)
        if hostname_match:
            hostname = hostname_match.group(1)
            ip = ip_match.group(1) if ip_match else None
            neighbor_ips[hostname] = ip
    return neighbor_ips


def get_neighbors(device):
    """Fetch CDP neighbors and IPs from a device"""
    try:
        conn = ConnectHandler(**device)

        # CDP parsed summary
        cdp_neighbors = conn.send_command("show cdp neighbors", use_textfsm=True)
        # Detailed CDP for IP extraction
        cdp_detail_raw = conn.send_command("show cdp entry *")
        neighbor_ip_map = parse_cdp_detail(cdp_detail_raw)

        # Local hostname
        hostname = conn.find_prompt().strip("#>")

        conn.disconnect()
        return device["ip"], hostname, cdp_neighbors, neighbor_ip_map
    except Exception as e:
        print(f"Error connecting to {device['ip']}: {e}")
        return device["ip"], "Unknown", [], {}


def build_graph(neighbor_data):
    """Build graph using CDP neighbors"""
    G = nx.Graph()

    # Map hostnames to IPs
    host_ip_map = {}
    for ip, hostname, _, neigh_ips in neighbor_data:
        host_ip_map[hostname] = ip
        host_ip_map.update(neigh_ips)

    for local_ip, local_host, neighbors, neigh_ips in neighbor_data:
        local_label = f"{local_host}\n({local_ip})"
        G.add_node(local_label)

        if isinstance(neighbors, list):
            for n in neighbors:
                if not isinstance(n, dict):
                    continue

                remote_host = n.get("neighbor_name")
                local_intf = n.get("local_interface", "")
                remote_intf = n.get("neighbor_interface", "")

                if not remote_host:
                    continue

                remote_ip = host_ip_map.get(remote_host, "Unknown")
                if remote_ip and remote_ip != "Unknown":
                    remote_label = f"{remote_host}\n({remote_ip})"
                else:
                    remote_label = remote_host

                G.add_node(remote_label)
                G.add_edge(local_label, remote_label,
                           label=f"{local_intf} ↔ {remote_intf}")

    return G


def visualize_graph(G):
    """Draw and save topology graph"""
    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=2200, edgecolors="black")
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight="bold")

    nx.draw_networkx_edges(G, pos, width=1.2, edge_color="gray")
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    plt.title("CDP Neighbor Network Map")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("network_topology.png")
    plt.show()


def main():
    devices = load_devices()
    neighbor_data = []
    for device in devices:
        ip, hostname, neighbors, neigh_ips = get_neighbors(device)
        neighbor_data.append((ip, hostname, neighbors, neigh_ips))
    G = build_graph(neighbor_data)
    visualize_graph(G)


if __name__ == "__main__":
    main()
