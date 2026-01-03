"""Quick test to verify bilingual data in database."""
from database.config import db_config
from database.models import Event, Century, Source

db = db_config.get_session()

try:
    # Test bilingual event
    event = db.query(Event).first()
    print("=" * 60)
    print("BILINGUAL DATA TEST")
    print("=" * 60)
    print(f"\nSample Event: {event.id}")
    print(f"Year: {event.year}")
    print(f"\nTitle (EN): {event.title['en']}")
    print(f"Title (ES): {event.title['es']}")
    print(f"\nDescription (EN): {event.description['en'][:100]}...")
    print(f"Description (ES): {event.description['es'][:100]}...")
    
    # Count all records
    print("\n" + "=" * 60)
    print("DATABASE STATISTICS")
    print("=" * 60)
    century_count = db.query(Century).count()
    event_count = db.query(Event).count()
    source_count = db.query(Source).count()
    
    print(f"Centuries: {century_count}")
    print(f"Events: {event_count}")
    print(f"Sources: {source_count}")
    
    # List all events by century
    print("\n" + "=" * 60)
    print("EVENTS BY CENTURY")
    print("=" * 60)
    centuries = db.query(Century).order_by(Century.id).all()
    for century in centuries:
        events = db.query(Event).filter(Event.century_id == century.id).count()
        print(f"{century.id}: {events} events")
    
    print("\n" + "=" * 60)
    print("✓ DATABASE TEST SUCCESSFUL")
    print("=" * 60)
    
finally:
    db.close()
