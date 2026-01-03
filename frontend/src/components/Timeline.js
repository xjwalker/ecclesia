/**
 * Timeline component - renders events in a vertical timeline layout
 * Can be configured for different orientations (vertical/horizontal)
 */
import React, { useMemo, useRef } from 'react';
import PropTypes from 'prop-types';
import TimelineEvent from './TimelineEvent';
import './Timeline.css';

const Timeline = ({ 
  events, 
  onEventClick, 
  loading, 
  error, 
  orientation = 'vertical',
  alternating = true 
}) => {
  const timelineRef = useRef(null);

  // Group events by century for markers
  const centuryGroups = useMemo(() => {
    if (!events || events.length === 0) return [];
    
    const groups = {};
    events.forEach(event => {
      const century = Math.ceil(event.year / 100);
      if (!groups[century]) {
        groups[century] = {
          century,
          events: [],
          firstEventIndex: events.indexOf(event)
        };
      }
      groups[century].events.push(event);
    });
    
    return Object.values(groups).sort((a, b) => a.century - b.century);
  }, [events]);

  // Handle mouse wheel for horizontal scrolling
  const handleWheel = (e) => {
    if (orientation === 'horizontal' && timelineRef.current) {
      e.preventDefault();
      // Multiply by 3 for faster scrolling
      timelineRef.current.scrollLeft += e.deltaY * 3;
    }
  };

  if (loading) {
    return (
      <div className="timeline-loading">
        <div className="spinner"></div>
        <p>Loading timeline...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="timeline-error">
        <p>Error loading timeline</p>
      </div>
    );
  }

  if (events.length === 0) {
    return (
      <div className="timeline-empty">
        <p>No events to display</p>
      </div>
    );
  }

  return (
    <div 
      className={`timeline timeline-${orientation}`}
      ref={timelineRef}
      onWheel={handleWheel}
    >
      {orientation === 'vertical' && <div className="timeline-line"></div>}
      {orientation === 'horizontal' && <div className="timeline-line"></div>}
      
      {events.map((event, index) => {
        const century = Math.ceil(event.year / 100);
        const isFirstInCentury = centuryGroups.find(g => g.century === century)?.firstEventIndex === index;
        
        return (
          <React.Fragment key={event.id}>
            {isFirstInCentury && (
              <div 
                id={`century-${event.century_id}`} 
                className={`century-marker ${orientation}`}
              >
                <div className="century-badge">
                  {century === 1 ? '1st' : century === 2 ? '2nd' : century === 3 ? '3rd' : `${century}th`} Century
                </div>
              </div>
            )}
            <TimelineEvent
              event={event}
              isLeft={alternating ? index % 2 === 0 : false}
              onClick={onEventClick}
              orientation={orientation}
            />
          </React.Fragment>
        );
      })}
      
      {/* Extra spacing at the end to ensure line reaches bottom */}
      <div className="timeline-end-spacer"></div>
    </div>
  );
};

Timeline.propTypes = {
  events: PropTypes.arrayOf(PropTypes.object).isRequired,
  onEventClick: PropTypes.func.isRequired,
  loading: PropTypes.bool,
  error: PropTypes.object,
  orientation: PropTypes.oneOf(['vertical', 'horizontal']),
  alternating: PropTypes.bool,
};

export default Timeline;
