"""
Tests for database operations.
"""
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from database.config import DatabaseConfig
from database.models import Century, Event, Source, ConfidenceLevel
from database.repository import (
    CenturyRepository, 
    EventRepository, 
    SourceRepository,
    ConfidenceLevelRepository
)


@pytest.fixture(scope="module")
def test_db():
    """Create a test database."""
    # Use in-memory SQLite for testing
    db_config = DatabaseConfig("sqlite:///:memory:")
    db_config.create_tables()
    
    # Seed test data
    db = db_config.get_session()
    
    # Add confidence level
    conf = ConfidenceLevel(
        id="C1",
        label="High",
        numeric_range=[0.85, 1.0],
        criteria=["Test criteria"]
    )
    db.add(conf)
    
    # Add source
    source = Source(
        id="SRC_TEST",
        type="primary",
        work="Test Work"
    )
    db.add(source)
    
    # Add century
    century = Century(
        id="CENT_TEST",
        century_range=[1, 100],
        summary="Test century",
        confidence_id="C1"
    )
    db.add(century)
    
    # Add events
    for i in range(5):
        event = Event(
            id=f"EVT_TEST_{i}",
            year=30 + (i * 10),
            century_id="CENT_TEST",
            title=f"Test Event {i}",
            confidence_id="C1"
        )
        db.add(event)
    
    db.commit()
    
    yield db_config
    
    db.close()


class TestEventRepository:
    """Test Event repository operations."""
    
    def test_get_all_events(self, test_db):
        """Test getting all events."""
        db = test_db.get_session()
        events = EventRepository.get_all(db)
        assert len(events) == 5
        db.close()
    
    def test_get_event_by_id(self, test_db):
        """Test getting event by ID."""
        db = test_db.get_session()
        event = EventRepository.get_by_id(db, "EVT_TEST_0")
        assert event is not None
        assert event.title == "Test Event 0"
        db.close()
    
    def test_filter_events_by_year_range(self, test_db):
        """Test filtering events by year range."""
        db = test_db.get_session()
        events = EventRepository.filter_events(db, year_from=30, year_to=50)
        assert len(events) == 3  # Events at 30, 40, 50
        db.close()
    
    def test_filter_events_by_century(self, test_db):
        """Test filtering events by century."""
        db = test_db.get_session()
        events = EventRepository.filter_events(db, century_id="CENT_TEST")
        assert len(events) == 5
        db.close()


class TestCenturyRepository:
    """Test Century repository operations."""
    
    def test_get_all_centuries(self, test_db):
        """Test getting all centuries."""
        db = test_db.get_session()
        centuries = CenturyRepository.get_all(db)
        assert len(centuries) == 1
        db.close()
    
    def test_get_century_by_id(self, test_db):
        """Test getting century by ID."""
        db = test_db.get_session()
        century = CenturyRepository.get_by_id(db, "CENT_TEST")
        assert century is not None
        assert century.summary == "Test century"
        db.close()


class TestSourceRepository:
    """Test Source repository operations."""
    
    def test_get_all_sources(self, test_db):
        """Test getting all sources."""
        db = test_db.get_session()
        sources = SourceRepository.get_all(db)
        assert len(sources) == 1
        db.close()


class TestConfidenceLevelRepository:
    """Test ConfidenceLevel repository operations."""
    
    def test_get_all_confidence_levels(self, test_db):
        """Test getting all confidence levels."""
        db = test_db.get_session()
        levels = ConfidenceLevelRepository.get_all(db)
        assert len(levels) == 1
        db.close()
