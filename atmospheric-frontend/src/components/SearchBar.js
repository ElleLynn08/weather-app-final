import React, { useState } from 'react';

const SearchBar = ({ onSearch }) => {
  const [city, setCity] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (city) {
      onSearch(city);
      setCity(''); // Clear input after search
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ textAlign: 'center', margin: '20px' }}>
      <input
        type="text"
        placeholder="Enter a city..."
        value={city}
        onChange={(e) => setCity(e.target.value)}
        style={{
          padding: '10px',
          borderRadius: '5px',
          border: '1px solid #ccc',
          width: '70%',
          maxWidth: '400px',
        }}
      />
      <button
        type="submit"
        style={{
          padding: '10px 20px',
          marginLeft: '10px',
          borderRadius: '5px',
          backgroundColor: '#007bff',
          color: '#fff',
          border: 'none',
        }}
      >
        Search
      </button>
    </form>
  );
};

export default SearchBar;
