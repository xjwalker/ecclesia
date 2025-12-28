# Database Layer - Ecclesia Timeline

SQLAlchemy-based database layer with support for SQLite, PostgreSQL, and MySQL.

## Features

- ✅ SQLAlchemy ORM models matching JSON structure
- ✅ Repository pattern for clean data access
- ✅ Support for SQLite (dev) and PostgreSQL (production)
- ✅ Database seeding from JSON files
- ✅ Proper relationships and foreign keys
- ✅ Indexed fields for efficient queries

## Installation

```bash
pip install sqlalchemy psycopg2-binary  # For PostgreSQL
# OR
pip install sqlalchemy pymysql  # For MySQL
# OR just SQLAlchemy for SQLite
pip install sqlalchemy
```

## Quick Start

### 1. Create Database Tables

```python
from database.config import db_config

# Create all tables
db_config.create_tables()
```

### 2. Seed Database from JSON

```bash
cd backend
python -m database.seed
```

This will:
- Create all tables
- Load data from JSON files
- Establish all relationships

### 3. Use in Your Code

```python
from database.config import db_config, get_db
from database.repository import EventRepository

# Get a database session
db = db_config.get_session()

# Query events
events = EventRepository.filter_events(
    db, 
    year_from=30, 
    year_to=70,
    confidence_id="C1"
)

# Convert to dict for API
events_dict = [event.to_dict() for event in events]

db.close()
```

## Database Configuration

Set the `DATABASE_URL` environment variable:

### SQLite (Default - Development)
```bash
# No configuration needed, uses: sqlite:///ecclesia_timeline.db
```

### PostgreSQL (Production)
```bash
export DATABASE_URL="postgresql://user:password@localhost/ecclesia_timeline"
```

### MySQL
```bash
export DATABASE_URL="mysql+pymysql://user:password@localhost/ecclesia_timeline"
```

## Models

### Century
- Historical centuries with date ranges
- Related to confidence levels and sources
- Contains multiple events

### Event
- Individual historical events
- Year, century, region, type
- Related to confidence levels and sources
- Supports approximate dates

### Source
- Historical source documents
- Primary, secondary, or scholarly
- Author, work, date written

### ConfidenceLevel
- Historical confidence ratings (C1, C2, C3)
- Numeric ranges and criteria

## Repository Methods

### EventRepository
```python
# Get all events
events = EventRepository.get_all(db)

# Get by ID
event = EventRepository.get_by_id(db, "EVT_0030_CRUCIFIXION")

# Filter events
events = EventRepository.filter_events(
    db,
    century_id="CENT_01_CE",
    year_from=30,
    year_to=100,
    confidence_id="C1"
)
```

### CenturyRepository
```python
centuries = CenturyRepository.get_all(db)
century = CenturyRepository.get_by_id(db, "CENT_01_CE")
```

### SourceRepository
```python
sources = SourceRepository.get_all(db)
primary_sources = SourceRepository.get_by_type(db, "primary")
```

### ConfidenceLevelRepository
```python
levels = ConfidenceLevelRepository.get_all(db)
level = ConfidenceLevelRepository.get_by_id(db, "C1")
```

## Migrations

For production, consider using Alembic for migrations:

```bash
pip install alembic
alembic init alembic
# Edit alembic.ini and alembic/env.py
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Example: Reset and Reseed Database

```python
from database.seed import seed_database

# Reset database and seed from JSON
seed_database("../archives/christianity_century_1", reset=True)
```

## Integration with API

The database layer integrates seamlessly with Flask and FastAPI. See the API implementations for examples of using the repository pattern with database sessions.
