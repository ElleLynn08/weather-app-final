import React from 'react';

const History = ({ history }) => {
  if (!history || history.length === 0) {
    return <p style={{ textAlign: 'center', color: '#fff' }}>No history available.</p>;
  }

  return (
    <div style={{ margin: '20px', textAlign: 'center' }}>
      <h3>Weather History</h3>
      {history.map((entry, index) => (
        <div
          key={index}
          style={{
            margin: '10px 0',
            padding: '10px',
            backgroundColor: '#007bff',
            borderRadius: '10px',
            color: '#fff',
            maxWidth: '400px',
            marginLeft: 'auto',
            marginRight: 'auto',
          }}
        >
          <p>
            {entry.city} on {entry.date}
          </p>
          <p>{entry.description}</p>
          <p>{entry.temp}°F</p>
        </div>
      ))}
    </div>
  );
};

export default History;
