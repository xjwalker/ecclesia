"""
Test the new highlight features for doctrines and major events.
"""
from database.config import db_config
from database.models import Event, Century

db = db_config.get_session()

try:
    print("=" * 70)
    print("HIGHLIGHTED EVENTS TEST")
    print("=" * 70)
    
    # Get all centuries
    centuries = db.query(Century).order_by(Century.id).all()
    total_events = db.query(Event).count()
    
    print(f"\nTotal Centuries: {len(centuries)}")
    print(f"Total Events: {total_events}\n")
    
    # Show century summaries
    print("=" * 70)
    print("CENTURY SUMMARIES")
    print("=" * 70)
    for century in centuries:
        print(f"\n{century.id}:")
        if isinstance(century.summary, dict):
            print(f"  EN: {century.summary['en']}")
            print(f"  ES: {century.summary['es']}")
        else:
            print(f"  {century.summary}")
    
    # Show highlighted events
    print("\n" + "=" * 70)
    print("HIGHLIGHTED EVENTS BY CATEGORY")
    print("=" * 70)
    
    # Doctrine established
    print("\n📜 DOCTRINES ESTABLISHED:")
    doctrine_events = db.query(Event).filter(
        Event.highlight == 'doctrine_established'
    ).order_by(Event.year).all()
    
    for event in doctrine_events:
        print(f"\n  {event.year} CE - {event.title['en']}")
        if event.doctrine:
            print(f"    Doctrine: {event.doctrine['name']['en']}")
            print(f"    Summary: {event.doctrine['summary']['en'][:80]}...")
        if event.heresy_condemned:
            print(f"    Condemned: {event.heresy_condemned['name']['en']}")
    
    # Councils
    print("\n\n⛪ ECUMENICAL COUNCILS:")
    council_events = db.query(Event).filter(
        Event.event_type == 'Council'
    ).order_by(Event.year).all()
    
    for event in council_events:
        print(f"\n  {event.year} CE - {event.title['en']}")
        print(f"    Location: {event.region}")
        if event.doctrine:
            print(f"    Defined: {event.doctrine['name']['en']}")
    
    # Major historical events
    print("\n\n🏛️  MAJOR HISTORICAL EVENTS:")
    historical_events = db.query(Event).filter(
        Event.highlight == 'historical_event'
    ).order_by(Event.year).all()
    
    for event in historical_events:
        year_str = event.year_approx if event.year_approx else str(event.year)
        print(f"\n  {year_str} CE - {event.title['en']}")
        print(f"    Type: {event.event_type}")
        print(f"    Region: {event.region}")
    
    # Timeline of 4th century (highlighting categories)
    print("\n\n" + "=" * 70)
    print("4th CENTURY TIMELINE (301-400 CE)")
    print("=" * 70)
    
    century_4_events = db.query(Event).filter(
        Event.century_id == 'CENT_04_CE'
    ).order_by(Event.year).all()
    
    for event in century_4_events:
        year_str = event.year_approx if event.year_approx else str(event.year)
        
        # Add emoji based on highlight type
        emoji = ""
        if event.highlight == 'doctrine_established':
            emoji = "📜"
        elif event.highlight == 'historical_event':
            emoji = "🏛️"
        elif event.event_type == 'Council':
            emoji = "⛪"
        else:
            emoji = "•"
        
        print(f"\n{year_str:>8} CE {emoji} {event.title['en']}")
        
        if event.doctrine:
            print(f"             └─ Doctrine: {event.doctrine['name']['en']}")
        if event.heresy_condemned:
            print(f"             └─ Condemned: {event.heresy_condemned['name']['en']}")
    
    # Statistics
    print("\n\n" + "=" * 70)
    print("STATISTICS")
    print("=" * 70)
    
    doctrine_count = db.query(Event).filter(
        Event.highlight == 'doctrine_established'
    ).count()
    
    historical_count = db.query(Event).filter(
        Event.highlight == 'historical_event'
    ).count()
    
    council_count = db.query(Event).filter(
        Event.event_type == 'Council'
    ).count()
    
    print(f"\nDoctrine Events: {doctrine_count}")
    print(f"Historical Events: {historical_count}")
    print(f"Councils: {council_count}")
    print(f"Total Events: {total_events}")
    
    print("\n" + "=" * 70)
    print("✓ HIGHLIGHT FEATURES TEST COMPLETED")
    print("=" * 70)
    
finally:
    db.close()
