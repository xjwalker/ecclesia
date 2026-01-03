"""
Database configuration and connection management.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Base class for all models
Base = declarative_base()

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "sqlite:///ecclesia_timeline.db"  # Default to SQLite
)

# For PostgreSQL, use: postgresql://user:password@localhost/ecclesia_timeline
# For MySQL, use: mysql+pymysql://user:password@localhost/ecclesia_timeline

class DatabaseConfig:
    """Database configuration and session management."""
    
    def __init__(self, database_url: str = None):
        self.database_url = database_url or DATABASE_URL
        
        # Create engine with appropriate settings
        if self.database_url.startswith('sqlite'):
            # SQLite specific settings
            self.engine = create_engine(
                self.database_url,
                connect_args={"check_same_thread": False},
                echo=False  # Set to True for SQL debugging
            )
        else:
            # PostgreSQL/MySQL settings
            self.engine = create_engine(
                self.database_url,
                pool_size=10,
                max_overflow=20,
                echo=False
            )
        
        # Create session factory
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )
        
        # Thread-safe session
        self.Session = scoped_session(self.SessionLocal)
    
    def create_tables(self):
        """Create all tables in the database."""
        Base.metadata.create_all(bind=self.engine)
        print(f"OK Database tables created using: {self.database_url}")
    
    def drop_tables(self):
        """Drop all tables (use with caution!)."""
        Base.metadata.drop_all(bind=self.engine)
        print("OK All tables dropped")
    
    def get_session(self):
        """Get a new database session."""
        return self.Session()
    
    def close_session(self):
        """Close the scoped session."""
        self.Session.remove()


# Global database instance
db_config = DatabaseConfig()


def get_db():
    """
    Dependency injection helper for FastAPI/Flask.
    Yields a database session and ensures it's closed.
    """
    db = db_config.get_session()
    try:
        yield db
    finally:
        db.close()
