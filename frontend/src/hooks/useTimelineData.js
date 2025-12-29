/**
 * Custom hook for fetching and managing timeline data
 */
import { useState, useEffect, useCallback } from 'react';
import apiService from '../services/api';

export const useTimelineData = (language) => {
  const [events, setEvents] = useState([]);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filters, setFilters] = useState({
    yearFrom: '',
    yearTo: '',
    confidenceId: '',
  });

  const loadData = useCallback(async (filterParams = {}) => {
    try {
      setLoading(true);
      setError(null);

      // Load summary
      const summaryResponse = await apiService.getSummary();
      setSummary(summaryResponse.data);

      // Build params for events
      const params = {};
      if (filterParams.yearFrom) params.year_from = parseInt(filterParams.yearFrom);
      if (filterParams.yearTo) params.year_to = parseInt(filterParams.yearTo);
      if (filterParams.confidenceId) params.confidence_id = filterParams.confidenceId;

      // Load events
      const eventsResponse = await apiService.getEvents(params, language);
      const eventsData = eventsResponse.data.data || eventsResponse.data;
      setEvents(eventsData);
    } catch (err) {
      setError(err);
      console.error('Timeline Data Error:', err);
    } finally {
      setLoading(false);
    }
  }, [language]);

  // Load data when language changes
  useEffect(() => {
    loadData(filters);
  }, [language, loadData]);

  const applyFilters = useCallback((newFilters) => {
    setFilters(newFilters);
    loadData(newFilters);
  }, [loadData]);

  const clearFilters = useCallback(() => {
    const emptyFilters = { yearFrom: '', yearTo: '', confidenceId: '' };
    setFilters(emptyFilters);
    loadData(emptyFilters);
  }, [loadData]);

  return {
    events,
    summary,
    loading,
    error,
    filters,
    setFilters,
    applyFilters,
    clearFilters,
    reload: loadData,
  };
};
