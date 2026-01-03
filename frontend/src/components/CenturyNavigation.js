/**
 * CenturyNavigation - Horizontal navigation bar showing all centuries
 * Allows clicking to scroll to specific century in timeline
 */
import React from 'react';
import PropTypes from 'prop-types';
import './CenturyNavigation.css';

const CenturyNavigation = ({ centuries, onCenturyClick, activeCentury }) => {
  // Guard against non-array or empty centuries
  if (!centuries || !Array.isArray(centuries) || centuries.length === 0) {
    return null;
  }

  const formatCenturyLabel = (century) => {
    const num = century.number || Math.ceil(century.year_start / 100);
    if (num === 1) return '1st';
    if (num === 2) return '2nd';
    if (num === 3) return '3rd';
    return `${num}th`;
  };

  return (
    <nav className="century-navigation">
      <div className="century-nav-container">
        {centuries.map((century) => (
          <button
            key={century.id}
            className={`century-nav-item ${activeCentury === century.id ? 'active' : ''}`}
            onClick={() => onCenturyClick(century.id)}
            title={century.name?.en || `Century ${century.number}`}
          >
            <span className="century-nav-number">{formatCenturyLabel(century)}</span>
            <span className="century-nav-label">Century</span>
            <span className="century-nav-range">
              {century.year_start}-{century.year_end}
            </span>
          </button>
        ))}
      </div>
    </nav>
  );
};

CenturyNavigation.propTypes = {
  centuries: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      number: PropTypes.number,
      year_start: PropTypes.number.isRequired,
      year_end: PropTypes.number.isRequired,
      name: PropTypes.shape({
        en: PropTypes.string,
        es: PropTypes.string,
      }),
    })
  ).isRequired,
  onCenturyClick: PropTypes.func.isRequired,
  activeCentury: PropTypes.string,
};

export default CenturyNavigation;
