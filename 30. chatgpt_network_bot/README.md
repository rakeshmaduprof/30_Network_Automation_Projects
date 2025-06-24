# ChatGPT-integrated Network Bot (Local Prompt)

A Python-based chatbot that uses prompt templates and local logic to answer questions about your network inventory/config.

---

## 📁 Contents

- `bot.py` – Main chatbot logic using templates
- `inventory.json` – Mock network inventory data
- `templates/response_template.txt` – Prompt template
- `requirements.txt` – Dependencies

---

## ⚙️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the chatbot:
```bash
python bot.py
```

3. Sample questions:
```
> What devices are running IOS version 15?
> List all devices in building A.
> Show me the hostname of 192.168.1.1
```

---

## 🧠 How It Works

- Loads network data from `inventory.json`
- Accepts natural questions
- Matches them to simple prompt templates
- Returns structured responses

This version doesn't need internet or API keys; it mimics chatbot logic locally.

