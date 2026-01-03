"""
Check which events are missing highlights.
"""
from database.config import db_config
from database.models import Event

db = db_config.get_session()

try:
    all_events = db.query(Event).order_by(Event.year).all()
    
    print("EVENTS WITHOUT HIGHLIGHTS:")
    print("=" * 70)
    
    count = 0
    for event in all_events:
        if not event.highlight:
            count += 1
            print(f"\n{count}. Year {event.year} CE: {event.title['en']}")
            print(f"   Century: {event.century_id}")
            print(f"   Type: {event.event_type}")
    
    print(f"\n{'=' * 70}")
    print(f"Total events without highlights: {count}")
    
finally:
    db.close()
