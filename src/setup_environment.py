import os
import json

def get_executables_list():
    executables_list = []

    for root, dirs, files in os.walk("C:\\"):
        for file in files:
            if file.lower().endswith(".exe"):
                file_path = os.path.join(root, file)
                executables_list.append(file_path)

    return executables_list

def create_commands_config(executables_list):
    commands_config = {"commands": {}}

    for exe_path in executables_list:
        exe_name = os.path.basename(exe_path).replace(".exe", "")
        command_name = f"open_{exe_name.lower()}"
        commands_config["commands"][command_name] = {"action": "open", "target": exe_path}

    with open("commands_config.json", "w") as config_file:
        json.dump(commands_config, config_file, indent=4)

if __name__ == "__main__":
    print("Setting up environment...")
    
    executables_list = get_executables_list()

    if not executables_list:
        print("No executable files found. Exiting.")
        exit()

    create_commands_config(executables_list)
    print("Environment setup complete. Configuration stored in commands_config.json.")
