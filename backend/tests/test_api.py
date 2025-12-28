"""
Integration tests for API handlers.
"""
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from api.routes import APIHandler


class TestAPIHandler:
    """Test API handler operations."""
    
    @pytest.fixture
    def api_handler(self):
        """Create API handler instance."""
        return APIHandler("../archives/christianity_century_1")
    
    def test_get_summary(self, api_handler):
        """Test getting data summary."""
        summary = api_handler.get_summary()
        assert "total_events" in summary
        assert "total_centuries" in summary
        assert summary["total_events"] > 0
    
    def test_get_centuries(self, api_handler):
        """Test getting all centuries."""
        centuries = api_handler.get_centuries()
        assert len(centuries) > 0
        assert "id" in centuries[0]
    
    def test_get_events(self, api_handler):
        """Test getting all events."""
        events = api_handler.get_events()
        assert len(events) > 0
        assert "id" in events[0]
        assert "year" in events[0]
    
    def test_filter_events_by_year_range(self, api_handler):
        """Test filtering events by year range."""
        events = api_handler.get_events(year_from=30, year_to=60)
        assert len(events) > 0
        for event in events:
            assert 30 <= event["year"] <= 60
    
    def test_get_event_by_id(self, api_handler):
        """Test getting specific event."""
        event = api_handler.get_event_by_id("EVT_0030_CRUCIFIXION")
        assert event is not None
        assert event["id"] == "EVT_0030_CRUCIFIXION"
    
    def test_get_sources(self, api_handler):
        """Test getting all sources."""
        sources = api_handler.get_sources()
        assert len(sources) > 0
        assert "id" in sources[0]
    
    def test_get_confidence_levels(self, api_handler):
        """Test getting confidence levels."""
        levels = api_handler.get_confidence_levels()
        assert len(levels) > 0
        assert "id" in levels[0]
