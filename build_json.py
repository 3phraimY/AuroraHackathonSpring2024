from dataclasses import dataclass
import json
import os

# Define the JSON file path
json_file = 'data.json'

# Check if the JSON file exists and is not empty
if os.path.exists(json_file) and os.path.getsize(json_file) > 0:
    # Open the existing JSON file and load its contents into data
    with open(json_file) as file_in:
        data = json.load(file_in)
else:
    # If the file doesn't exist or is empty, initialize data as an empty list
    data = []

new_entry = {
    "title": "video title",
    "author": "video author",
    "publish_date": "1/1/2024",
    "keywords": [
        "gold", 
        "investor", 
        "world"
        ],
    "curator": "Arik Johnson",
    "consumers": [
        "John Doe",
        "Jane Doe",
        "Rick Astly",
        "Tom Jones"
    ]
}

# Add the new object to the array
data.append(new_entry)

# Write the updated data back to the JSON file
with open(json_file, "w") as file_out:
    json.dump(data, file_out, indent=2)
