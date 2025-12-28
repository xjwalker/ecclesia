# FastAPI - Ecclesia Timeline

Modern, high-performance API with automatic interactive documentation.

## Installation

```bash
pip install fastapi uvicorn
```

## Run the API

From the `backend` directory:

```bash
uvicorn api.fastapi.app:app --reload
```

Or from the `backend/api/fastapi` directory:
```bash
cd backend/api/fastapi
uvicorn app:app --reload
```

The API will start on **http://localhost:8000**

## Interactive Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

These docs let you test all endpoints directly in your browser!

## Test the API

```bash
# Check API is running
curl http://localhost:8000/

# Get summary
curl http://localhost:8000/api/summary

# Get all events
curl http://localhost:8000/api/events

# Filter events by century
curl http://localhost:8000/api/events?century_id=CENT_01_CE

# Filter events by year range
curl "http://localhost:8000/api/events?year_from=30&year_to=70"

# Get specific event
curl http://localhost:8000/api/events/EVT_0030_CRUCIFIXION
```

## Deploy Options

### Local Development
```bash
uvicorn app:app --reload
```

### Production
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

### With Gunicorn (Production)
```bash
pip install gunicorn
gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Docker
```bash
docker build -t ecclesia-fastapi .
docker run -p 8000:8000 ecclesia-fastapi
```

## Why FastAPI?

- ⚡ **Fast**: High performance, on par with NodeJS and Go
- 📝 **Auto Docs**: Automatic interactive API documentation
- ✅ **Type Validation**: Automatic request/response validation
- 🔧 **Modern**: Based on Python 3.12+ type hints
- 📊 **OpenAPI**: Full OpenAPI 3.0 compliance

## Environment Variables

- `PORT`: Server port (default: 8000)
- `DATA_DIR`: Path to data directory (default: ../../archives/christianity_century_1)
- `RELOAD`: Enable auto-reload on code changes (development only)
