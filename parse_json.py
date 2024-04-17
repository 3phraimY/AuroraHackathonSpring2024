import json

data = {
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

with open("new_data.json", "w") as json_file:
    json.dump(data, json_file, indent=2)  # Optional: Use indent for pretty formatting