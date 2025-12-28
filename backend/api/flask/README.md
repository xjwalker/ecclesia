# Flask API - Ecclesia Timeline

Simple REST API implementation using Flask.

## Installation

```bash
pip install flask flask-cors
```

## Run the API

From the `backend` directory:

```bash
python api/flask/app.py
```

Or directly:
```bash
cd backend/api/flask
python app.py
```

The API will start on **http://localhost:5000**

## Test the API

Open your browser or use curl:

```bash
# Check API is running
curl http://localhost:5000/

# Get summary
curl http://localhost:5000/api/summary

# Get all events
curl http://localhost:5000/api/events

# Filter events by century
curl http://localhost:5000/api/events?century_id=CENT_01_CE

# Filter events by year range
curl http://localhost:5000/api/events?year_from=30&year_to=70

# Get specific event
curl http://localhost:5000/api/events/EVT_0030_CRUCIFIXION
```

## Deploy Options

### Local Development
```bash
python app.py
```

### Production with Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 "app:app"
```

### Docker
```bash
docker build -t ecclesia-flask .
docker run -p 5000:5000 ecclesia-flask
```

## Environment Variables

- `FLASK_ENV`: Set to `development` or `production`
- `PORT`: Server port (default: 5000)
- `DATA_DIR`: Path to data directory (default: ../archives/christianity_century_1)
