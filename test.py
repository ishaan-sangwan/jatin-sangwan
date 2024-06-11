import os
import json

def dir_to_json(path):
  data = {}
  if os.path.isfile(path):
    data["name"] = os.path.basename(path)
    data["type"] = "file"
  elif os.path.isdir(path):
    data["name"] = os.path.basename(path)
    data["type"] = "directory"
    data["children"] = []
    for item in os.listdir(path):
      child_path = os.path.join(path, item)
      data["children"].append(dir_to_json(child_path))
  return data

root_dir = "."  # Change this to your desired starting directory

# Initialize final JSON object
final_json = {}

# Add entries for top-level files
for file in os.listdir(root_dir):
  if file.endswith(".md") or file.endswith(".png"):
    file_path = os.path.join(root_dir, file)
    final_json[file] = None

# Add "audio" directory if it exists
audio_dir = os.path.join(root_dir, "audio")
if os.path.isdir(audio_dir):
  final_json["audio"] = dir_to_json(audio_dir)

# Convert to JSON string with indentation
json_string = json.dumps(final_json, indent=2)

print(json_string)
