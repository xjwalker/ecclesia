/**
 * HighlightBadge - Displays event highlights with icons and colors
 * Used to show doctrine_established, historical_event, or council highlights
 */
import React from 'react';
import PropTypes from 'prop-types';
import './HighlightBadge.css';

const HighlightBadge = ({ highlight, eventType, compact = false }) => {
  if (!highlight && eventType !== 'Council') {
    return null;
  }

  const getHighlightInfo = () => {
    // Council events get special treatment
    if (eventType === 'Council') {
      return {
        type: 'council',
        label: { en: 'Council', es: 'Concilio' },
        icon: '⛪',
        color: '#9333ea', // purple
      };
    }

    switch (highlight) {
      case 'doctrine_established':
        return {
          type: 'doctrine',
          label: { en: 'Doctrine', es: 'Doctrina' },
          icon: '📜',
          color: '#dc2626', // red
        };
      case 'historical_event':
        return {
          type: 'historical',
          label: { en: 'Historical', es: 'Histórico' },
          icon: '🏛️',
          color: '#2563eb', // blue
        };
      default:
        return null;
    }
  };

  const info = getHighlightInfo();
  if (!info) return null;

  return (
    <div 
      className={`highlight-badge highlight-${info.type} ${compact ? 'compact' : ''}`}
      style={{ backgroundColor: info.color }}
      title={info.label.en}
    >
      <span className="highlight-icon">{info.icon}</span>
      {!compact && <span className="highlight-label">{info.label.en}</span>}
    </div>
  );
};

HighlightBadge.propTypes = {
  highlight: PropTypes.oneOf(['doctrine_established', 'historical_event', null]),
  eventType: PropTypes.string,
  compact: PropTypes.bool,
};

export default HighlightBadge;
