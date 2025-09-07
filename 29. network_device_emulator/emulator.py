import yaml
import os

def load_commands(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)['commands']

def main():
    commands = load_commands("29. network_device_emulator/mock_data/commands.yaml")
    print("Mock Network Device CLI")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("Router# ").strip()
            if user_input.lower() == "exit":
                print("Exiting CLI...")
                break
            elif user_input in commands:
                print(commands[user_input])
            else:
                print("% Invalid input detected at '^' marker.")
        except KeyboardInterrupt:
            print("\nExiting CLI...")
            break

if __name__ == "__main__":
    if not os.path.exists("29. network_device_emulator/mock_data/commands.yaml"):
        print("Missing command definitions in '29. network_device_emulator/mock_data/commands.yaml'.")
    else:
        main()
