"""
Flask API implementation for Ecclesia Timeline.
Run with: python api/flask_app.py
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from api.routes import APIHandler

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Initialize API handler with data
DATA_DIR = "../archives/christianity_century_1"
try:
    api_handler = APIHandler(DATA_DIR)
    print("✓ Data loaded successfully")
except Exception as e:
    print(f"✗ Error loading data: {e}")
    api_handler = None


@app.route('/')
def index():
    """API root endpoint."""
    return jsonify({
        "name": "Ecclesia Timeline API",
        "version": "1.0",
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
    if not api_handler:
        return jsonify({"error": "Data not loaded"}), 500
    return jsonify(api_handler.get_summary())


@app.route('/api/centuries')
def get_centuries():
    """Get all centuries."""
    if not api_handler:
        return jsonify({"error": "Data not loaded"}), 500
    return jsonify(api_handler.get_centuries())


@app.route('/api/centuries/<century_id>')
def get_century(century_id):
    """Get specific century."""
    if not api_handler:
        return jsonify({"error": "Data not loaded"}), 500
    century = api_handler.get_century_by_id(century_id)
    if century:
        return jsonify(century)
    return jsonify({"error": "Century not found"}), 404


@app.route('/api/events')
def get_events():
    """Get events with optional filters."""
    if not api_handler:
        return jsonify({"error": "Data not loaded"}), 500
    
    # Parse query parameters
    century_id = request.args.get('century_id')
    year = request.args.get('year', type=int)
    year_from = request.args.get('year_from', type=int)
    year_to = request.args.get('year_to', type=int)
    confidence_id = request.args.get('confidence_id')
    
    events = api_handler.get_events(
        century_id=century_id,
        year=year,
        year_from=year_from,
        year_to=year_to,
        confidence_id=confidence_id
    )
    return jsonify(events)


@app.route('/api/events/<event_id>')
def get_event(event_id):
    """Get specific event."""
    if not api_handler:
        return jsonify({"error": "Data not loaded"}), 500
    event = api_handler.get_event_by_id(event_id)
    if event:
        return jsonify(event)
    return jsonify({"error": "Event not found"}), 404


@app.route('/api/sources')
def get_sources():
    """Get all sources."""
    if not api_handler:
        return jsonify({"error": "Data not loaded"}), 500
    language = request.args.get('lang', 'es')
    return jsonify(api_handler.get_sources(language))


@app.route('/api/sources/<source_id>')
def get_source(source_id):
    """Get specific source."""
    if not api_handler:
        return jsonify({"error": "Data not loaded"}), 500
    language = request.args.get('lang', 'es')
    source = api_handler.get_source_by_id(source_id, language)
    if source:
        return jsonify(source)
    return jsonify({"error": "Source not found"}), 404


@app.route('/api/confidence')
def get_confidence_levels():
    """Get all confidence levels."""
    if not api_handler:
        return jsonify({"error": "Data not loaded"}), 500
    return jsonify(api_handler.get_confidence_levels())


@app.route('/api/confidence/<confidence_id>')
def get_confidence(confidence_id):
    """Get specific confidence level."""
    if not api_handler:
        return jsonify({"error": "Data not loaded"}), 500
    confidence = api_handler.get_confidence_by_id(confidence_id)
    if confidence:
        return jsonify(confidence)
    return jsonify({"error": "Confidence level not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
