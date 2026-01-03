# Database Setup Guide

## Overview

This project uses **SQLite by default** with support for **PostgreSQL**. All data is stored in bilingual format (English and Spanish).

## Current Status

✅ **All 3 centuries are bilingual and ready**:
- Century 1 (1-100 CE): 11 events
- Century 2 (101-200 CE): 6 events  
- Century 3 (201-300 CE): 5 events

Total: **22 events, 49 sources, 3 confidence levels**

## Quick Start

### Option 1: Complete Setup (Recommended)

Run the complete setup script that verifies data and seeds the database:

```bash
cd backend
python setup_database.py
```

This script will:
1. ✅ Verify all century data is bilingual
2. 🗄️ Create database tables
3. 📊 Seed all centuries
4. ✔️ Verify the seeded data

### Option 2: Quick Reseed

If you just need to reseed existing database:

```bash
cd backend
python reseed_db.py
```

Or use the alternative:

```bash
cd backend
python reseed_all_centuries.py
```

## Database Configuration

### Using SQLite (Default)

No configuration needed! The database file will be created at:
```
backend/ecclesia_timeline.db
```

### Switching to PostgreSQL

1. **Set environment variable:**
   ```bash
   # Windows PowerShell
   $env:DATABASE_URL="postgresql://user:password@localhost/ecclesia_timeline"
   
   # Linux/Mac
   export DATABASE_URL="postgresql://user:password@localhost/ecclesia_timeline"
   ```

2. **Install PostgreSQL driver:**
   ```bash
   pip install psycopg2-binary
   ```

3. **Create the database:**
   ```sql
   CREATE DATABASE ecclesia_timeline;
   ```

4. **Run setup:**
   ```bash
   python setup_database.py
   ```

## Verifying Century Data

To check if all centuries have bilingual data:

```bash
cd archives
python verify_centuries.py
```

## Database Schema

### Tables

- **centuries**: Historical centuries (1st, 2nd, 3rd CE)
- **events**: Historical events with bilingual content
- **sources**: Primary and secondary sources
- **confidence_levels**: Evidence quality ratings (C1, C2, C3)
- **event_sources**: Many-to-many relationship
- **century_sources**: Many-to-many relationship

### Bilingual Fields

All text content is stored as JSON with language keys:

```json
{
  "title": {
    "en": "Crucifixion of Jesus",
    "es": "Crucifixión de Jesús"
  },
  "description": {
    "en": "Execution of Jesus...",
    "es": "Ejecución de Jesús..."
  }
}
```

Bilingual fields include:
- `title`
- `description`
- `context`
- `confidence_rationale`
- `significance`
- Person names and roles in `people_involved`

## API Access

After seeding, you can start the API server:

```bash
cd backend
python -m api.fastapi_app
# or
python -m api.flask_app
```

The API will serve bilingual content based on the `language` parameter (default: 'es').

## Adding More Centuries

To add Century 4, 5, etc.:

1. **Create data directory:**
   ```
   archives/christianity_century_4/
   ├── centuries.json
   ├── events.json
   ├── sources.json
   └── confidence_model.json
   ```

2. **Ensure bilingual format:**
   All events must have bilingual fields as shown above.

3. **Verify:**
   ```bash
   python archives/verify_centuries.py
   ```

4. **Update seeding scripts:**
   Add the new century to the list in:
   - `backend/reseed_db.py`
   - `backend/reseed_all_centuries.py`
   - `backend/setup_database.py`

5. **Reseed:**
   ```bash
   python backend/setup_database.py
   ```

## Troubleshooting

### Database locked (SQLite)

If you get "database is locked" errors:
- Close any open connections to the database
- Delete `ecclesia_timeline.db` and run setup again

### Missing packages

```bash
pip install sqlalchemy
# For PostgreSQL support:
pip install psycopg2-binary
```

### Data not bilingual

Run the verification script:
```bash
python archives/verify_centuries.py
```

If issues are found, you'll need to convert the data. See `archives/convert_century_2.py` for an example conversion script.

## File Structure

```
backend/
├── setup_database.py       # Complete setup with verification
├── reseed_db.py           # Quick reseed script
├── reseed_all_centuries.py # Alternative reseed script
├── ecclesia_timeline.db   # SQLite database (created after setup)
├── database/
│   ├── config.py          # Database configuration
│   ├── models.py          # SQLAlchemy models
│   └── seed.py            # Seeding logic
└── api/
    ├── fastapi_app.py     # FastAPI server
    └── flask_app.py       # Flask server

archives/
├── verify_centuries.py    # Verification script
├── christianity_century_1/
├── christianity_century_2/
└── christianity_century_3/
```

## Next Steps

1. ✅ Database is ready with SQLite
2. 🚀 Start the API server
3. 🌐 Connect the frontend
4. 📊 Add more centuries as needed
5. 🔄 Optionally migrate to PostgreSQL for production

For PostgreSQL migration in production, simply set the `DATABASE_URL` environment variable and run the setup script again. The data will be migrated automatically.
