import os
import json

def dir_to_json(path):
    if not os.path.isdir(path):
        return None  # Path is not a directory

    json_dict = {}
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path):
            json_dict[item] = None  # File with null value

        elif os.path.isdir(item_path):
            child_json = dir_to_json(item_path)
            if child_json is not None:
                json_dict[item] = child_json

    return json_dict

root_dir = "."  # Change this to your desired starting directory

# Get JSON representation of the directory tree
json_representation = dir_to_json(root_dir)

# Check for successful execution
if json_representation is not None:
    print(json.dumps(json_representation, indent=4))
else:
    print("Error: An error occurred while processing the directory tree.")
