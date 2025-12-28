"""Script to reseed the database with new schema."""
from pathlib import Path
from database.config import DatabaseConfig
from database.seed import seed_database

# Initialize database
db = DatabaseConfig()

# Drop and recreate tables
print("Dropping existing tables...")
db.drop_tables()

print("Creating new tables...")
db.create_tables()

# Seed with data from all centuries
base_dir = Path(__file__).parent.parent / 'archives'
century_dirs = [
    base_dir / 'christianity_century_1',
    base_dir / 'christianity_century_2'
]

for century_dir in century_dirs:
    if century_dir.exists():
        print(f"\nSeeding from: {century_dir}")
        seed_database(str(century_dir))

print("\n✓ Database reseeded successfully!")
