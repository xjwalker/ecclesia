"""
FastAPI implementation for Ecclesia Timeline.
Run with: uvicorn api.fastapi_app:app --reload
"""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from api.routes import APIHandler

# Initialize FastAPI app
app = FastAPI(
    title="Ecclesia Timeline API",
    description="Historical Christianity timeline API with normalized data",
    version="1.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize API handler with data
DATA_DIR = "../archives/christianity_century_1"
try:
    api_handler = APIHandler(DATA_DIR)
    print("✓ Data loaded successfully")
except Exception as e:
    print(f"✗ Error loading data: {e}")
    api_handler = None


@app.get("/")
async def root():
    """API root endpoint."""
    return {
        "name": "Ecclesia Timeline API",
        "version": "1.0",
        "status": "running",
        "docs": "/docs",
        "endpoints": {
            "summary": "/api/summary",
            "centuries": "/api/centuries",
            "events": "/api/events",
            "sources": "/api/sources",
            "confidence": "/api/confidence"
        }
    }


@app.get("/api/summary")
async def get_summary():
    """Get data summary statistics."""
    if not api_handler:
        raise HTTPException(status_code=500, detail="Data not loaded")
    return api_handler.get_summary()


@app.get("/api/centuries")
async def get_centuries():
    """Get all centuries."""
    if not api_handler:
        raise HTTPException(status_code=500, detail="Data not loaded")
    return api_handler.get_centuries()


@app.get("/api/centuries/{century_id}")
async def get_century(century_id: str):
    """Get specific century by ID."""
    if not api_handler:
        raise HTTPException(status_code=500, detail="Data not loaded")
    century = api_handler.get_century_by_id(century_id)
    if not century:
        raise HTTPException(status_code=404, detail="Century not found")
    return century


@app.get("/api/events")
async def get_events(
    century_id: Optional[str] = Query(None, description="Filter by century ID"),
    year: Optional[int] = Query(None, description="Filter by specific year"),
    year_from: Optional[int] = Query(None, description="Filter by year range start"),
    year_to: Optional[int] = Query(None, description="Filter by year range end"),
    confidence_id: Optional[str] = Query(None, description="Filter by confidence level")
):
    """Get events with optional filters."""
    if not api_handler:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    return api_handler.get_events(
        century_id=century_id,
        year=year,
        year_from=year_from,
        year_to=year_to,
        confidence_id=confidence_id
    )


@app.get("/api/events/{event_id}")
async def get_event(event_id: str):
    """Get specific event by ID."""
    if not api_handler:
        raise HTTPException(status_code=500, detail="Data not loaded")
    event = api_handler.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@app.get("/api/sources")
async def get_sources():
    """Get all historical sources."""
    if not api_handler:
        raise HTTPException(status_code=500, detail="Data not loaded")
    return api_handler.get_sources()


@app.get("/api/sources/{source_id}")
async def get_source(source_id: str):
    """Get specific source by ID."""
    if not api_handler:
        raise HTTPException(status_code=500, detail="Data not loaded")
    source = api_handler.get_source_by_id(source_id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    return source


@app.get("/api/confidence")
async def get_confidence_levels():
    """Get all confidence levels."""
    if not api_handler:
        raise HTTPException(status_code=500, detail="Data not loaded")
    return api_handler.get_confidence_levels()


@app.get("/api/confidence/{confidence_id}")
async def get_confidence(confidence_id: str):
    """Get specific confidence level by ID."""
    if not api_handler:
        raise HTTPException(status_code=500, detail="Data not loaded")
    confidence = api_handler.get_confidence_by_id(confidence_id)
    if not confidence:
        raise HTTPException(status_code=404, detail="Confidence level not found")
    return confidence
