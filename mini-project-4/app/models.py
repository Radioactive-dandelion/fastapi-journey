from typing import Dict
from pydantic import BaseModel
from uuid import uuid4

class Poll:
    def __init__(self, question: str, options: list[str]):
        self.id = str(uuid4())
        self.question = question
        self.options = options
        self.votes: Dict[str, int] = {option: 0 for option in options}