export const translations = {
  en: {
    // Header
    appTitle: 'Ecclesia Timeline',
    subtitle: 'Historical Christianity Timeline',
    events: 'Events',
    sources: 'Sources',
    centuries: 'Centuries',
    
    // Filters
    yearFrom: 'Year from',
    yearTo: 'Year to',
    allConfidenceLevels: 'All Confidence Levels',
    highConfidence: 'High (C1)',
    mediumConfidence: 'Medium (C2)',
    lowConfidence: 'Low (C3)',
    applyFilters: 'Apply Filters',
    clear: 'Clear',
    
    // Timeline
    clickForDetails: 'Click for more details →',
    
    // Event card
    region: 'Region',
    type: 'Type',
    sourcesLabel: 'Sources',
    
    // Confidence levels
    confidence: {
      C1: 'High',
      C2: 'Medium',
      C3: 'Low'
    },
    
    // Sidebar
    eventDetails: 'Event Details',
    description: 'Description',
    peopleInvolved: 'People Involved',
    whatHappened: 'What Happened?',
    whyConfidence: 'Why This Confidence Level?',
    historicalSignificance: 'Historical Significance',
    information: 'Information',
    centuryContext: 'Century Context',
    years: 'Years',
    confidenceLevel: 'Confidence Level',
    range: 'Range',
    criteria: 'Criteria',
    historicalSources: 'Historical Sources',
    author: 'Author',
    date: 'Date',
    language: 'Language',
    citation: 'Citation',
    id: 'ID',
    century: 'Century',
    reliability: 'Reliability',
    
    // Loading and errors
    loading: 'Loading timeline...',
    error: 'Error loading data from API. Make sure the backend is running.',
    retry: 'Retry',
    noEvents: 'No events found',
    loadingDetails: 'Loading details...',
    
    // Footer
    footerText: 'Ecclesia Timeline - Historical Christianity Data',
    apiLabel: 'API'
  },
  
  es: {
    // Header
    appTitle: 'Línea de Tiempo Ecclesia',
    subtitle: 'Historia del Cristianismo',
    events: 'Eventos',
    sources: 'Fuentes',
    centuries: 'Siglos',
    
    // Filters
    yearFrom: 'Año desde',
    yearTo: 'Año hasta',
    allConfidenceLevels: 'Todos los Niveles de Confianza',
    highConfidence: 'Alta (C1)',
    mediumConfidence: 'Media (C2)',
    lowConfidence: 'Baja (C3)',
    applyFilters: 'Aplicar Filtros',
    clear: 'Limpiar',
    
    // Timeline
    clickForDetails: 'Click para más detalles →',
    
    // Event card
    region: 'Región',
    type: 'Tipo',
    sourcesLabel: 'Fuentes',
    
    // Confidence levels
    confidence: {
      C1: 'Alta',
      C2: 'Media',
      C3: 'Baja'
    },
    
    // Sidebar
    eventDetails: 'Detalles del Evento',
    description: 'Descripción',
    peopleInvolved: 'Personas Involucradas',
    whatHappened: '¿Qué Sucedió?',
    whyConfidence: '¿Por Qué Este Nivel de Confianza?',
    historicalSignificance: 'Importancia Histórica',
    information: 'Información',
    centuryContext: 'Contexto del Siglo',
    years: 'Años',
    confidenceLevel: 'Nivel de Confiabilidad',
    range: 'Rango',
    criteria: 'Criterios',
    historicalSources: 'Fuentes Históricas',
    author: 'Autor',
    date: 'Fecha',
    language: 'Idioma',
    citation: 'Cita',
    id: 'ID',
    century: 'Siglo',
    reliability: 'Confiabilidad',
    
    // Loading and errors
    loading: 'Cargando línea de tiempo...',
    error: 'Error al cargar datos de la API. Asegúrate de que el backend esté funcionando.',
    retry: 'Reintentar',
    noEvents: 'No se encontraron eventos',
    loadingDetails: 'Cargando detalles...',
    
    // Footer
    footerText: 'Línea de Tiempo Ecclesia - Historia del Cristianismo',
    apiLabel: 'API'
  }
};

export const getTranslation = (lang = 'en') => {
  return translations[lang] || translations.en;
};
