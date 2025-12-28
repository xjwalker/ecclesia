/**
 * API service for communicating with the backend.
 */
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const apiService = {
  // Summary
  getSummary: () => api.get('/api/summary'),
  
  // Centuries
  getCenturies: () => api.get('/api/centuries'),
  getCentury: (id) => api.get(`/api/centuries/${id}`),
  
  // Events
  getEvents: (params = {}, language = 'es') => api.get('/api/events', { params: { ...params, lang: language } }),
  getEvent: (id, language = 'es') => api.get(`/api/events/${id}`, { params: { lang: language } }),
  
  // Sources
  getSources: (language = 'es') => api.get('/api/sources', { params: { lang: language } }),
  getSource: (id, language = 'es') => api.get(`/api/sources/${id}`, { params: { lang: language } }),
  
  // Confidence levels
  getConfidenceLevels: () => api.get('/api/confidence'),
  getConfidenceLevel: (id) => api.get(`/api/confidence/${id}`),
};

export default apiService;
