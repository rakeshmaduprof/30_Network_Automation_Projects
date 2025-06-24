import tkinter as tk
from tkinter import scrolledtext, messagebox
import paramiko
import threading
import os
import time

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def run_ssh(ip, username, password, commands, output_box):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, timeout=5, look_for_keys=False, allow_agent=False)

        output_box.insert(tk.END, f"Connected to {ip}\n")

        shell = ssh.invoke_shell()
        time.sleep(1)  # Give shell time to respond
        shell.send('terminal len 0'+"\n")

        log_filename = os.path.join(LOG_DIR, f"output_{ip.replace('.', '_')}.txt")
        with open(log_filename, "w") as log_file:
            shell.recv(1000)  # Clear initial banner

            for cmd in commands.splitlines():
                if cmd.strip():
                    output_box.insert(tk.END, f"Running: {cmd}\n")
                    shell.send(cmd + '\n')
                    time.sleep(1.5)  # Wait for command to complete

                    output = shell.recv(5000).decode(errors='ignore')
                    output_box.insert(tk.END, output + "\n")
                    log_file.write(f"Command: {cmd}\n{output}\n{'-'*40}\n")

        ssh.close()
        output_box.insert(tk.END, f"Done. Output saved to {log_filename}\n")

    except Exception as e:
        output_box.insert(tk.END, f"Error: {str(e)}\n")
        messagebox.showerror("Connection Error", str(e))

def start_ssh_thread(ip, username, password, commands, output_box):
    threading.Thread(
        target=run_ssh,
        args=(ip, username, password, commands, output_box),
        daemon=True
    ).start()

def create_gui():
    window = tk.Tk()
    window.title("CLI Automation Tool")

    tk.Label(window, text="Device IP:").grid(row=0, column=0, sticky="w")
    ip_entry = tk.Entry(window, width=30)
    ip_entry.grid(row=0, column=1)

    tk.Label(window, text="Username:").grid(row=1, column=0, sticky="w")
    user_entry = tk.Entry(window, width=30)
    user_entry.grid(row=1, column=1)

    tk.Label(window, text="Password:").grid(row=2, column=0, sticky="w")
    pass_entry = tk.Entry(window, width=30, show="*")
    pass_entry.grid(row=2, column=1)

    tk.Label(window, text="Commands (one per line):").grid(row=3, column=0, sticky="nw")
    cmd_text = tk.Text(window, width=50, height=10)
    cmd_text.grid(row=3, column=1)

    tk.Label(window, text="Output:").grid(row=4, column=0, sticky="nw")
    output_box = scrolledtext.ScrolledText(window, width=60, height=15)
    output_box.grid(row=4, column=1)

    def on_run():
        ip = ip_entry.get()
        user = user_entry.get()
        passwd = pass_entry.get()
        commands = cmd_text.get("1.0", tk.END)
        output_box.delete("1.0", tk.END)
        start_ssh_thread(ip, user, passwd, commands, output_box)

    run_btn = tk.Button(window, text="Run Commands", command=on_run)
    run_btn.grid(row=5, column=1, sticky="e", pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
