# Ecclesia Timeline API

REST API for serving historical Christianity timeline data.

## Quick Start

Choose your preferred framework:

### Option 1: Flask (Simple & Proven)
```bash
pip install flask flask-cors
python api/flask/app.py
```
API runs on http://localhost:5000

📖 **[Flask Documentation →](flask/README.md)**

### Option 2: FastAPI (Modern & Fast)
```bash
pip install fastapi uvicorn
uvicorn api.fastapi.app:app --reload
```
API runs on http://localhost:8000  
Interactive docs at http://localhost:8000/docs

📖 **[FastAPI Documentation →](fastapi/README.md)**

## Endpoints

### Core Endpoints
- `GET /` - API info and available endpoints
- `GET /api/summary` - Data summary statistics

### Centuries
- `GET /api/centuries` - List all centuries
- `GET /api/centuries/{id}` - Get specific century

### Events
- `GET /api/events` - List all events (with filters)
  - Query params: `century_id`, `year`, `year_from`, `year_to`, `confidence_id`
- `GET /api/events/{id}` - Get specific event

### Sources
- `GET /api/sources` - List all historical sources
- `GET /api/sources/{id}` - Get specific source

### Confidence Levels
- `GET /api/confidence` - List all confidence levels
- `GET /api/confidence/{id}` - Get specific confidence level

## Example Queries

```bash
# Get all events
curl http://localhost:5000/api/events

# Filter events by century
curl http://localhost:5000/api/events?century_id=CENT_01_CE

# Filter events by year range
curl http://localhost:5000/api/events?year_from=30&year_to=70

# Get specific event
curl http://localhost:5000/api/events/EVT_0030_CRUCIFIXION
```

## Architecture

- `routes.py` - Framework-agnostic business logic (APIHandler class)
- `flask_app.py` - Flask implementation
- `fastapi_app.py` - FastAPI implementation

Both implementations use the same APIHandler, making it easy to switch or deploy multiple options.
