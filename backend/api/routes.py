"""
Shared route handlers for the API.
Framework-agnostic business logic.
"""
from typing import Dict, List, Optional, Any
from services.data_loader import DataLoader
from services.data_validator import DataValidator


class APIHandler:
    """Handles API logic independent of web framework."""
    
    def __init__(self, data_directory: str):
        self.data = DataLoader.load_data(data_directory)
        if not DataValidator.validate(self.data):
            raise ValueError("Data validation failed")
    
    def get_centuries(self) -> List[Dict]:
        """Get all centuries."""
        return [century.__dict__ for century in self.data.get('centuries', [])]
    
    def get_century_by_id(self, century_id: str) -> Optional[Dict]:
        """Get a specific century by ID."""
        for century in self.data.get('centuries', []):
            if century.id == century_id:
                return century.__dict__
        return None
    
    def get_events(self, 
                   century_id: Optional[str] = None,
                   year: Optional[int] = None,
                   year_from: Optional[int] = None,
                   year_to: Optional[int] = None,
                   confidence_id: Optional[str] = None) -> List[Dict]:
        """
        Get events with optional filters.
        
        Args:
            century_id: Filter by century
            year: Filter by specific year
            year_from: Filter by year range (start)
            year_to: Filter by year range (end)
            confidence_id: Filter by confidence level
        """
        events = self.data.get('events', [])
        filtered = []
        
        for event in events:
            # Apply filters
            if century_id and event.century_id != century_id:
                continue
            if year and event.year != year:
                continue
            if year_from and event.year < year_from:
                continue
            if year_to and event.year > year_to:
                continue
            if confidence_id and event.confidence_id != confidence_id:
                continue
            
            filtered.append(event.__dict__)
        
        return filtered
    
    def get_event_by_id(self, event_id: str) -> Optional[Dict]:
        """Get a specific event by ID."""
        for event in self.data.get('events', []):
            if event.id == event_id:
                return event.__dict__
        return None
    
    def get_sources(self) -> List[Dict]:
        """Get all sources."""
        return [source.__dict__ for source in self.data.get('sources', [])]
    
    def get_source_by_id(self, source_id: str) -> Optional[Dict]:
        """Get a specific source by ID."""
        for source in self.data.get('sources', []):
            if source.id == source_id:
                return source.__dict__
        return None
    
    def get_confidence_levels(self) -> List[Dict]:
        """Get all confidence levels."""
        return [conf.__dict__ for conf in self.data.get('confidence_model', [])]
    
    def get_confidence_by_id(self, confidence_id: str) -> Optional[Dict]:
        """Get a specific confidence level by ID."""
        for conf in self.data.get('confidence_model', []):
            if conf.id == confidence_id:
                return conf.__dict__
        return None
    
    def get_summary(self) -> Dict[str, Any]:
        """Get data summary statistics."""
        return {
            "total_centuries": len(self.data.get('centuries', [])),
            "total_events": len(self.data.get('events', [])),
            "total_sources": len(self.data.get('sources', [])),
            "confidence_levels": len(self.data.get('confidence_model', [])),
            "data_loaded": True
        }
