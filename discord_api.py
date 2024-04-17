# make sure you execute "pip install pyoembed." Recommend doing this as admin

import requests
from pyoembed import oEmbed
from youtube_transcript_api import YouTubeTranscriptApi



# API retrieving video creator and title
def get_video(url):
    try:
        data = oEmbed(url, maxwidth=640, maxheight=480)
        print(data)
        print("\n")
    except:
        print("Error: unable to parse provided URL.")



# API retrieving video transcript
def get_transcript(video_id):
    try:
        results = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ""

        for i in range(0,len(results)):
            transcript_text = transcript_text + " " + results[i]["text"]
        print(transcript_text + "\n")
    except:
        print("Error: unable to retrieve transcript for provided video id")


# Discord API reading message content and metadata from General Channel
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
        print("Message: " + message['content'])
        json = message['author']
        print("Curator: " + json["username"])
        print("Date: " + message['timestamp'] + "\n")

else:
    print("Failed to read messages.")

url = "https://www.youtube.com/watch?v=v7-YprDdMyw"
video_id = "v7-YprDdMyw"

get_video(url)
get_transcript(video_id)