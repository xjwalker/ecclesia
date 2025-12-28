import React, { useState, useEffect } from 'react';
import { useLanguage } from '../i18n/LanguageContext';
import apiService from '../services/api';
import './EventSidebar.css';

const EventSidebar = ({ event, isOpen, onClose }) => {
  const { t, language } = useLanguage();
  const [sources, setSources] = useState([]);
  const [confidence, setConfidence] = useState(null);
  const [century, setCentury] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (event && isOpen) {
      loadEventDetails();
    }
  }, [event, isOpen, language]);

  const loadEventDetails = async () => {
    if (!event) return;
    
    setLoading(true);
    try {
      // Load sources
      if (event.sources && event.sources.length > 0) {
        const sourcePromises = event.sources.map(sourceId =>
          apiService.getSource(sourceId, language).catch(() => null)
        );
        const sourceResults = await Promise.all(sourcePromises);
        setSources(sourceResults.filter(s => s).map(s => s.data));
      }

      // Load confidence level
      if (event.confidence_id) {
        const confResponse = await apiService.getConfidenceLevel(event.confidence_id);
        setConfidence(confResponse.data);
      }

      // Load century
      if (event.century_id) {
        const centuryResponse = await apiService.getCentury(event.century_id);
        setCentury(centuryResponse.data);
      }
    } catch (error) {
      console.error('Error loading event details:', error);
    } finally {
      setLoading(false);
    }
  };

  if (!event) return null;

  // Helper function to format text with paragraphs and bullet points
  const formatText = (text) => {
    if (!text) return null;
    
    // Split by numbered points that come after punctuation/space: ": 1)" or ", 2)"
    // This avoids matching parenthetical numbers like (C2)
    const parts = text.split(/(\s+\d+\))/);
    
    return (
      <div className="formatted-paragraphs">
        {parts.map((part, idx) => {
          const trimmed = part.trim();
          if (!trimmed) return null;
          
          // Check if this part is a numbered marker like " 1)" or " 2)"
          const numberMatch = trimmed.match(/^(\d+\))$/);
          if (numberMatch && idx + 1 < parts.length) {
            // This is a number marker, combine it with the next part (the actual text)
            const nextPart = parts[idx + 1];
            if (nextPart) {
              return (
                <div key={idx} className="bullet-point">
                  <span className="bullet-number">{numberMatch[1]}</span>
                  <span className="bullet-text">{nextPart.trim()}</span>
                </div>
              );
            }
          }
          
          // Skip if this was already rendered as part of a bullet point
          if (idx > 0 && parts[idx - 1].trim().match(/^\d+\)$/)) {
            return null;
          }
          
          // Regular paragraph
          return <p key={idx} className="formatted-paragraph">{trimmed}</p>;
        })}
      </div>
    );
  };


  const confidenceColors = {
    C1: '#4CAF50',
    C2: '#FFC107',
    C3: '#FF9800',
  };

  const confidenceLabels = {
    C1: 'Alta',
    C2: 'Media',
    C3: 'Baja',
  };

  return (
    <>
      <div className={`sidebar-overlay ${isOpen ? 'open' : ''}`} onClick={onClose} />
      <div className={`event-sidebar ${isOpen ? 'open' : ''}`}>
        <div className="sidebar-header">
          <button className="close-button" onClick={onClose}>✕</button>
          <h2>{t.eventDetails}</h2>
        </div>

        <div className="sidebar-content">
          {/* Main Event Info */}
          <div className="detail-section">
            <div className="event-year-large">{event.year} CE</div>
            <h3 className="event-title-large">{event.title}</h3>
            
            <div 
              className="confidence-badge-large"
              style={{ backgroundColor: confidenceColors[event.confidence_id] || '#999' }}
            >
              {t.reliability}: {t.confidence[event.confidence_id] || event.confidence_id}
            </div>
          </div>

          {/* Description */}
          {event.description && (
            <div className="detail-section">
              <h4 className="section-title">📝 {t.description}</h4>
              <p className="event-description-full">{event.description}</p>
              
              {/* Event Image - right under description */}
              {event.image_url && (
                <div className="event-image-container">
                  <img src={event.image_url} alt={event.title} className="event-image" onError={(e) => e.target.style.display = 'none'} />
                </div>
              )}
            </div>
          )}

          {/* People Involved */}
          {event.people_involved && event.people_involved.length > 0 && (
            <div className="detail-section">
              <h4 className="section-title">👥 {t.peopleInvolved}</h4>
              <div className="people-list">
                {event.people_involved.map((person, index) => {
                  const name = person.name_es && person.name_en 
                    ? (language === 'es' ? person.name_es : person.name_en)
                    : person.name; // Fallback for old format
                  const role = person.role_es && person.role_en 
                    ? (language === 'es' ? person.role_es : person.role_en)
                    : person.role; // Fallback for old format
                  return (
                    <div key={index} className="person-item">
                      <span className="person-name">{name}</span>
                      <span className="person-role">• {role}</span>
                    </div>
                  );
                })}
              </div>
            </div>
          )}

          {/* Historical Context - What Happened */}
          {event.context && (
            <div className="detail-section">
              <h4 className="section-title">📖 {t.whatHappened}</h4>
              <div className="formatted-text">{formatText(event.context)}</div>
            </div>
          )}

          {/* Confidence Rationale - Why This Confidence Level */}
          {event.confidence_rationale && (
            <div className="detail-section confidence-rationale-section">
              <h4 className="section-title">🔍 {t.whyConfidence}</h4>
              <div className="formatted-text confidence-text">{formatText(event.confidence_rationale)}</div>
            </div>
          )}

          {/* Significance */}
          {event.significance && (
            <div className="detail-section">
              <h4 className="section-title">⭐ {t.historicalSignificance}</h4>
              <div className="formatted-text">{formatText(event.significance)}</div>
            </div>
          )}

          {/* Metadata */}
          <div className="detail-section">
            <h4 className="section-title">ℹ️ {t.information}</h4>
            <div className="info-grid">
              {event.region && (
                <div className="info-item">
                  <span className="info-label">{t.region}:</span>
                  <span className="info-value">{event.region}</span>
                </div>
              )}
              {event.event_type && (
                <div className="info-item">
                  <span className="info-label">{t.type}:</span>
                  <span className="info-value">{event.event_type}</span>
                </div>
              )}
              {event.century_id && (
                <div className="info-item">
                  <span className="info-label">{t.century}:</span>
                  <span className="info-value">{event.century_id}</span>
                </div>
              )}
              <div className="info-item">
                <span className="info-label">{t.id}:</span>
                <span className="info-value info-code">{event.id}</span>
              </div>
            </div>
          </div>

          {/* Century Info */}
          {century && century.century_range && (
            <div className="detail-section">
              <h4 className="section-title">📅 {t.centuryContext}</h4>
              <div className="century-info">
                <p className="century-range">
                  {t.years} {century.century_range[0]} - {century.century_range[1]}
                </p>
                {century.summary && <p className="century-summary">{century.summary}</p>}
              </div>
            </div>
          )}

          {/* Confidence Details */}
          {confidence && (
            <div className="detail-section">
              <h4 className="section-title">🎯 {t.confidenceLevel}</h4>
              <div className="confidence-details">
                <div className="confidence-info">
                  <span className="confidence-label">{confidence.label || confidence.id}</span>
                  {confidence.numeric_range && confidence.numeric_range.length >= 2 && (
                    <span className="confidence-range">
                      {t.range}: {(confidence.numeric_range[0] * 100).toFixed(0)}% - {(confidence.numeric_range[1] * 100).toFixed(0)}%
                    </span>
                  )}
                </div>
                {confidence.criteria && confidence.criteria.length > 0 && (
                  <div className="criteria-list">
                    <p className="criteria-title">{t.criteria}:</p>
                    <ul>
                      {confidence.criteria.map((criterion, index) => (
                        <li key={index}>{criterion}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* Sources */}
          {sources.length > 0 && (
            <div className="detail-section">
              <h4 className="section-title">📚 {t.historicalSources} ({sources.length})</h4>
              <div className="sources-list">
                {sources.map((source, index) => (
                  <div key={index} className="source-card">
                    <div className="source-header">
                      <span className={`source-type ${source.type}`}>
                        {source.type === 'primary' ? '1°' : source.type === 'secondary' ? '2°' : '📖'}
                      </span>
                      <span className="source-work">{source.work}</span>
                    </div>
                    {source.author && (
                      <div className="source-detail">
                        <span className="source-label">{t.author}:</span> {source.author}
                      </div>
                    )}
                    {source.date_written && (
                      <div className="source-detail">
                        <span className="source-label">{t.date}:</span> {source.date_written}
                      </div>
                    )}
                    {source.language && (
                      <div className="source-detail">
                        <span className="source-label">{t.language}:</span> {source.language}
                      </div>
                    )}
                    {source.citation_info && (
                      <div className="source-citation">
                        <span className="source-label">📍 {t.citation}:</span> {source.citation_info}
                      </div>
                    )}
                    {source.notes && (
                      <div className="source-notes">{source.notes}</div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}

          {loading && (
            <div className="sidebar-loading">
              <div className="spinner-small"></div>
              <p>{t.loadingDetails}</p>
            </div>
          )}
        </div>
      </div>
    </>
  );
};

export default EventSidebar;
