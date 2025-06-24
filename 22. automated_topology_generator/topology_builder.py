import csv
import paramiko
import networkx as nx
import matplotlib.pyplot as plt
import time

DEVICE_FILE = "22. automated_topology_generator/devices.csv"

def get_cdp_neighbors(ip, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, timeout=5, look_for_keys=False, allow_agent=False)

        # Start an interactive shell session
        shell = ssh.invoke_shell()
        shell.recv(1000)  # Clear the banner

        # Disable paging
        shell.send("terminal length 0\n")
        time.sleep(1)
        shell.recv(1000)

        # Run CDP command
        shell.send("show cdp neighbors detail\n")
        time.sleep(3)  # Adjust if needed for large output

        output = shell.recv(10000).decode('utf-8')
        ssh.close()

        # Optional: save raw CDP output to file for debugging
        with open(f"cdp_output_{ip}.txt", "w") as f:
            f.write(output)

        neighbors = []
        current_neighbor = {}

        for line in output.splitlines():
            line = line.strip()
            if "Device ID" in line:
                current_neighbor = {"local_ip": ip}
                current_neighbor["device_id"] = line.split("Device ID:")[1].strip()
            elif "IP address:" in line and current_neighbor:
                current_neighbor["neighbor_ip"] = line.split("IP address:")[1].strip()

            # If both local and neighbor IPs are present, save the link
            if "local_ip" in current_neighbor and "neighbor_ip" in current_neighbor:
                neighbors.append((current_neighbor["local_ip"], current_neighbor["neighbor_ip"]))
                current_neighbor = {}

        return neighbors

    except Exception as e:
        print(f"[!] Error on {ip}: {e}")
        return []

def load_devices():
    with open(DEVICE_FILE) as f:
        reader = csv.DictReader(f)
        return list(reader)

def build_topology(devices):
    G = nx.Graph()
    for device in devices:
        ip = device["ip"]
        user = device["username"]
        passwd = device["password"]
        neighbors = get_cdp_neighbors(ip, user, passwd)
        for src, dst in neighbors:
            G.add_edge(src, dst)
    return G

def draw_topology(graph):
    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=3000, font_size=10)
    plt.title("Network Topology via CDP")
    plt.tight_layout()
    plt.show()
    # Optional: save to file
    # plt.savefig("topology.png")

if __name__ == "__main__":
    devices = load_devices()
    graph = build_topology(devices)
    draw_topology(graph)
