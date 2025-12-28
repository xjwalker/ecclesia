import React from 'react';
import { useLanguage } from '../i18n/LanguageContext';
import './TimelineEvent.css';

const TimelineEvent = ({ event, isLeft, onClick }) => {
  const { t } = useLanguage();
  
  const confidenceColors = {
    C1: '#4CAF50',  // High - Green
    C2: '#FFC107',  // Medium - Amber
    C3: '#FF9800',  // Low - Orange
  };

  return (
    <div 
      className={`timeline-event ${isLeft ? 'left' : 'right'}`}
      onClick={() => onClick(event)}
    >
      <div className="timeline-content">
        <div 
          className="confidence-badge"
          style={{ backgroundColor: confidenceColors[event.confidence_id] || '#999' }}
        >
          {t.confidence[event.confidence_id] || event.confidence_id}
        </div>
        
        <div className="event-year">{event.year} CE</div>
        <h3 className="event-title">{event.title}</h3>
        
        {event.description && (
          <p className="event-description">{event.description}</p>
        )}
        
        <div className="event-metadata">
          {event.region && (
            <div className="event-meta">
              <span className="meta-icon">📍</span>
              <span className="meta-label">{t.region}:</span> {event.region}
            </div>
          )}
          
          {event.event_type && (
            <div className="event-meta">
              <span className="meta-icon">🏷️</span>
              <span className="meta-label">{t.type}:</span> {event.event_type}
            </div>
          )}
          
          {event.sources && event.sources.length > 0 && (
            <div className="event-meta">
              <span className="meta-icon">📚</span>
              <span className="sources-label">{t.sourcesLabel}:</span>
              <span className="sources-count">{event.sources.length}</span>
            </div>
          )}
        </div>
        
        <div className="click-hint">{t.clickForDetails}</div>
      </div>
    </div>
  );
};

export default TimelineEvent;
