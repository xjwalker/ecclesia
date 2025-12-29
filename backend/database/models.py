"""
SQLAlchemy database models for Ecclesia Timeline.
Maps to the JSON data structure with proper relationships.
"""
from sqlalchemy import Column, String, Integer, Float, JSON, ForeignKey, Table, Text
from sqlalchemy.orm import relationship
from database.config import Base


# Association table for many-to-many relationship between events and sources
event_sources = Table(
    'event_sources',
    Base.metadata,
    Column('event_id', String, ForeignKey('events.id'), primary_key=True),
    Column('source_id', String, ForeignKey('sources.id'), primary_key=True)
)

# Association table for many-to-many relationship between centuries and sources
century_sources = Table(
    'century_sources',
    Base.metadata,
    Column('century_id', String, ForeignKey('centuries.id'), primary_key=True),
    Column('source_id', String, ForeignKey('sources.id'), primary_key=True)
)


class Century(Base):
    """Century model - represents a historical century."""
    __tablename__ = 'centuries'
    
    id = Column(String, primary_key=True)
    century_range = Column(JSON)  # [start, end] as array
    summary = Column(String)
    confidence_id = Column(String, ForeignKey('confidence_levels.id'))
    
    # Relationships
    confidence = relationship("ConfidenceLevel", back_populates="centuries")
    sources = relationship("Source", secondary=century_sources, back_populates="centuries")
    events = relationship("Event", back_populates="century")
    
    def to_dict(self):
        """Convert to dictionary for API responses."""
        return {
            "id": self.id,
            "century_range": self.century_range,
            "summary": self.summary,
            "confidence_id": self.confidence_id,
            "sources": [s.id for s in self.sources] if self.sources else []
        }


class Event(Base):
    """Event model - represents a historical event."""
    __tablename__ = 'events'
    
    id = Column(String, primary_key=True)
    year = Column(Integer, index=True)
    year_approx = Column(String, nullable=True)  # For approximate dates like "~50"
    century_id = Column(String, ForeignKey('centuries.id'), index=True)
    title = Column(JSON)  # {"en": "...", "es": "..."}
    description = Column(JSON, nullable=True)  # {"en": "...", "es": "..."}
    context = Column(JSON, nullable=True)  # {"en": "...", "es": "..."}
    confidence_rationale = Column(JSON, nullable=True)  # {"en": "...", "es": "..."}
    significance = Column(JSON, nullable=True)  # {"en": "...", "es": "..."}
    people_involved = Column(JSON, nullable=True)  # List of key people involved
    image_url = Column(String, nullable=True)  # URL to event image
    region = Column(String, nullable=True, index=True)
    event_type = Column(String, nullable=True, index=True)
    confidence_id = Column(String, ForeignKey('confidence_levels.id'), index=True)
    
    # Relationships
    century = relationship("Century", back_populates="events")
    confidence = relationship("ConfidenceLevel", back_populates="events")
    sources = relationship("Source", secondary=event_sources, back_populates="events")
    
    def to_dict(self, language='es'):
        """Convert to dictionary for API responses.
        
        Args:
            language: Language code ('en' or 'es') to return content in
        """
        def get_text(field):
            """Extract text for specified language from JSON field."""
            if field is None:
                return None
            if isinstance(field, dict):
                return field.get(language, field.get('es', field.get('en', '')))
            return field  # Fallback for non-JSON data
        
        return {
            "id": self.id,
            "year": self.year,
            "year_approx": self.year_approx,
            "century_id": self.century_id,
            "title": get_text(self.title),
            "description": get_text(self.description),
            "context": get_text(self.context),
            "confidence_rationale": get_text(self.confidence_rationale),
            "significance": get_text(self.significance),
            "people_involved": self.people_involved,
            "image_url": self.image_url,
            "region": self.region,
            "event_type": self.event_type,
            "confidence_id": self.confidence_id,
            "sources": [s.id for s in self.sources] if self.sources else []
        }


class Source(Base):
    """Source model - represents a historical source document."""
    __tablename__ = 'sources'
    
    id = Column(String, primary_key=True)
    type = Column(JSON, index=False)  # {"en": "primary", "es": "primaria"}
    author = Column(JSON, nullable=True)  # {"en": "Author Name", "es": "Nombre del Autor"}
    work = Column(JSON)  # {"en": "Work Title", "es": "Título de la Obra"}
    date_written = Column(String, nullable=True)
    language = Column(JSON, nullable=True)  # {"en": "Greek", "es": "Griego"}
    notes = Column(JSON, nullable=True)  # {"en": "Notes", "es": "Notas"}
    citation_info = Column(JSON, nullable=True)  # {"en": "Citation", "es": "Cita"}
    
    # Relationships
    events = relationship("Event", secondary=event_sources, back_populates="sources")
    centuries = relationship("Century", secondary=century_sources, back_populates="sources")
    
    def to_dict(self, language='es'):
        """Convert to dictionary for API responses with language support."""
        def get_text(field):
            """Extract text for the given language from a field."""
            if isinstance(field, dict):
                return field.get(language, field.get('es', ''))
            return field
        
        return {
            "id": self.id,
            "type": get_text(self.type),
            "author": get_text(self.author),
            "work": get_text(self.work),
            "date_written": self.date_written,
            "language": get_text(self.language),
            "notes": get_text(self.notes),
            "citation_info": get_text(self.citation_info)
        }


class ConfidenceLevel(Base):
    """Confidence level model - represents historical confidence ratings."""
    __tablename__ = 'confidence_levels'
    
    id = Column(String, primary_key=True)
    label = Column(String)
    numeric_range = Column(JSON)  # [min, max] as array
    criteria = Column(JSON)  # Array of criteria strings
    description = Column(String, nullable=True)
    
    # Relationships
    events = relationship("Event", back_populates="confidence")
    centuries = relationship("Century", back_populates="confidence")
    
    def to_dict(self):
        """Convert to dictionary for API responses."""
        return {
            "id": self.id,
            "label": self.label,
            "numeric_range": self.numeric_range,
            "criteria": self.criteria,
            "description": self.description
        }
