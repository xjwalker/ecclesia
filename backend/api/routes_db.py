"""
Database-powered route handlers for the API.
Uses SQLAlchemy instead of JSON files.
"""
from typing import Dict, List, Optional, Any
from database.config import db_config
from database.repository import (
    CenturyRepository, 
    EventRepository, 
    SourceRepository, 
    ConfidenceLevelRepository
)


class DatabaseAPIHandler:
    """Handles API logic using database backend."""
    
    def __init__(self):
        """Initialize with database connection."""
        pass
    
    def get_centuries(self) -> List[Dict]:
        """Get all centuries."""
        db = db_config.get_session()
        try:
            centuries = CenturyRepository.get_all(db)
            return [c.to_dict() for c in centuries]
        finally:
            db.close()
    
    def get_century_by_id(self, century_id: str) -> Optional[Dict]:
        """Get a specific century by ID."""
        db = db_config.get_session()
        try:
            century = CenturyRepository.get_by_id(db, century_id)
            return century.to_dict() if century else None
        finally:
            db.close()
    
    def get_events(self, 
                   century_id: Optional[str] = None,
                   year: Optional[int] = None,
                   year_from: Optional[int] = None,
                   year_to: Optional[int] = None,
                   region: Optional[str] = None,
                   event_type: Optional[str] = None,
                   confidence_id: Optional[str] = None,
                   language: str = 'es') -> List[Dict]:
        """Get events with optional filters.
        
        Args:
            language: Language code ('en' or 'es') for content
        """
        db = db_config.get_session()
        try:
            events = EventRepository.filter_events(
                db,
                century_id=century_id,
                year=year,
                year_from=year_from,
                year_to=year_to,
                region=region,
                event_type=event_type,
                confidence_id=confidence_id
            )
            return [e.to_dict(language=language) for e in events]
        finally:
            db.close()
    
    def get_event_by_id(self, event_id: str, language: str = 'es') -> Optional[Dict]:
        """Get a specific event by ID.
        
        Args:
            event_id: Event identifier
            language: Language code ('en' or 'es') for content
        """
        db = db_config.get_session()
        try:
            event = EventRepository.get_by_id(db, event_id)
            return event.to_dict(language=language) if event else None
        finally:
            db.close()
    
    def get_sources(self, language: str = 'es', source_type: Optional[str] = None) -> List[Dict]:
        """Get all sources, optionally filtered by type."""
        db = db_config.get_session()
        try:
            if source_type:
                sources = SourceRepository.get_by_type(db, source_type)
            else:
                sources = SourceRepository.get_all(db)
            return [s.to_dict(language=language) for s in sources]
        finally:
            db.close()
    
    def get_source_by_id(self, source_id: str, language: str = 'es') -> Optional[Dict]:
        """Get a specific source by ID."""
        db = db_config.get_session()
        try:
            source = SourceRepository.get_by_id(db, source_id)
            return source.to_dict(language=language) if source else None
        finally:
            db.close()
    
    def get_confidence_levels(self) -> List[Dict]:
        """Get all confidence levels."""
        db = db_config.get_session()
        try:
            levels = ConfidenceLevelRepository.get_all(db)
            return [l.to_dict() for l in levels]
        finally:
            db.close()
    
    def get_confidence_by_id(self, confidence_id: str) -> Optional[Dict]:
        """Get a specific confidence level by ID."""
        db = db_config.get_session()
        try:
            level = ConfidenceLevelRepository.get_by_id(db, confidence_id)
            return level.to_dict() if level else None
        finally:
            db.close()
    
    def get_summary(self) -> Dict[str, Any]:
        """Get data summary statistics."""
        db = db_config.get_session()
        try:
            return {
                "total_centuries": len(CenturyRepository.get_all(db)),
                "total_events": len(EventRepository.get_all(db)),
                "total_sources": len(SourceRepository.get_all(db)),
                "confidence_levels": len(ConfidenceLevelRepository.get_all(db)),
                "data_source": "database",
                "database_url": db_config.database_url.split('@')[-1] if '@' in db_config.database_url else db_config.database_url
            }
        finally:
            db.close()
