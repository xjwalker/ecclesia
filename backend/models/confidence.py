from .base_model import BaseModel

class Confidence(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self.level = data.get("level")
        self.description = data.get("description")