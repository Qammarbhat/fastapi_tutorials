from enum import Enum

class BlogType(str, Enum):
    short= "short"
    story= "story"
    howTo= "howTo"
