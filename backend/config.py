"""
Configuration for choosing between JSON or Database backend.
"""
import os
from enum import Enum


class DataSource(Enum):
    """Available data sources."""
    JSON = "json"
    DATABASE = "database"


class Config:
    """Application configuration."""
    
    # Data source selection
    DATA_SOURCE = os.getenv("DATA_SOURCE", "database").lower()
    
    # JSON data directory
    JSON_DATA_DIR = os.getenv("JSON_DATA_DIR", "../archives/christianity_century_1")
    
    # Database URL
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///ecclesia_timeline.db")
    
    @classmethod
    def use_database(cls) -> bool:
        """Check if database should be used."""
        return cls.DATA_SOURCE == DataSource.DATABASE.value
    
    @classmethod
    def use_json(cls) -> bool:
        """Check if JSON files should be used."""
        return cls.DATA_SOURCE == DataSource.JSON.value


def get_api_handler():
    """
    Factory function to get the appropriate API handler.
    Returns either JSON-based or Database-based handler.
    """
    if Config.use_database():
        from api.routes_db import DatabaseAPIHandler
        print(f"✓ Using DATABASE backend: {Config.DATABASE_URL}")
        return DatabaseAPIHandler()
    else:
        from api.routes import APIHandler
        print(f"✓ Using JSON backend: {Config.JSON_DATA_DIR}")
        return APIHandler(Config.JSON_DATA_DIR)
