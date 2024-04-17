import json
from pyoembed import oEmbed

# convert video data to dictionary
data = oEmbed('https://youtu.be/dQw4w9WgXcQ')
print(data)
# can replace words in "" with any match in the dictionary
print(data["author_name"])
