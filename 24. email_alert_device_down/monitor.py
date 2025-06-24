import os
import smtplib
import yaml
from email.mime.text import MIMEText

def load_devices(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip()]

def load_email_settings(config_file):
    with open(config_file) as f:
        config = yaml.safe_load(f)
    return config["email_settings"]

def is_device_reachable(ip):
    response = os.system(f"ping -c 2 -W 2 {ip} > /dev/null 2>&1")
    return response == 0

def send_email_alert(email_settings, down_devices):
    subject = "ALERT: Device(s) Down"
    body = "The following device(s) are unreachable:\n\n" + "\n".join(down_devices)
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = email_settings["sender_email"]
    msg["To"] = email_settings["receiver_email"]

    try:
        with smtplib.SMTP(email_settings["smtp_server"], email_settings["smtp_port"]) as server:
            server.starttls()
            server.login(email_settings["sender_email"], email_settings["sender_password"])
            server.send_message(msg)
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    devices = load_devices("24. email_alert_device_down/devices.txt")
    email_settings = load_email_settings("24. email_alert_device_down/alert_config.yaml")
    down = []

    for ip in devices:
        print(f"Pinging {ip}...", end=" ")
        if is_device_reachable(ip):
            print("✅ UP")
        else:
            print("❌ DOWN")
            down.append(ip)

    if down:
        send_email_alert(email_settings, down)

if __name__ == "__main__":
    main()
