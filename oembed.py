# make sure you execute "pip install pyoembed." Recommend doing this as admin

from pyoembed import oEmbed

try:
    data = oEmbed('https://youtu.be/dQw4w9WgXcQ', maxwidth=640, maxheight=480)
    print(data)
    
except:
    print("Error: unable to parse provided URL.")
