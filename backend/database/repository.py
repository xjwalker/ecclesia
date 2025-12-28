"""
Repository layer for database operations.
Provides clean abstraction over SQLAlchemy queries.
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from database.models import Century, Event, Source, ConfidenceLevel


class CenturyRepository:
    """Repository for Century operations."""
    
    @staticmethod
    def get_all(db: Session) -> List[Century]:
        """Get all centuries."""
        return db.query(Century).all()
    
    @staticmethod
    def get_by_id(db: Session, century_id: str) -> Optional[Century]:
        """Get century by ID."""
        return db.query(Century).filter(Century.id == century_id).first()
    
    @staticmethod
    def create(db: Session, century_data: Dict) -> Century:
        """Create a new century."""
        century = Century(**century_data)
        db.add(century)
        db.commit()
        db.refresh(century)
        return century


class EventRepository:
    """Repository for Event operations."""
    
    @staticmethod
    def get_all(db: Session) -> List[Event]:
        """Get all events."""
        return db.query(Event).order_by(Event.year).all()
    
    @staticmethod
    def get_by_id(db: Session, event_id: str) -> Optional[Event]:
        """Get event by ID."""
        return db.query(Event).filter(Event.id == event_id).first()
    
    @staticmethod
    def filter_events(
        db: Session,
        century_id: Optional[str] = None,
        year: Optional[int] = None,
        year_from: Optional[int] = None,
        year_to: Optional[int] = None,
        region: Optional[str] = None,
        event_type: Optional[str] = None,
        confidence_id: Optional[str] = None
    ) -> List[Event]:
        """Filter events by multiple criteria."""
        query = db.query(Event)
        
        if century_id:
            query = query.filter(Event.century_id == century_id)
        if year:
            query = query.filter(Event.year == year)
        if year_from:
            query = query.filter(Event.year >= year_from)
        if year_to:
            query = query.filter(Event.year <= year_to)
        if region:
            query = query.filter(Event.region == region)
        if event_type:
            query = query.filter(Event.event_type == event_type)
        if confidence_id:
            query = query.filter(Event.confidence_id == confidence_id)
        
        return query.order_by(Event.year).all()
    
    @staticmethod
    def get_by_century(db: Session, century_id: str) -> List[Event]:
        """Get all events in a century."""
        return db.query(Event).filter(Event.century_id == century_id).order_by(Event.year).all()
    
    @staticmethod
    def create(db: Session, event_data: Dict) -> Event:
        """Create a new event."""
        event = Event(**event_data)
        db.add(event)
        db.commit()
        db.refresh(event)
        return event


class SourceRepository:
    """Repository for Source operations."""
    
    @staticmethod
    def get_all(db: Session) -> List[Source]:
        """Get all sources."""
        return db.query(Source).all()
    
    @staticmethod
    def get_by_id(db: Session, source_id: str) -> Optional[Source]:
        """Get source by ID."""
        return db.query(Source).filter(Source.id == source_id).first()
    
    @staticmethod
    def get_by_type(db: Session, source_type: str) -> List[Source]:
        """Get sources by type (primary, secondary, scholarly)."""
        return db.query(Source).filter(Source.type == source_type).all()
    
    @staticmethod
    def create(db: Session, source_data: Dict) -> Source:
        """Create a new source."""
        source = Source(**source_data)
        db.add(source)
        db.commit()
        db.refresh(source)
        return source


class ConfidenceLevelRepository:
    """Repository for ConfidenceLevel operations."""
    
    @staticmethod
    def get_all(db: Session) -> List[ConfidenceLevel]:
        """Get all confidence levels."""
        return db.query(ConfidenceLevel).all()
    
    @staticmethod
    def get_by_id(db: Session, confidence_id: str) -> Optional[ConfidenceLevel]:
        """Get confidence level by ID."""
        return db.query(ConfidenceLevel).filter(ConfidenceLevel.id == confidence_id).first()
    
    @staticmethod
    def create(db: Session, confidence_data: Dict) -> ConfidenceLevel:
        """Create a new confidence level."""
        confidence = ConfidenceLevel(**confidence_data)
        db.add(confidence)
        db.commit()
        db.refresh(confidence)
        return confidence


class TimelineRepository:
    """Unified repository for all timeline operations."""
    
    def __init__(self, db: Session):
        self.db = db
        
    def get_summary(self) -> Dict[str, Any]:
        """Get summary statistics."""
        return {
            "total_events": self.db.query(Event).count(),
            "total_sources": self.db.query(Source).count(),
            "total_centuries": self.db.query(Century).count(),
            "total_confidence_levels": self.db.query(ConfidenceLevel).count()
        }
    
    def get_events(self, year_from: Optional[int] = None, year_to: Optional[int] = None,
                   confidence_id: Optional[str] = None, region: Optional[str] = None,
                   event_type: Optional[str] = None, language: str = 'es') -> List[Dict]:
        """Get events with filters.
        
        Args:
            language: Language code ('en' or 'es') for content
        """
        events = EventRepository.filter_events(
            self.db, year_from=year_from, year_to=year_to, 
            confidence_id=confidence_id, region=region, event_type=event_type
        )
        return [e.to_dict(language=language) for e in events]
    
    def get_event_by_id(self, event_id: str, language: str = 'es') -> Optional[Dict]:
        """Get event by ID.
        
        Args:
            event_id: Event identifier
            language: Language code ('en' or 'es') for content
        """
        event = EventRepository.get_by_id(self.db, event_id)
        return event.to_dict(language=language) if event else None
    
    def get_sources(self) -> List[Dict]:
        """Get all sources."""
        sources = SourceRepository.get_all(self.db)
        return [s.to_dict() for s in sources]
    
    def get_source_by_id(self, source_id: str) -> Optional[Dict]:
        """Get source by ID."""
        source = SourceRepository.get_by_id(self.db, source_id)
        return source.to_dict() if source else None
    
    def get_centuries(self) -> List[Dict]:
        """Get all centuries."""
        centuries = CenturyRepository.get_all(self.db)
        return [c.to_dict() for c in centuries]
    
    def get_century_by_id(self, century_id: str) -> Optional[Dict]:
        """Get century by ID."""
        century = CenturyRepository.get_by_id(self.db, century_id)
        return century.to_dict() if century else None
    
    def get_confidence_levels(self) -> List[Dict]:
        """Get all confidence levels."""
        levels = ConfidenceLevelRepository.get_all(self.db)
        return [l.to_dict() for l in levels]
    
    def get_confidence_by_id(self, confidence_id: str) -> Optional[Dict]:
        """Get confidence level by ID."""
        level = ConfidenceLevelRepository.get_by_id(self.db, confidence_id)
        return level.to_dict() if level else None
