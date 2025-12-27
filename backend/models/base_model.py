from typing import Any, Dict


class BaseModel:
    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__
