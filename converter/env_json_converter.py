import os
import json
import sys

def env_to_json(env_file_path, json_file_path):
    """
    Convert a .env file to a JSON file.

    :param env_file_path: Path to the .env file
    :param json_file_path: Path to save the JSON file
    """
    try:
        # Check if .env file exists
        if not os.path.exists(env_file_path):
            print(f"Error: The file '{env_file_path}' does not exist.")
            sys.exit(1)

        env_dict = {}

        # Read and parse the .env file
        with open(env_file_path, 'r') as env_file:
            for line in env_file:
                line = line.strip()
                # Skip empty lines or comments
                if line == "" or line.startswith('#'):
                    continue
                
                # Split key and value by the first "="
                if "=" in line:
                    key, value = line.split("=", 1)
                    env_dict[key.strip()] = value.strip()

        # Write to the JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(env_dict, json_file, indent=4)
        
        print(f"JSON file saved successfully at '{json_file_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def json_to_env(json_file_path, env_file_path):
    """
    Convert a JSON file to a .env file.

    :param json_file_path: Path to the JSON file
    :param env_file_path: Path to save the .env file
    """
    try:
        # Check if JSON file exists
        if not os.path.exists(json_file_path):
            print(f"Error: The file '{json_file_path}' does not exist.")
            sys.exit(1)

        # Read and parse the JSON file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        # Write to the .env file
        with open(env_file_path, 'w') as env_file:
            for key, value in data.items():
                env_file.write(f"{key}={value}\n")
        
        print(f".env file saved successfully at '{env_file_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py <action> <input_file_path> <output_file_path>")
        print("Actions: 'env-to-json' or 'json-to-env'")
        sys.exit(1)
    
    action = sys.argv[1].lower()
    input_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    if action == "env-to-json":
        env_to_json(input_file_path, output_file_path)
    elif action == "json-to-env":
        json_to_env(input_file_path, output_file_path)
    else:
        print("Error: Invalid action. Use 'env-to-json' or 'json-to-env'.")
        sys.exit(1)

