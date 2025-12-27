from .base_model import BaseModel

class Source(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self.title = data.get("title")
        self.author = data.get("author")
        self.year = data.get("year")