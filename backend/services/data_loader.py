from pathlib import Path
from typing import Dict, List
import json

from models.century import Century
from models.event import Event
from models.source import Source
from models.confidence import Confidence


class DataLoader:
    MODELS = {
        "centuries": Century,
        "events": Event,
        "sources": Source,
        "confidence_model": Confidence,
    }

    @staticmethod
    def load_data(directory: str) -> Dict[str, List]:
        data = {}
        for file_name, model in DataLoader.MODELS.items():
            file_path = Path(directory) / f"{file_name}.json"
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            with open(file_path, "r", encoding="utf-8") as file:
                data[file_name] = [model(item) for item in json.load(file)]
        return data
