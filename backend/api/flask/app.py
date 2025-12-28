"""
Flask API implementation for Ecclesia Timeline.
Run with: python app.py
"""
import sys
from pathlib import Path

# Add parent directory to path to import from backend
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from flask import Flask, jsonify, request
from flask_cors import CORS
from database.config import DatabaseConfig
from database.repository import TimelineRepository

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Initialize database
db_config = DatabaseConfig()
repository = TimelineRepository(db_config.Session())

print("✓ Database connection established")
print(f"  Using database: {db_config.database_url}")


@app.route('/')
def index():
    """API root endpoint."""
    return jsonify({
        "name": "Ecclesia Timeline API",
        "version": "1.0",
        "framework": "Flask",
        "status": "running",
        "endpoints": {
            "summary": "/api/summary",
            "centuries": "/api/centuries",
            "events": "/api/events",
            "sources": "/api/sources",
            "confidence": "/api/confidence"
        }
    })


@app.route('/api/summary')
def get_summary():
    """Get data summary."""
    try:
        summary = repository.get_summary()
        return jsonify(summary)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/centuries')
def get_centuries():
    """Get all centuries."""
    try:
        centuries = repository.get_centuries()
        return jsonify({"data": centuries, "count": len(centuries)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/centuries/<century_id>')
def get_century(century_id):
    """Get specific century."""
    try:
        century = repository.get_century_by_id(century_id)
        if century:
            return jsonify(century)
        return jsonify({"error": "Century not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/events')
def get_events():
    """Get events with optional filters."""
    try:
        # Parse query parameters
        year_from = request.args.get('year_from', type=int)
        year_to = request.args.get('year_to', type=int)
        confidence_id = request.args.get('confidence_id')
        region = request.args.get('region')
        event_type = request.args.get('event_type')
        language = request.args.get('lang', 'es')  # Default to Spanish
        
        # Get filtered events
        events = repository.get_events(
            year_from=year_from,
            year_to=year_to,
            confidence_id=confidence_id,
            region=region,
            event_type=event_type,
            language=language
        )
        
        return jsonify({"data": events, "count": len(events)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/events/<event_id>')
def get_event(event_id):
    """Get specific event."""
    try:
        language = request.args.get('lang', 'es')  # Default to Spanish
        event = repository.get_event_by_id(event_id, language=language)
        if event:
            return jsonify(event)
        return jsonify({"error": "Event not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sources')
def get_sources():
    """Get all sources."""
    try:
        sources = repository.get_sources()
        return jsonify({"data": sources, "count": len(sources)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sources/<source_id>')
def get_source(source_id):
    """Get specific source."""
    try:
        source = repository.get_source_by_id(source_id)
        if source:
            return jsonify(source)
        return jsonify({"error": "Source not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/confidence')
def get_confidence_levels():
    """Get all confidence levels."""
    try:
        confidence_levels = repository.get_confidence_levels()
        return jsonify({"data": confidence_levels, "count": len(confidence_levels)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/confidence/<confidence_id>')
def get_confidence(confidence_id):
    """Get specific confidence level."""
    try:
        confidence = repository.get_confidence_by_id(confidence_id)
        if confidence:
            return jsonify(confidence)
        return jsonify({"error": "Confidence level not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Ecclesia Timeline API (Flask)")
    print("=" * 50)
    print("API running on: http://localhost:5000")
    print("API docs: See api/flask/README.md")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
