from .base_model import BaseModel

class Century(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self.name = data.get("name")
        self.start_year = data.get("start_year")
        self.end_year = data.get("end_year")