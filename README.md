# Ecclesia Timeline

Historical Christianity timeline with normalized data, REST API, and interactive visualization.

## Project Structure

```
ecclesia/
├── backend/              # Python backend with API and database
│   ├── models/          # Data models
│   ├── services/        # Data loading and validation
│   ├── database/        # SQLAlchemy ORM layer
│   ├── api/             # REST APIs (Flask & FastAPI)
│   └── tests/           # Backend tests
├── frontend/            # React timeline visualization
│   ├── src/            
│   │   ├── components/ # React components
│   │   └── services/   # API client
│   └── public/
└── archives/            # JSON data source files
```

## Quick Start

### Backend Setup

```bash
cd backend

# Using uv (recommended)
uv pip install sqlalchemy flask flask-cors pytest

# Or using pip
pip install sqlalchemy flask flask-cors pytest

# Create and seed database
python -m database.seed

# Run tests
pytest

# Start API (choose one)
python api/flask/app.py        # Flask on :5000
# OR
uvicorn api.fastapi.app:app    # FastAPI on :8000
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Configure API endpoint (edit .env if needed)
# REACT_APP_API_URL=http://localhost:5000

# Start development server
npm start
```

App opens at **http://localhost:3000**

## Features

### Backend
- ✅ **JSON Data Loading**: Loads historical data from normalized JSON files
- ✅ **SQLAlchemy Database**: SQLite (dev) / PostgreSQL (production) support
- ✅ **Repository Pattern**: Clean data access layer
- ✅ **REST APIs**: Flask and FastAPI implementations
- ✅ **Filtering**: Events by year range, region, type, confidence
- ✅ **Relationships**: Events ↔ Sources, Centuries ↔ Confidence
- ✅ **Tests**: Comprehensive test suite with pytest

### Frontend
- 📜 **Interactive Timeline**: Vertical scrolling timeline with animations
- 🎨 **Confidence Visualization**: Color-coded badges (High/Medium/Low)
- 🔍 **Dynamic Filtering**: Year range and confidence level filters
- 📱 **Responsive Design**: Desktop and mobile optimized
- ⚡ **Real-time API**: Fetches data from backend REST API
- 🌐 **Environment Config**: `.env` based configuration

## API Endpoints

```
GET  /api/summary                     # Data statistics
GET  /api/centuries                   # All centuries
GET  /api/centuries/{id}              # Specific century
GET  /api/events                      # All events
GET  /api/events?year_from=X&year_to=Y  # Filtered events
GET  /api/events/{id}                 # Specific event
GET  /api/sources                     # All sources
GET  /api/confidence                  # Confidence levels
```

## Development Workflow

### 1. Run Backend
```bash
cd backend
python api/flask/app.py
# API running on http://localhost:5000
```

### 2. Run Frontend
```bash
cd frontend
npm start
# App running on http://localhost:3000
```

### 3. View Timeline
Open browser to `http://localhost:3000`

## Testing

### Backend Tests
```bash
cd backend
pytest                    # Run all tests
pytest -v                 # Verbose output
pytest tests/test_api.py  # Specific test file
```

### Test Coverage
```bash
pytest --cov=. --cov-report=html
```

## Environment Variables

### Backend
- `DATABASE_URL` - Database connection (default: SQLite)
- `DATA_SOURCE` - "json" or "database" (default: database)

### Frontend
- `REACT_APP_API_URL` - Backend API URL (default: http://localhost:5000)

## Package Management

This project uses **uv** for Python package management:

```bash
# Install packages
uv pip install package-name

# Install from pyproject.toml
uv pip install -e .

# Install dev dependencies
uv pip install -e ".[dev]"
```

Traditional pip also works:
```bash
pip install -r requirements.txt
```

## Data Flow

```
JSON Files (archives/)
    ↓
Data Loader (services/)
    ↓
Database (SQLAlchemy)
    ↓
Repository Layer
    ↓
API Handlers (routes.py)
    ↓
Flask/FastAPI (api/)
    ↓
Frontend (React)
```

## Production Deployment

### Backend (Database)
```bash
export DATABASE_URL="postgresql://user:pass@host/db"
python -m database.seed
uvicorn api.fastapi.app:app --host 0.0.0.0 --port 8000
```

### Frontend
```bash
npm run build
# Deploy build/ folder to Vercel/Netlify/S3
```

## Documentation

- [Backend README](backend/README.md)
- [Frontend README](frontend/README.md)
- [Database Setup](backend/database/README.md)
- [API Documentation](backend/api/README.md)

## Tech Stack

**Backend:**
- Python 3.12+
- SQLAlchemy 2.0
- Flask / FastAPI
- pytest

**Frontend:**
- React 18
- Axios
- CSS3 (animations, gradients)

**Database:**
- SQLite (development)
- PostgreSQL (production)

## Contributing

1. Add data to JSON files in `archives/`
2. Run `python -m database.seed` to update database
3. Backend automatically serves new data
4. Frontend displays updated timeline

## License

MIT
