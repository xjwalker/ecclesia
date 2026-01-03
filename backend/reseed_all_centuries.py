"""
Reseed database with all three centuries, including the new Century 3.
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.seed import seed_database
from database.config import db_config
from database.models import Base

# Get the archives directory
archives_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'archives')

# Drop existing tables
print("Dropping existing tables...")
Base.metadata.drop_all(db_config.engine)
print("✓ All tables dropped")

# Create tables
print("Creating new tables...")
db_config.create_tables()
print(f"✓ Database tables created")

# Seed each century
centuries = [
    'christianity_century_1',
    'christianity_century_2',
    'christianity_century_3',
    'christianity_century_4'
]

for century_dir in centuries:
    century_path = os.path.join(archives_dir, century_dir)
    if os.path.exists(century_path):
        print(f"\nSeeding from: {century_path}")
        seed_database(century_path)
    else:
        print(f"⚠️  Directory not found: {century_path}")

print("\n✓ Database reseeded successfully with all three centuries!")
