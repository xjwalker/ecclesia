/**
 * Filters component - reusable filter controls for timeline
 */
import React from 'react';
import PropTypes from 'prop-types';
import './Filters.css';

const Filters = ({ filters, onChange, onApply, onClear, translations }) => {
  const t = translations;

  const handleInputChange = (field, value) => {
    onChange({ ...filters, [field]: value });
  };

  return (
    <div className="filters-section">
      <div className="filters-container">
        <input
          type="number"
          placeholder={t.yearFrom}
          value={filters.yearFrom}
          onChange={(e) => handleInputChange('yearFrom', e.target.value)}
          className="filter-input"
        />
        <input
          type="number"
          placeholder={t.yearTo}
          value={filters.yearTo}
          onChange={(e) => handleInputChange('yearTo', e.target.value)}
          className="filter-input"
        />
        <select
          value={filters.confidenceId}
          onChange={(e) => handleInputChange('confidenceId', e.target.value)}
          className="filter-select"
        >
          <option value="">{t.allConfidenceLevels}</option>
          <option value="C1">{t.highConfidence}</option>
          <option value="C2">{t.mediumConfidence}</option>
          <option value="C3">{t.lowConfidence}</option>
        </select>
        <button onClick={onApply} className="filter-button apply">
          {t.applyFilters}
        </button>
        <button onClick={onClear} className="filter-button clear">
          {t.clear}
        </button>
      </div>
    </div>
  );
};

Filters.propTypes = {
  filters: PropTypes.shape({
    yearFrom: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    yearTo: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    confidenceId: PropTypes.string,
  }).isRequired,
  onChange: PropTypes.func.isRequired,
  onApply: PropTypes.func.isRequired,
  onClear: PropTypes.func.isRequired,
  translations: PropTypes.object.isRequired,
};

export default Filters;
