"""
Verify that all centuries have bilingual data.
Checks each century's events.json to ensure all fields have both 'en' and 'es' keys.
"""
import json
from pathlib import Path

def is_bilingual_field(field):
    """Check if a field is in bilingual format (dict with 'en' and 'es' keys)."""
    if not isinstance(field, dict):
        return False
    return 'en' in field and 'es' in field

def verify_events(events_file):
    """Verify that events have bilingual fields."""
    with open(events_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    events = data.get('events', [])
    issues = []
    
    for event in events:
        event_id = event.get('id', 'UNKNOWN')
        
        # Check required bilingual fields
        bilingual_fields = ['title', 'description', 'context', 'confidence_rationale', 'significance']
        
        for field in bilingual_fields:
            if field in event:
                if not is_bilingual_field(event[field]):
                    issues.append(f"  ❌ {event_id}: '{field}' is not bilingual")
            else:
                issues.append(f"  ⚠️  {event_id}: '{field}' is missing")
        
        # Check people_involved if present
        if 'people_involved' in event:
            for i, person in enumerate(event['people_involved']):
                if not is_bilingual_field(person.get('name', {})):
                    if 'name_en' in person and 'name_es' in person:
                        # Old format but acceptable
                        pass
                    else:
                        issues.append(f"  ⚠️  {event_id}: person[{i}] name not bilingual")
                
                if not is_bilingual_field(person.get('role', {})):
                    if 'role_en' in person and 'role_es' in person:
                        # Old format but acceptable
                        pass
                    else:
                        issues.append(f"  ⚠️  {event_id}: person[{i}] role not bilingual")
    
    return issues

def verify_all_centuries():
    """Verify all centuries."""
    archives_dir = Path(__file__).parent
    centuries = [
        'christianity_century_1',
        'christianity_century_2',
        'christianity_century_3',
        'christianity_century_4'
    ]
    
    print("=" * 60)
    print("BILINGUAL DATA VERIFICATION")
    print("=" * 60)
    
    all_ok = True
    
    for century_name in centuries:
        century_dir = archives_dir / century_name
        events_file = century_dir / 'events.json'
        
        print(f"\n📁 Checking {century_name}...")
        
        if not events_file.exists():
            print(f"  ❌ events.json not found!")
            all_ok = False
            continue
        
        issues = verify_events(events_file)
        
        if issues:
            print(f"  ❌ Found {len(issues)} issues:")
            for issue in issues[:10]:  # Show first 10 issues
                print(issue)
            if len(issues) > 10:
                print(f"  ... and {len(issues) - 10} more issues")
            all_ok = False
        else:
            # Count events
            with open(events_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                event_count = len(data.get('events', []))
            print(f"  ✓ All {event_count} events are properly bilingual!")
    
    print("\n" + "=" * 60)
    if all_ok:
        print("✓ ALL CENTURIES ARE BILINGUAL!")
    else:
        print("⚠️  SOME CENTURIES HAVE ISSUES - See above")
    print("=" * 60)
    
    return all_ok

if __name__ == "__main__":
    verify_all_centuries()
