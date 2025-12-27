from .base_model import BaseModel

class Event(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self.name = data.get("name")
        self.year = data.get("year")
        self.century_id = data.get("century_id")
        self.source_id = data.get("source_id")
        self.confidence_id = data.get("confidence_id")
        self.region = data.get("region")
        self.event_type = data.get("event_type")