from dataclasses import dataclass
#loop though all video entries in discord servers

#each video has Creator, Consumer, Curator, keywords
CurrentVideoIndex = 0

@dataclass
class NormalFormat:
    VideoIndex: int
    Creator: str
    Consumer: str
    Keywords: []
    
Video12 = [1,2]
Video1 = NormalFormat(1,"test1","Creator",Video12)

JSON = []

JSON.append(Video1)
print(JSON)