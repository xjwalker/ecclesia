import React, { useState, useEffect } from 'react';
import { useLanguage } from './i18n/LanguageContext';
import { useTimelineData } from './hooks/useTimelineData';
import Timeline from './components/Timeline';
import Filters from './components/Filters';
import EventSidebar from './components/EventSidebar';
import CenturyNavigation from './components/CenturyNavigation';
import apiService from './services/api';
import './App.css';

function App() {
  const { t, language, changeLanguage } = useLanguage();
  const { 
    events, 
    summary, 
    loading, 
    error, 
    filters, 
    setFilters, 
    applyFilters, 
    clearFilters,
    reload 
  } = useTimelineData(language);
  
  const [selectedEvent, setSelectedEvent] = useState(null);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [timelineOrientation, setTimelineOrientation] = useState('vertical');
  const [sidebarWidth, setSidebarWidth] = useState(450);
  const [isDragging, setIsDragging] = useState(false);
  const [centuries, setCenturies] = useState([]);
  const [activeCentury, setActiveCentury] = useState(null);

  const handleEventClick = (event) => {
    setSelectedEvent(event);
    setSidebarOpen(true);
  };

  const handleCloseSidebar = () => {
    setSidebarOpen(false);
    setTimeout(() => setSelectedEvent(null), 300);
  };

  const handleCenturyClick = (centuryId) => {
    setActiveCentury(centuryId);
    const element = document.getElementById(`century-${centuryId}`);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  // Load centuries
  useEffect(() => {
    const loadCenturies = async () => {
      try {
        const response = await apiService.getCenturies();
        // Handle different response structures
        const centuriesData = response.data?.centuries || response.data || [];
        console.log('Centuries loaded:', centuriesData);
        setCenturies(Array.isArray(centuriesData) ? centuriesData : []);
      } catch (err) {
        console.error('Failed to load centuries:', err);
        setCenturies([]);
      }
    };
    loadCenturies();
  }, []);

  const handleMouseDown = (e) => {
    if (timelineOrientation === 'vertical') {
      setIsDragging(true);
      e.preventDefault();
    }
  };

  const handleMouseMove = (e) => {
    if (isDragging && timelineOrientation === 'vertical') {
      const newWidth = window.innerWidth - e.clientX;
      const maxWidth = Math.floor(window.innerWidth * 0.6); // Up to 60% of screen
      if (newWidth >= 300 && newWidth <= maxWidth) {
        setSidebarWidth(newWidth);
      }
    }
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  React.useEffect(() => {
    if (isDragging) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
      return () => {
        document.removeEventListener('mousemove', handleMouseMove);
        document.removeEventListener('mouseup', handleMouseUp);
      };
    }
  }, [isDragging]);

  return (
    <div className="App">
      <header className="app-header">
        <div className="header-content">
          <div className="header-top">
            <h1>{t.appTitle}</h1>
            <div className="header-controls">
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
              <div className="view-switcher">
                <button 
                  className={`view-btn ${timelineOrientation === 'vertical' ? 'active' : ''}`}
                  onClick={() => setTimelineOrientation('vertical')}
                  title="Vertical timeline"
                >
                  ⬍
                </button>
                <button 
                  className={`view-btn ${timelineOrientation === 'horizontal' ? 'active' : ''}`}
                  onClick={() => setTimelineOrientation('horizontal')}
                  title="Horizontal timeline"
                >
                  ⬌
                </button>
              </div>
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

      <CenturyNavigation 
        centuries={centuries}
        onCenturyClick={handleCenturyClick}
        activeCentury={activeCentury}
      />

      <Filters
        filters={filters}
        onChange={setFilters}
        onApply={() => applyFilters(filters)}
        onClear={clearFilters}
        translations={t}
      />

      <div className={`main-content ${timelineOrientation}`}>
        <main className={`timeline-container ${timelineOrientation}`}>
          <Timeline
            events={events}
            onEventClick={handleEventClick}
            loading={loading}
            error={error}
            orientation={timelineOrientation}
          />
        </main>

        {timelineOrientation === 'vertical' && sidebarOpen && (
          <div 
            className="resize-divider"
            onMouseDown={handleMouseDown}
          >
            <div className="resize-handle"></div>
          </div>
        )}

        <EventSidebar
          event={selectedEvent}
          isOpen={sidebarOpen}
          onClose={handleCloseSidebar}
          orientation={timelineOrientation}
          width={sidebarWidth}
        />
      </div>

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
