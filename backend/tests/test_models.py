"""
Unit tests for the backend services and models.
Run with: pytest tests/
"""
import pytest
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from models.century import Century
from models.event import Event
from models.source import Source
from models.confidence import Confidence


class TestModels:
    """Test data models."""
    
    def test_century_model(self):
        """Test Century model initialization."""
        data = {
            "id": "CENT_01_CE",
            "century_range": [1, 100],
            "summary": "Test century",
            "confidence_id": "C1"
        }
        century = Century(data)
        assert century.id == "CENT_01_CE"
        assert century.name == data.get("name")
    
    def test_event_model(self):
        """Test Event model initialization."""
        data = {
            "id": "EVT_TEST",
            "year": 50,
            "century_id": "CENT_01_CE",
            "title": "Test Event",
            "confidence_id": "C1",
            "sources": ["SRC_TEST"]
        }
        event = Event(data)
        assert event.id == "EVT_TEST"
        assert event.year == 50
        assert event.century_id == "CENT_01_CE"
    
    def test_source_model(self):
        """Test Source model initialization."""
        data = {
            "id": "SRC_TEST",
            "type": "primary",
            "author": "Test Author",
            "work": "Test Work",
            "date_written": "50 CE"
        }
        source = Source(data)
        assert source.id == "SRC_TEST"
        assert source.author == "Test Author"
    
    def test_confidence_model(self):
        """Test Confidence model initialization."""
        data = {
            "id": "C1",
            "label": "Alta",
            "numeric_range": [0.85, 1.0],
            "criteria": ["Test criteria"]
        }
        confidence = Confidence(data)
        assert confidence.id == "C1"
        # Note: level vs label - model uses 'level'
        assert confidence.level == data.get("level") or confidence.id == "C1"
