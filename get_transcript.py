from collections import Counter
import re

from youtube_transcript_api import YouTubeTranscriptApi
from collections import Counter
import re

video_id = "v7-YprDdMyw"

transcript = YouTubeTranscriptApi.get_transcript(video_id)

print(transcript)

def extract_keywords(transcript):
    # Common filler words to exclude
    common_filler_words = ['the', 'a', 'an', 'i', 'you', 'we', 'they', 'is', 'are', 'am', 'it', 'and', 'or', 'but', 'this','will','After','in','than']

    # Tokenize the transcript by words
    words = re.findall(r'\b\w+\b', transcript.lower())

    # Exclude common filler words
    filtered_words = [word for word in words if word not in common_filler_words]

    # Count the frequency of each word
    word_freq = Counter(filtered_words)

    # Get the most common word
    most_common_word = word_freq.most_common(10)

    return most_common_word

# Example YouTube transcript
youtube_transcript = transcript_text

# Extract keywords from the YouTube transcript
keyword = extract_keywords(youtube_transcript)

print("The most common keyword in the transcript is:", keyword[0][0])