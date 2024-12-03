import React from "react";

const Logo = () => {
  return (
    <header className="header">
      <img
        src="./logo.svg"
        alt="Atmospheric Logo"
        style={{
          maxWidth: "250px", // Adjusted size for a slightly larger logo
          display: "block",
          margin: "0 auto",
        }}
      />
    </header>
  );
};

export default Logo;








