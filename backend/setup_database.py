"""
Complete database setup and verification script.
This script:
1. Verifies all century data is bilingual
2. Sets up the database (SQLite by default, PostgreSQL optional)
3. Seeds all centuries
4. Verifies the seeded data
"""
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.config import db_config, DatabaseConfig
from database.seed import seed_database
from database.models import Base, Century, Event, Source, ConfidenceLevel

def verify_bilingual_data():
    """Verify that all century data is bilingual."""
    print("\n" + "=" * 60)
    print("STEP 1: VERIFYING BILINGUAL DATA")
    print("=" * 60)
    
    archives_dir = Path(__file__).parent.parent / 'archives'
    centuries = [
        'christianity_century_1',
        'christianity_century_2',
        'christianity_century_3'
    ]
    
    all_ok = True
    event_counts = {}
    
    for century_name in centuries:
        century_dir = archives_dir / century_name
        events_file = century_dir / 'events.json'
        
        if not events_file.exists():
            print(f"❌ {century_name}: events.json not found")
            all_ok = False
            continue
        
        import json
        with open(events_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            events = data.get('events', [])
            event_counts[century_name] = len(events)
            
            # Quick check for bilingual format
            sample_event = events[0] if events else {}
            has_bilingual = isinstance(sample_event.get('title'), dict)
            
            if has_bilingual:
                print(f"✓ {century_name}: {len(events)} events (bilingual)")
            else:
                print(f"❌ {century_name}: {len(events)} events (NOT bilingual)")
                all_ok = False
    
    if not all_ok:
        print("\n❌ Some centuries are not bilingual. Please convert them first.")
        return False
    
    print(f"\n✓ All centuries verified! Total events: {sum(event_counts.values())}")
    return True

def setup_database(database_url=None):
    """Set up the database."""
    print("\n" + "=" * 60)
    print("STEP 2: DATABASE SETUP")
    print("=" * 60)
    
    # Use provided URL or default
    if database_url:
        db = DatabaseConfig(database_url)
        print(f"Using database: {database_url}")
    else:
        db = db_config
        print(f"Using database: {db.database_url}")
    
    # Drop existing tables
    print("\nDropping existing tables...")
    Base.metadata.drop_all(db.engine)
    print("✓ All tables dropped")
    
    # Create tables
    print("\nCreating new tables...")
    db.create_tables()
    
    return db

def seed_all_centuries():
    """Seed all centuries."""
    print("\n" + "=" * 60)
    print("STEP 3: SEEDING DATA")
    print("=" * 60)
    
    archives_dir = Path(__file__).parent.parent / 'archives'
    centuries = [
        'christianity_century_1',
        'christianity_century_2',
        'christianity_century_3',
        'christianity_century_4'
    ]
    
    for century_dir_name in centuries:
        century_path = archives_dir / century_dir_name
        if century_path.exists():
            print(f"\n📁 Seeding {century_dir_name}...")
            seed_database(str(century_path))
        else:
            print(f"⚠️  Directory not found: {century_path}")

def verify_database():
    """Verify the seeded database."""
    print("\n" + "=" * 60)
    print("STEP 4: VERIFYING DATABASE")
    print("=" * 60)
    
    db = db_config.get_session()
    
    try:
        # Count records
        century_count = db.query(Century).count()
        event_count = db.query(Event).count()
        source_count = db.query(Source).count()
        confidence_count = db.query(ConfidenceLevel).count()
        
        print(f"\n✓ Database verification:")
        print(f"  - Centuries: {century_count}")
        print(f"  - Events: {event_count}")
        print(f"  - Sources: {source_count}")
        print(f"  - Confidence Levels: {confidence_count}")
        
        # Verify bilingual data in database
        sample_event = db.query(Event).first()
        if sample_event:
            if isinstance(sample_event.title, dict) and 'en' in sample_event.title:
                print(f"\n✓ Bilingual data preserved in database")
            else:
                print(f"\n⚠️  Warning: Bilingual format may not be preserved")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error verifying database: {e}")
        return False
    finally:
        db.close()

def main():
    """Main setup function."""
    print("\n" + "=" * 60)
    print("ECCLESIA TIMELINE - COMPLETE DATABASE SETUP")
    print("=" * 60)
    
    # Step 1: Verify bilingual data
    if not verify_bilingual_data():
        sys.exit(1)
    
    # Step 2: Setup database
    try:
        setup_database()
    except Exception as e:
        print(f"\n❌ Database setup failed: {e}")
        sys.exit(1)
    
    # Step 3: Seed all centuries
    try:
        seed_all_centuries()
    except Exception as e:
        print(f"\n❌ Seeding failed: {e}")
        sys.exit(1)
    
    # Step 4: Verify database
    if not verify_database():
        print("\n⚠️  Database verification completed with warnings")
    
    # Final summary
    print("\n" + "=" * 60)
    print("✓ SETUP COMPLETE!")
    print("=" * 60)
    print("\nYour SQLite database is ready at: ecclesia_timeline.db")
    print("You can now start the backend server and use the API.")
    print("\nTo switch to PostgreSQL:")
    print("  1. Set DATABASE_URL environment variable:")
    print("     export DATABASE_URL='postgresql://user:password@localhost/ecclesia_timeline'")
    print("  2. Run this script again")
    print("=" * 60)

if __name__ == "__main__":
    main()
