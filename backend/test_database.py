"""
Test script to verify database operations.
"""
from database.config import db_config
from database.repository import EventRepository, CenturyRepository, SourceRepository, ConfidenceLevelRepository


def test_database():
    """Test database queries."""
    print("=" * 50)
    print("Testing Database Layer")
    print("=" * 50)
    
    db = db_config.get_session()
    
    try:
        # Test 1: Get all centuries
        print("\n1. Testing Centuries:")
        centuries = CenturyRepository.get_all(db)
        print(f"   Found {len(centuries)} centuries")
        for century in centuries:
            print(f"   - {century.id}: {century.summary[:50]}...")
        
        # Test 2: Get all events
        print("\n2. Testing Events:")
        events = EventRepository.get_all(db)
        print(f"   Found {len(events)} events")
        for event in events[:3]:  # Show first 3
            print(f"   - {event.year}: {event.title}")
        
        # Test 3: Filter events by year range
        print("\n3. Testing Event Filtering (years 30-60):")
        filtered = EventRepository.filter_events(db, year_from=30, year_to=60)
        print(f"   Found {len(filtered)} events")
        for event in filtered:
            print(f"   - {event.year}: {event.title}")
        
        # Test 4: Get event with relationships
        print("\n4. Testing Event Relationships:")
        event = EventRepository.get_by_id(db, "EVT_0030_CRUCIFIXION")
        if event:
            print(f"   Event: {event.title}")
            print(f"   Year: {event.year}")
            print(f"   Confidence: {event.confidence.label if event.confidence else 'N/A'}")
            print(f"   Sources: {len(event.sources)}")
            for source in event.sources:
                print(f"      - {source.work} by {source.author}")
        
        # Test 5: Get sources
        print("\n5. Testing Sources:")
        sources = SourceRepository.get_all(db)
        print(f"   Found {len(sources)} sources")
        for source in sources:
            print(f"   - {source.id}: {source.work}")
        
        # Test 6: Get confidence levels
        print("\n6. Testing Confidence Levels:")
        levels = ConfidenceLevelRepository.get_all(db)
        print(f"   Found {len(levels)} confidence levels")
        for level in levels:
            print(f"   - {level.id} ({level.label}): {level.numeric_range}")
        
        print("\n" + "=" * 50)
        print("✓ All tests passed!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    test_database()
