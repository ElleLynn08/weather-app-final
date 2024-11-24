import React from 'react';

const Logo = () => {
  return (
    <div style={{ textAlign: 'center', margin: '20px 0' }}>
      <video
        src="/assets/atmospheric_logo.mp4"
        autoPlay
        loop
        muted
        style={{ maxWidth: '200px' }}
      />
      <h1 style={{ color: '#fff', marginTop: '10px' }}>Atmospheric: 5-Day Weather</h1>
    </div>
  );
};

export default Logo;
