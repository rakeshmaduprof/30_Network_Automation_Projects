"""
REST API Caller for Network Devices
"""

import requests
import json

CONFIG_FILE = "18. rest_api_caller/config.json"

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def call_api(config):
    try:
        response = requests.get(
            config["url"],
            auth=(config["username"], config["password"]),
            headers=config["headers"],
            verify=False  # For sandbox self-signed certs
        )
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"❌ API call failed: {e}")

def main():
    config = load_config()
    call_api(config)

if __name__ == "__main__":
    main()
