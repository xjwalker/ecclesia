# Ecclesia Timeline - Frontend

React application for visualizing the historical Christianity timeline.

## Features

- 📜 **Scrolling Timeline**: Beautiful vertical timeline with alternating events
- 🎨 **Confidence Visualization**: Color-coded confidence levels (High/Medium/Low)
- 🔍 **Filtering**: Filter events by year range and confidence level
- 📱 **Responsive Design**: Works on desktop and mobile
- 🌐 **API Integration**: Consumes backend REST API
- ⚙️ **Environment Config**: Uses `.env` for API configuration

## Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure API Endpoint

Edit `.env` file:
```bash
REACT_APP_API_URL=http://localhost:5000
```

### 3. Start Development Server

```bash
npm start
```

App runs on **http://localhost:3000**

## Environment Variables

- `REACT_APP_API_URL` - Backend API URL (default: http://localhost:5000)

### Environment Files

- `.env` - Default configuration
- `.env.development` - Development settings (localhost)
- `.env.production` - Production settings (deployed API)

## Running with Backend

### Option 1: Flask Backend
```bash
# Terminal 1 - Backend
cd backend
python api/flask/app.py

# Terminal 2 - Frontend
cd frontend
npm start
```

### Option 2: FastAPI Backend
```bash
# Terminal 1 - Backend
cd backend
uvicorn api.fastapi.app:app --reload

# Terminal 2 - Frontend (update .env)
cd frontend
# Edit .env: REACT_APP_API_URL=http://localhost:8000
npm start
```

## Build for Production

```bash
npm run build
```

Creates optimized production build in `build/` folder.

## Project Structure

```
frontend/
├── public/
│   └── index.html          # HTML template
├── src/
│   ├── components/
│   │   ├── TimelineEvent.js    # Event card component
│   │   └── TimelineEvent.css   # Event styling
│   ├── services/
│   │   └── api.js              # API service
│   ├── App.js                  # Main app component
│   ├── App.css                 # App styling
│   ├── index.js                # Entry point
│   └── index.css               # Global styles
├── .env                        # Environment config
├── .env.development            # Dev config
├── .env.production             # Prod config
└── package.json                # Dependencies

```

## Features Details

### Timeline Visualization
- Vertical scrolling timeline with center line
- Alternating left/right event cards
- Smooth animations and hover effects
- Color-coded confidence badges

### Filtering
- Filter by year range (from/to)
- Filter by confidence level (C1/C2/C3)
- Clear filters to reset view

### Responsive Design
- Desktop: Side-by-side event layout
- Mobile: Stacked vertical layout
- Touch-friendly interface

## API Integration

The app consumes these endpoints:

- `GET /api/summary` - Overview statistics
- `GET /api/events` - All events
- `GET /api/events?year_from=X&year_to=Y` - Filtered events
- `GET /api/events?confidence_id=C1` - Events by confidence

## Customization

### Colors

Edit confidence colors in `TimelineEvent.js`:
```javascript
const confidenceColors = {
  C1: '#4CAF50',  // High - Green
  C2: '#FFC107',  // Medium - Amber
  C3: '#FF9800',  // Low - Orange
};
```

### Styling

- `App.css` - Main layout and timeline
- `TimelineEvent.css` - Event card styling
- `index.css` - Global styles

## Deployment

### Vercel/Netlify
```bash
npm run build
# Deploy build/ folder
```

### Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]
```

## Troubleshooting

**API Connection Error:**
- Check backend is running
- Verify `REACT_APP_API_URL` in `.env`
- Check CORS is enabled in backend

**No Events Showing:**
- Check backend has data (run `python -m database.seed`)
- Check API endpoint returns data
- Check browser console for errors
