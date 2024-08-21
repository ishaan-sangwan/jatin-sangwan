#! /bin/bash

function dir_to_json() {
  local path="$1"

  if [[ ! -d "$path" ]]; then
    return 1  # Path is not a directory
  fi

  local json="{"
  for item in "$path/"*; do
    local filename="${item##*/}"
    local filetype=""

    if [[ -f "$item" ]]; then
      # Get file extension (remove leading .)
      filetype="${filename##*.}"
    fi

    # Add entry with filename and "null" value, optionally including filetype
    if [[ -f "$item" ]]; then
      json+="\"$filename\": null,"
      
    fi

    # Recursively call for subdirectories
    if [[ -d "$item" ]]; then
      local child_json="$(dir_to_json "$item")"
      if [[ $? -eq 0 ]]; then  # Check for successful recursion
        json+="\"$filename\":$child_json,"
      fi
    fi
  done

  # Remove trailing comma
  json="${json%,}"

  # Close JSON object
  json+="}"
  echo $json
}

root_dir="."  # Change this to your desired starting directory

# Get JSON representation of the directory tree
json="$(dir_to_json "$root_dir")"

# Check for successful execution
if [[ $? -eq 0 ]]; then
  echo "$json"
else
  echo "Error: An error occurred while processing the directory tree."
fi
