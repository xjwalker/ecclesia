import React, { useState, useEffect } from 'react';
import { useLanguage } from './i18n/LanguageContext';
import apiService from './services/api';
import TimelineEvent from './components/TimelineEvent';
import EventSidebar from './components/EventSidebar';
import './App.css';

function App() {
  const { t, language, changeLanguage } = useLanguage();
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [summary, setSummary] = useState(null);
  const [selectedEvent, setSelectedEvent] = useState(null);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [filters, setFilters] = useState({
    yearFrom: '',
    yearTo: '',
    confidenceId: '',
  });

  useEffect(() => {
    loadData();
  }, [language]);

  const loadData = async () => {
    try {
      setLoading(true);
      setError(null);

      // Load summary
      const summaryResponse = await apiService.getSummary();
      setSummary(summaryResponse.data);

      // Load events
      const eventsResponse = await apiService.getEvents({}, language);
      // Handle both wrapped and unwrapped data formats
      const eventsData = eventsResponse.data.data || eventsResponse.data;
      setEvents(eventsData);
    } catch (err) {
      setError(t.error);
      console.error('API Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const applyFilters = async () => {
    try {
      setLoading(true);
      const params = {};
      
      if (filters.yearFrom) params.year_from = parseInt(filters.yearFrom);
      if (filters.yearTo) params.year_to = parseInt(filters.yearTo);
      if (filters.confidenceId) params.confidence_id = filters.confidenceId;

      const response = await apiService.getEvents(params, language);
      // Handle both wrapped and unwrapped data formats
      const eventsData = response.data.data || response.data;
      setEvents(eventsData);
    } catch (err) {
      setError('Error filtering events');
      console.error('Filter Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const clearFilters = () => {
    setFilters({ yearFrom: '', yearTo: '', confidenceId: '' });
    loadData();
  };

  const handleEventClick = (event) => {
    setSelectedEvent(event);
    setSidebarOpen(true);
  };

  const handleCloseSidebar = () => {
    setSidebarOpen(false);
    setTimeout(() => setSelectedEvent(null), 300);
  };

  return (
    <div className="App">
      <header className="app-header">
        <div className="header-content">
          <div className="header-top">
            <h1>{t.appTitle}</h1>
            <div className="language-switcher">
              <button 
                className={`lang-btn ${language === 'en' ? 'active' : ''}`}
                onClick={() => changeLanguage('en')}
              >
                EN
              </button>
              <button 
                className={`lang-btn ${language === 'es' ? 'active' : ''}`}
                onClick={() => changeLanguage('es')}
              >
                ES
              </button>
            </div>
          </div>
          <p className="subtitle">{t.subtitle}</p>
          {summary && (
            <div className="summary-stats">
              <span className="stat">{summary.total_events} {t.events}</span>
              <span className="stat-separator">•</span>
              <span className="stat">{summary.total_sources} {t.sources}</span>
              <span className="stat-separator">•</span>
              <span className="stat">{summary.total_centuries} {t.centuries}</span>
            </div>
          )}
        </div>
      </header>

      <div className="filters-section">
        <div className="filters-container">
          <input
            type="number"
            placeholder={t.yearFrom}
            value={filters.yearFrom}
            onChange={(e) => setFilters({ ...filters, yearFrom: e.target.value })}
            className="filter-input"
          />
          <input
            type="number"
            placeholder={t.yearTo}
            value={filters.yearTo}
            onChange={(e) => setFilters({ ...filters, yearTo: e.target.value })}
            className="filter-input"
          />
          <select
            value={filters.confidenceId}
            onChange={(e) => setFilters({ ...filters, confidenceId: e.target.value })}
            className="filter-select"
          >
            <option value="">{t.allConfidenceLevels}</option>
            <option value="C1">{t.highConfidence}</option>
            <option value="C2">{t.mediumConfidence}</option>
            <option value="C3">{t.lowConfidence}</option>
          </select>
          <button onClick={applyFilters} className="filter-button apply">
            {t.applyFilters}
          </button>
          <button onClick={clearFilters} className="filter-button clear">
            {t.clear}
          </button>
        </div>
      </div>

      <main className="timeline-container">
        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>{t.loading}</p>
          </div>
        )}

        {error && (
          <div className="error">
            <p>{error}</p>
            <button onClick={loadData} className="retry-button">{t.retry}</button>
          </div>
        )}

        {!loading && !error && events.length === 0 && (
          <div className="no-data">
            <p>{t.noEvents}</p>
          </div>
        )}

        {!loading && !error && events.length > 0 && (
          <div className="timeline">
            <div className="timeline-line"></div>
            {events.map((event, index) => (
              <TimelineEvent
                key={event.id}
                event={event}
                isLeft={index % 2 === 0}
                onClick={handleEventClick}
              />
            ))}
          </div>
        )}
      </main>

      <EventSidebar
        event={selectedEvent}
        isOpen={sidebarOpen}
        onClose={handleCloseSidebar}
      />

      <footer className="app-footer">
        <p>{t.footerText}</p>
        <p className="footer-note">
          {t.apiLabel}: {process.env.REACT_APP_API_URL || 'http://localhost:5000'}
        </p>
      </footer>
    </div>
  );
}

export default App;
