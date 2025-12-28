"""
Seed database from JSON files.
Loads the existing JSON data into the database.
"""
import json
from pathlib import Path
from database.config import db_config
from database.models import Century, Event, Source, ConfidenceLevel


def load_json_data(data_directory: str):
    """Load JSON data from files."""
    data_dir = Path(data_directory)
    
    # Load all JSON files
    with open(data_dir / "centuries.json", "r", encoding="utf-8") as f:
        centuries_data = json.load(f).get("centuries", [])
    
    with open(data_dir / "events.json", "r", encoding="utf-8") as f:
        events_data = json.load(f).get("events", [])
    
    with open(data_dir / "sources.json", "r", encoding="utf-8") as f:
        sources_data = json.load(f).get("sources", [])
    
    with open(data_dir / "confidence_model.json", "r", encoding="utf-8") as f:
        confidence_data = json.load(f).get("confidence_levels", [])
    
    return {
        "centuries": centuries_data,
        "events": events_data,
        "sources": sources_data,
        "confidence_levels": confidence_data
    }


def seed_confidence_levels(db, confidence_data):
    """Seed confidence levels."""
    print("Seeding confidence levels...")
    added_count = 0
    for item in confidence_data:
        # Check if already exists
        existing = db.query(ConfidenceLevel).filter_by(id=item["id"]).first()
        if existing:
            print(f"  Skipping {item['id']} (already exists)")
            continue
            
        confidence = ConfidenceLevel(
            id=item["id"],
            label=item["label"],
            numeric_range=item["numeric_range"],
            criteria=item["criteria"],
            description=item.get("description")
        )
        db.add(confidence)
        added_count += 1
    db.commit()
    print(f"✓ Added {added_count} confidence levels")


def seed_sources(db, sources_data):
    """Seed sources."""
    print("Seeding sources...")
    sources_map = {}
    added_count = 0
    for item in sources_data:
        # Check if already exists
        existing = db.query(Source).filter_by(id=item["id"]).first()
        if existing:
            print(f"  Skipping {item['id']} (already exists)")
            sources_map[item["id"]] = existing
            continue
            
        source = Source(
            id=item["id"],
            type=item["type"],
            author=item.get("author"),
            work=item["work"],
            date_written=item.get("date_written"),
            language=item.get("language"),
            notes=item.get("notes"),
            citation_info=item.get("citation_info")
        )
        db.add(source)
        sources_map[item["id"]] = source
        added_count += 1
    db.commit()
    print(f"✓ Added {added_count} sources")
    return sources_map


def seed_centuries(db, centuries_data, sources_map):
    """Seed centuries."""
    print("Seeding centuries...")
    centuries_map = {}
    for item in centuries_data:
        century = Century(
            id=item["id"],
            century_range=item["century_range"],
            summary=item["summary"],
            confidence_id=item["confidence_id"]
        )
        
        # Add source relationships
        if "sources" in item:
            for source_id in item["sources"]:
                if source_id in sources_map:
                    century.sources.append(sources_map[source_id])
        
        db.add(century)
        centuries_map[item["id"]] = century
    db.commit()
    print(f"✓ Added {len(centuries_data)} centuries")
    return centuries_map


def seed_events(db, events_data, sources_map):
    """Seed events."""
    print("Seeding events...")
    for item in events_data:
        event = Event(
            id=item["id"],
            year=item.get("year"),
            year_approx=item.get("year_approx"),
            century_id=item["century_id"],
            title=item["title"],
            description=item.get("description"),
            context=item.get("context"),
            confidence_rationale=item.get("confidence_rationale"),
            significance=item.get("significance"),
            people_involved=item.get("people_involved"),
            image_url=item.get("image_url"),
            region=item.get("region"),
            event_type=item.get("event_type"),
            confidence_id=item["confidence_id"]
        )
        
        # Add source relationships
        if "sources" in item:
            for source_id in item["sources"]:
                if source_id in sources_map:
                    event.sources.append(sources_map[source_id])
        
        db.add(event)
    db.commit()
    print(f"✓ Added {len(events_data)} events")


def seed_database(data_directory: str, reset: bool = False):
    """
    Seed the database from JSON files.
    
    Args:
        data_directory: Path to JSON data files
        reset: If True, drop all tables before seeding
    """
    print("=" * 50)
    print("Database Seeding")
    print("=" * 50)
    
    # Reset database if requested
    if reset:
        print("⚠ Resetting database (dropping all tables)...")
        db_config.drop_tables()
    
    # Create tables
    db_config.create_tables()
    
    # Load JSON data
    print("\nLoading JSON data...")
    data = load_json_data(data_directory)
    print(f"✓ Loaded data from {data_directory}")
    
    # Get database session
    db = db_config.get_session()
    
    try:
        # Seed in order (dependencies first)
        seed_confidence_levels(db, data["confidence_levels"])
        sources_map = seed_sources(db, data["sources"])
        centuries_map = seed_centuries(db, data["centuries"], sources_map)
        seed_events(db, data["events"], sources_map)
        
        print("\n" + "=" * 50)
        print("✓ Database seeded successfully!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n✗ Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # Seed from default data directory
    data_dir = "../archives/christianity_century_1"
    seed_database(data_dir, reset=True)
