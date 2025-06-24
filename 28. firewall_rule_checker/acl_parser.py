import yaml

def load_config(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()

def load_policy(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def parse_acls(config_lines):
    acls = {}
    for line in config_lines:
        line = line.strip()
        if line.startswith("access-list"):
            parts = line.split()
            acl_number = parts[1]
            rule = " ".join(parts[2:])
            if acl_number not in acls:
                acls[acl_number] = []
            acls[acl_number].append(rule)
    return acls

def validate_acls(acls, policy):
    for entry in policy["expected_acls"]:
        acl_num = entry["acl"]
        required_rules = entry["required_rules"]
        actual_rules = acls.get(str(acl_num), [])
        print(f"\n[ACL {acl_num}]")
        for rule in required_rules:
            if rule in actual_rules:
                print(f"[OK] Rule exists: {rule}")
            else:
                print(f"[MISSING] Rule not found: {rule}")

if __name__ == "__main__":
    config_lines = load_config("28. firewall_rule_checker/sample_config.txt")
    policy = load_policy("28. firewall_rule_checker/policy.yaml")
    acls = parse_acls(config_lines)
    validate_acls(acls, policy)
