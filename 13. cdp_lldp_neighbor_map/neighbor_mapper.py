"""
neighbor_mapper.py
------------------
Discover CDP/LLDP neighbors and visualize the network.
"""

import yaml
from netmiko import ConnectHandler
import networkx as nx
import matplotlib.pyplot as plt

def load_devices(file="13. cdp_lldp_neighbor_map/devices.yaml"):
    with open(file, "r") as f:
        return yaml.safe_load(f)["devices"]

def get_neighbors(device):
    try:
        conn = ConnectHandler(**device)
        output = conn.send_command("show cdp neighbors", use_textfsm=True)
        conn.disconnect()
        return device["ip"], output
    except Exception as e:
        print(f"Error connecting to {device['ip']}: {e}")
        return device["ip"], []

def build_graph(neighbor_data):
    G = nx.Graph()
    for local_ip, neighbors in neighbor_data:
        local_node = f"{local_ip}"
        G.add_node(local_node)
        if isinstance(neighbors, list):
            for n in neighbors:
                remote_node = n.get("destination_host", "Unknown")
                G.add_edge(local_node, remote_node)
    return G

def visualize_graph(G):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1500, font_size=10, font_weight="bold")
    plt.title("CDP Neighbor Network Map")
    plt.savefig("network_topology.png")
    plt.show()

def main():
    devices = load_devices()
    neighbor_data = []
    for device in devices:
        ip, neighbors = get_neighbors(device)
        neighbor_data.append((ip, neighbors))
    G = build_graph(neighbor_data)
    visualize_graph(G)

if __name__ == "__main__":
    main()
