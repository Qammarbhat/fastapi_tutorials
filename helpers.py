from enum import Enum
from typing import Optional, List, Dict
from pydantic import BaseModel


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comments: int
    head: str
    tags: List[str]
    metadata: Dict[str, str] = {"key1": "va1"}
    image: Optional[Image] = None

class BlogType(str, Enum):
    short= "short"
    story= "story"
    howTo= "howTo"
