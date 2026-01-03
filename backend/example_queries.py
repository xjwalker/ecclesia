"""
Example queries showing how to work with bilingual data.
Run this to see how to query and display bilingual content.
"""
from database.config import db_config
from database.models import Event, Century, Source, ConfidenceLevel

def example_1_get_event_bilingual():
    """Example 1: Get a single event in both languages."""
    print("\n" + "=" * 60)
    print("EXAMPLE 1: Get Event in Both Languages")
    print("=" * 60)
    
    db = db_config.get_session()
    try:
        event = db.query(Event).filter_by(id="EVT_0030_CRUCIFIXION").first()
        
        print(f"\nEvent ID: {event.id}")
        print(f"Year: {event.year}")
        print(f"\nEnglish:")
        print(f"  Title: {event.title['en']}")
        print(f"  Description: {event.description['en'][:100]}...")
        print(f"\nEspañol:")
        print(f"  Título: {event.title['es']}")
        print(f"  Descripción: {event.description['es'][:100]}...")
        
    finally:
        db.close()

def example_2_get_events_by_century():
    """Example 2: Get all events for a century."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Get Events by Century")
    print("=" * 60)
    
    db = db_config.get_session()
    try:
        century = db.query(Century).filter_by(id="CENT_01_CE").first()
        events = db.query(Event).filter_by(century_id=century.id).all()
        
        print(f"\nCentury: {century.id}")
        print(f"Total Events: {len(events)}")
        print(f"\nEvents (English):")
        for event in events[:3]:  # Show first 3
            print(f"  • {event.year} CE - {event.title['en']}")
        
        print(f"\nEventos (Español):")
        for event in events[:3]:
            print(f"  • {event.year} CE - {event.title['es']}")
        
    finally:
        db.close()

def example_3_api_like_response():
    """Example 3: Format response like API would."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: API-like Response")
    print("=" * 60)
    
    db = db_config.get_session()
    try:
        event = db.query(Event).filter_by(id="EVT_0110_IGNATIUS").first()
        
        # English response
        response_en = {
            "id": event.id,
            "year": event.year,
            "title": event.title['en'],
            "description": event.description['en'],
            "region": event.region,
            "event_type": event.event_type
        }
        
        # Spanish response
        response_es = {
            "id": event.id,
            "year": event.year,
            "title": event.title['es'],
            "description": event.description['es'],
            "region": event.region,
            "event_type": event.event_type
        }
        
        print("\n/api/events/EVT_0110_IGNATIUS?language=en")
        print(f"Title: {response_en['title']}")
        print(f"Description: {response_en['description'][:80]}...")
        
        print("\n/api/events/EVT_0110_IGNATIUS?language=es")
        print(f"Título: {response_es['title']}")
        print(f"Descripción: {response_es['description'][:80]}...")
        
    finally:
        db.close()

def example_4_search_by_type():
    """Example 4: Search events by type."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Search by Event Type")
    print("=" * 60)
    
    db = db_config.get_session()
    try:
        martyrdom_events = db.query(Event).filter(
            Event.event_type.in_(['execution', 'Martyrdom'])
        ).all()
        
        print(f"\nFound {len(martyrdom_events)} martyrdom/execution events:\n")
        
        print("English:")
        for event in martyrdom_events[:5]:
            print(f"  • {event.year} CE - {event.title['en']}")
        
        print("\nEspañol:")
        for event in martyrdom_events[:5]:
            print(f"  • {event.year} CE - {event.title['es']}")
        
    finally:
        db.close()

def example_5_with_sources():
    """Example 5: Get event with its sources."""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Event with Sources")
    print("=" * 60)
    
    db = db_config.get_session()
    try:
        event = db.query(Event).filter_by(id="EVT_0048_PAUL_MISSION").first()
        
        print(f"\nEvent: {event.title['en']}")
        print(f"Year: {event.year} CE")
        print(f"Confidence: {event.confidence_id}")
        print(f"\nSources ({len(event.sources)}):")
        for source in event.sources[:5]:  # Show first 5
            print(f"  • {source.id}: {source.work}")
            if source.author:
                print(f"    Author: {source.author}")
        
    finally:
        db.close()

def example_6_people_involved():
    """Example 6: Get people involved in an event."""
    print("\n" + "=" * 60)
    print("EXAMPLE 6: People Involved in Event")
    print("=" * 60)
    
    db = db_config.get_session()
    try:
        event = db.query(Event).filter_by(id="EVT_0030_CRUCIFIXION").first()
        
        print(f"\nEvent: {event.title['en']}")
        print(f"\nPeople Involved:")
        
        for person in event.people_involved:
            # Handle both old and new formats
            if 'name' in person:
                name_en = person['name'].get('en', person.get('name_en', 'N/A'))
                name_es = person['name'].get('es', person.get('name_es', 'N/A'))
                role_en = person['role'].get('en', person.get('role_en', 'N/A'))
                role_es = person['role'].get('es', person.get('role_es', 'N/A'))
            else:
                name_en = person.get('name_en', 'N/A')
                name_es = person.get('name_es', 'N/A')
                role_en = person.get('role_en', 'N/A')
                role_es = person.get('role_es', 'N/A')
            
            print(f"  • {name_en} / {name_es}")
            print(f"    Role: {role_en} / {role_es}")
        
    finally:
        db.close()

def example_7_timeline_view():
    """Example 7: Timeline view of all events."""
    print("\n" + "=" * 60)
    print("EXAMPLE 7: Timeline View (Chronological)")
    print("=" * 60)
    
    db = db_config.get_session()
    try:
        events = db.query(Event).order_by(Event.year).all()
        
        print(f"\nChristianity Timeline ({events[0].year}-{events[-1].year} CE)")
        print(f"Total Events: {len(events)}\n")
        
        for event in events:
            year_str = event.year_approx if event.year_approx else str(event.year)
            print(f"{year_str:>8} CE | {event.title['en']}")
        
    finally:
        db.close()

def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("BILINGUAL DATA QUERY EXAMPLES")
    print("=" * 60)
    print("\nThis script demonstrates how to query and use bilingual data")
    print("from the Ecclesia Timeline database.\n")
    
    example_1_get_event_bilingual()
    example_2_get_events_by_century()
    example_3_api_like_response()
    example_4_search_by_type()
    example_5_with_sources()
    example_6_people_involved()
    example_7_timeline_view()
    
    print("\n" + "=" * 60)
    print("✓ ALL EXAMPLES COMPLETED")
    print("=" * 60)
    print("\nThese examples show how to:")
    print("  • Query bilingual data from the database")
    print("  • Access both English and Spanish content")
    print("  • Format responses for API endpoints")
    print("  • Work with relationships (sources, people)")
    print("  • Filter and search events")
    print("\nUse these patterns in your API routes and frontend!")
    print("=" * 60)

if __name__ == "__main__":
    main()
