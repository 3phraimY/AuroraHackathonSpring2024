from dataclasses import dataclass

#each video has Creator, Consumer, Curator, keywords
CurrentVideoIndex = 0

@dataclass
class NormalFormat:
    VideoIndex: int
    Creator: str
    Consumer: str
    Keywords: []

#Example of how to build and append NormalFormat class

#Video12 = [1,2]
#Video1 = NormalFormat(1,"test1","Creator",Video12)
#JSON = []
#JSON.append(Video1)
#print(JSON[1])