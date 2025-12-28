"""
Tests for data loading and validation services.
"""
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from services.data_loader import DataLoader
from services.data_validator import DataValidator


class TestDataLoader:
    """Test DataLoader service."""
    
    def test_load_data_success(self):
        """Test successful data loading."""
        data_dir = "../archives/christianity_century_1"
        data = DataLoader.load_data(data_dir)
        
        assert "centuries" in data
        assert "events" in data
        assert "sources" in data
        assert "confidence_model" in data
        
        assert len(data["centuries"]) > 0
        assert len(data["events"]) > 0
    
    def test_load_data_missing_directory(self):
        """Test loading from non-existent directory."""
        with pytest.raises(FileNotFoundError):
            DataLoader.load_data("./nonexistent")


class TestDataValidator:
    """Test DataValidator service."""
    
    def test_validate_success(self):
        """Test validation of loaded data."""
        data_dir = "../archives/christianity_century_1"
        data = DataLoader.load_data(data_dir)
        
        assert DataValidator.validate(data) == True
    
    def test_validate_empty_data(self):
        """Test validation with empty data."""
        result = DataValidator.validate({})
        # Should handle empty data gracefully
        assert isinstance(result, bool)
