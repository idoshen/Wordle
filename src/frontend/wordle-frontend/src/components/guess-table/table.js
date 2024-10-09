// src/Table.js
import React, { useState } from "react";
import Row from "./row";
//import './table.css';

const Table = () => {
  const [activeRow, setActiveRow] = useState(0);

  // const handleCharacterAdded = () => {
  //     setActiveRow((prevActiveRow) => prevActiveRow + 1);
  // };

  const handleEnterPress = async (word) => {
    try {
      const response = await fetch(
        `http://192.168.1.222:5000/handle-input?word=${encodeURIComponent(
          word
        )}`,
        {
          method: "GET", // You can change this to 'POST' if needed
        }
      );

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json(); // Assuming the server responds with JSON
      console.log(data); // Handle the data received from the server

      if (data.legal === false) {
        alert("word not in word bank");
      } else {
        // Update the active row after the request
        setActiveRow((prevActiveRow) => prevActiveRow + 1);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div className="table">
      {[...Array(6)].map((_, index) => (
        <Row
          key={index}
          isActive={index === activeRow}
          onEnterPress={handleEnterPress}
          // onCharacterAdded={handleCharacterAdded}
        />
      ))}
    </div>
  );
};

export default Table;
