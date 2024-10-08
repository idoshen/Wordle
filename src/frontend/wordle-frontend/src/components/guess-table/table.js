// src/Table.js
import React, { useState } from "react";
import Row from "./row";
//import './table.css';

const Table = () => {
  const [activeRow, setActiveRow] = useState(0);

  // const handleCharacterAdded = () => {
  //     setActiveRow((prevActiveRow) => prevActiveRow + 1);
  // };

  const handleEnterPress = () => {
    setActiveRow((prevActiveRow) => prevActiveRow + 1);
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
