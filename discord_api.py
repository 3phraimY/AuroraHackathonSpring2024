import requests

def read_message(channel_id, token):
    url = f"https://discord.com/api/v9/channels/922898869233287170/messages"
   
    header = {
        "Authorization": f"{token}"
    }

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        messages = response.json()
        return messages
    else:
        print("Failed to fetch messages.")
        print(response.text)
        return None

token = "YOUR DISCORD TOKEN"
channel_id = "CHANNEL ID"

messages = read_message(channel_id, token)

if messages:
    for message in messages:
        print(f"{message['content']}")
        print(f"{message['author']}")
        print(f"{message['timestamp']}")
else:
    print("Failed to read messages.")