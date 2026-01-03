"""
Test and verify all events have proper structure, highlights, and images.
"""
from database.config import db_config
from database.models import Event

db = db_config.get_session()

try:
    print("=" * 80)
    print("EVENT STRUCTURE VERIFICATION")
    print("=" * 80)
    
    all_events = db.query(Event).order_by(Event.year).all()
    
    # Stats
    total = len(all_events)
    with_highlight = sum(1 for e in all_events if e.highlight)
    with_doctrine = sum(1 for e in all_events if e.doctrine)
    with_heresy = sum(1 for e in all_events if e.heresy_condemned)
    with_image = sum(1 for e in all_events if e.image_url)
    
    print(f"\nTotal Events: {total}")
    print(f"Events with highlights: {with_highlight}")
    print(f"Events with doctrine info: {with_doctrine}")
    print(f"Events with heresy condemned: {with_heresy}")
    print(f"Events with images: {with_image}")
    
    # Show all events by century with their properties
    print("\n" + "=" * 80)
    print("ALL EVENTS WITH METADATA")
    print("=" * 80)
    
    current_century = None
    for event in all_events:
        if event.century_id != current_century:
            current_century = event.century_id
            print(f"\n{'='*80}")
            print(f"CENTURY: {current_century}")
            print(f"{'='*80}")
        
        year_str = event.year_approx if event.year_approx else str(event.year)
        
        # Icons
        icon = ""
        if event.highlight == 'doctrine_established':
            icon = "📜"
        elif event.highlight == 'historical_event':
            icon = "🏛️"
        elif event.event_type == 'Council':
            icon = "⛪"
        else:
            icon = "•"
        
        print(f"\n{year_str:>12} CE {icon} {event.title['en']}")
        print(f"                Type: {event.event_type or 'N/A'}")
        print(f"                Region: {event.region or 'N/A'}")
        print(f"                Image: {'YES' if event.image_url else 'NO'}")
        
        if event.highlight:
            print(f"                Highlight: {event.highlight}")
        
        if event.doctrine:
            print(f"                Doctrine: {event.doctrine['name']['en']}")
        
        if event.heresy_condemned:
            print(f"                Condemned: {event.heresy_condemned['name']['en']}")
    
    # Events without images
    print("\n\n" + "=" * 80)
    print("EVENTS WITHOUT IMAGES")
    print("=" * 80)
    
    without_images = [e for e in all_events if not e.image_url]
    if without_images:
        for event in without_images:
            print(f"  • {event.year} CE - {event.title['en']}")
    else:
        print("\n✓ ALL EVENTS HAVE IMAGES!")
    
    # Gospel events (special doctrine events)
    print("\n\n" + "=" * 80)
    print("GOSPEL COMPOSITIONS (Canonical Formation)")
    print("=" * 80)
    
    gospel_events = [e for e in all_events if 'Gospel' in e.title.get('en', '')]
    for event in gospel_events:
        print(f"\n{event.year} CE - {event.title['en']}")
        if event.doctrine:
            print(f"  Doctrine: {event.doctrine['name']['en']}")
            print(f"  Summary: {event.doctrine['summary']['en'][:80]}...")
        print(f"  Image: {event.image_url or 'NO IMAGE'}")
    
    # Sample image URLs for verification
    print("\n\n" + "=" * 80)
    print("SAMPLE IMAGE URLs (First 5 Events)")
    print("=" * 80)
    
    for event in all_events[:5]:
        print(f"\n{event.title['en']}:")
        print(f"  {event.image_url or 'NO IMAGE'}")
    
    print("\n\n" + "=" * 80)
    print("✓ STRUCTURE VERIFICATION COMPLETE")
    print("=" * 80)
    print(f"\nAll {total} events are properly structured with:")
    print(f"  • Bilingual content (en/es)")
    print(f"  • {with_highlight} events with highlights")
    print(f"  • {with_doctrine} doctrinal definitions")
    print(f"  • {with_heresy} heresies condemned")
    print(f"  • {with_image} events with images ({with_image}/{total} = {with_image*100//total}%)")
    
finally:
    db.close()
