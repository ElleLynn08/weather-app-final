import React, { useState, useEffect } from "react";
import { DateTime } from "luxon";

const CurrentTime = ({ timeFormat }) => {
  const [currentTime, setCurrentTime] = useState("");

  useEffect(() => {
    const updateTime = () => {
      const now = DateTime.local();
      setCurrentTime(
        now.toFormat(timeFormat === "12-hour" ? "hh:mm:ss a" : "HH:mm:ss")
      );
    };

    updateTime();
    const timer = setInterval(updateTime, 1000);

    return () => clearInterval(timer);
  }, [timeFormat]);

  return (
    <p style={{ fontSize: "1rem", color: "#fff", margin: "10px 0" }}>
      Your current time is: <strong>{currentTime}</strong>
    </p>
  );
};

export default CurrentTime;





