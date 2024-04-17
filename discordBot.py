import discord
import re
import json
from pyoembed import oEmbed

# this is how you get the author of the video
def get_youtube_author(video_id):
    data = oEmbed(f'https://youtu.be/{video_id}')
    return str(data['author_name'])

# Function to save the dictionary to a JSON file
def save_to_json(data, filename):
    with open(filename, 'w', encoding = "utf-8") as file:
        json.dump(data, file, indent=4)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

youtube_videos = {}

youtube_url_pattern = re.compile(r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})')

data_file = "data.txt"
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    # Check if the message author is a bot

    if message.author.bot:
        return

    await update_existing_video_messages()

    # print("message channel", (message.channel.name))

    if message.channel.name == "general":
        await process_message(message)
    # if message.content == "history":
        # print("Channel", message.channel)
        # await get_youtube_videos_in_general(message.channel)
    if message.content.lower() == "$go":

        await process_channel_history(message.channel)
    # Find YouTube video links in the message content
    matches = youtube_url_pattern.findall(message.content)
    if matches:
        # Extract video IDs from the matches
        video_ids = [match[3] for match in matches]

        # Record the Discord user who posted the message
        user = message.author

        # Process the video IDs
        for video_id in video_ids:
            # Do something with the video ID and the user (e.g., store in a database)
            print(f"User {user} posted YouTube video with ID: {video_id}")

# automatically gather all youtube videos posted in general cahnnel
@client.event
async def on_guild_join(guild):
    # Check if the general channel exists
    general_channel = discord.utils.get(guild.text_channels, name="general")
    if general_channel:
        await get_youtube_videos_in_general(general_channel)

async def update_existing_video_messages():
    # Get the channel object by name
    # print("working...")
    channel = discord.utils.get(client.get_all_channels(), name='general')
    if channel:
        print('working')
        for youtube_id in youtube_videos:
            message_id = youtube_videos[youtube_id]["message_id"]
            # print("message id", message_id)
            try:
                # Fetch the message object from Discord
                message = await channel.fetch_message(message_id)
                # print(message)
                await process_message(message)
            except discord.NotFound:
                print(f"Message with ID {message_id} not found.")
    else:
        print("Channel 'general' not found.")
    print("done")
    save_to_json(youtube_videos, 'youtube_videos.json')


async def get_youtube_videos_in_general(channel):
    async for message in channel.history(limit=None):
        await process_message(message)
        # Process each message
        # print(f"{message.author}: {message.content}")

        # Get reactions on the message
        # reactions = message.reactions
        # for reaction in reactions:
            # async for user in reaction.users():
                # print(f"User {user} reacted with {reaction.emoji}")

# Function to process channel history
async def process_channel_history(channel):
    async for message in channel.history(limit=None):
        await process_message(message)

    print(youtube_videos)
    save_to_json(youtube_videos, 'youtube_videos.json')



async def process_message(message):


    # Check if the message author is a bot or if it's not a YouTube video link
    if message.reference is not None:
        replied_message = await message.channel.fetch_message(message.reference.message_id)
        print(f"REFERENCE FOR {message.content}", replied_message.content)
    if message.author.bot or not youtube_url_pattern.search(message.content):
        return

    # Extract video ID from YouTube link
    match = youtube_url_pattern.search(message.content)
    video_id = match.group(4)

    # Update youtube_videos dictionary
    if video_id not in youtube_videos:
        # Add entry for new video
        youtube_videos[video_id] = {
            'creator': get_youtube_author(video_id),
            'curator': str(message.author),
            'consumers': {},
            'message_id': message.id

        }

    # Update consumers dictionary for the video
    consumers: dict = youtube_videos[video_id]['consumers']

    def add_to_consumer(username, reaction=None, reply=None):
        if username not in consumers:
            consumers.update({username: {"reactions": [], "replies": []}})
        if reaction is not None:
            if reaction not in consumers[username]["reactions"]:
                consumers[username]["reactions"].append(str(reaction))
        if reply is not None:
            if reply not in consumers[username]["replies"]:
                consumers[username]["replies"].append(reply)

    # add reactions
    reactions = message.reactions
    for reaction in reactions:
        # Get the users who reacted with the emoji
        async for consumer in reaction.users():
            # print(f"User {consumer} reacted with {reaction.emoji}")
            add_to_consumer(str(consumer.name), reaction=reaction.emoji)

    # consumers[str(message.author)] = {
        # 'reactions': [reaction.emoji for reaction in message.reactions],
        # 'replies': [],
        # "views": []
    # }

    # Check responses to the message
    async for response in message.channel.history(limit=None):
        if response.reference and response.reference.message_id == message.id:
            (await response.channel.fetch_message(response.reference.message_id))
            add_to_consumer(str(response.author), reply=str(response.content))
            # consumers[str(response.author)]['replies'].append(str(response.content))
            # message.channel.fetch_message(message.reference.message_id)

    # print("ALL REFERENCES", message.reference)

    # Check responses to the message
    # async for response in message.reference.channel.history(limit=None):
        # if response.reference and response.reference.message_id == message.id:
            # consumers[message.author]['responses'].append(response)


client.run('private key')