"""
Reseed the database with all centuries.
This script drops existing tables, creates new ones, and seeds data from all centuries.
By default uses SQLite (ecclesia_timeline.db).
"""
from pathlib import Path
from database.config import DatabaseConfig
from database.seed import seed_database

# Initialize database
db = DatabaseConfig()

print("=" * 60)
print("DATABASE RESEEDING")
print("=" * 60)
print(f"Database: {db.database_url}\n")

# Drop and recreate tables
print("Dropping existing tables...")
db.drop_tables()

print("Creating new tables...")
db.create_tables()

# Seed with data from all centuries
base_dir = Path(__file__).parent.parent / 'archives'
century_dirs = [
    base_dir / 'christianity_century_1',
    base_dir / 'christianity_century_2',
    base_dir / 'christianity_century_3',
    base_dir / 'christianity_century_4'
]

for century_dir in century_dirs:
    if century_dir.exists():
        print(f"\nSeeding from: {century_dir}")
        seed_database(str(century_dir))
    else:
        print(f"\n⚠️  Directory not found: {century_dir}")

print("\n" + "=" * 60)
print("✓ Database reseeded successfully!")
print("=" * 60)
