from flask import Flask, render_template
import os
import yaml
from snmp_utils import get_device_stats

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
DEVICE_FILE = os.path.join(BASE_DIR, "devices.yaml")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route("/")
def dashboard():
    with open(DEVICE_FILE) as f:
        devices = yaml.safe_load(f)["devices"]

    device_data = []
    for dev in devices:
        stats = get_device_stats(dev["ip"], dev["community"])
        stats["name"] = dev["name"]
        device_data.append(stats)

    return render_template("dashboard.html", devices=device_data)

if __name__ == "__main__":
    app.run(debug=True)
