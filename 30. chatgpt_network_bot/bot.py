import json
from jinja2 import Template

# Load network inventory
with open("30. chatgpt_network_bot/inventory.json", "r") as f:
    inventory = json.load(f)
    print(inventory)

# Load response template
with open("30. chatgpt_network_bot/templates/response_template.txt", "r") as f:
    response_template = Template(f.read())
    print(response_template)

def search_inventory(question):
    if "ios version 15" in question.lower():
        return [d for d in inventory if d["os_version"].startswith("15")]
    elif "building a" in question.lower():
        return [d for d in inventory if d["location"].lower() == "building a"]
    elif "hostname of" in question.lower():
        ip = question.split()[-1]
        return [d for d in inventory if d["ip"] == ip]
    else:
        return []

def main():
    print("Network Bot Ready (local). Type 'exit' to quit.")
    while True:
        question = input("> ").strip()
        if question.lower() == "exit":
            break
        results = search_inventory(question)
        if results:
            output = response_template.render(devices=results)
            print(output)
        else:
            print("I couldn't find relevant data.")

if __name__ == "__main__":
    main()
