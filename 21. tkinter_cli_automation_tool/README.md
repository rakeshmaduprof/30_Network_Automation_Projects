# CLI Automation Tool (with Paramiko invoke_shell)

This is a simple GUI-based SSH automation tool built using Python's `tkinter` and `paramiko` libraries. It connects to a remote device over SSH, executes multiple CLI commands using an interactive shell (`invoke_shell()`), and displays/saves the output.

---

## 🔧 Features
- GUI for entering device IP, username, password, and CLI commands.
- Uses `paramiko`'s `invoke_shell()` to maintain an interactive session.
- Output is displayed in the app and saved to a log file.
- Each session logs output to a separate file inside a `logs/` directory.
- Non-blocking GUI using Python threads.

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install paramiko
