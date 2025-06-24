"""
parser.py
---------
Parses a Cisco-style 'show mac address-table' output file.
"""

def parse_mac_table(file_path="10. mac_address_table_parser/mac_table.txt"):
    entries = []
    with open(file_path, "r") as f:
        for line in f:
            if line.strip() == "" or "----" in line or "Mac Address Table" in line:
                continue
            parts = line.split()
            if len(parts) == 4:
                vlan, mac, typ, port = parts
                entries.append({
                    "vlan": vlan,
                    "mac": mac.lower(),
                    "type": typ,
                    "port": port
                })
    return entries

if __name__ == "__main__":
    import pprint
    pprint.pprint(parse_mac_table())
