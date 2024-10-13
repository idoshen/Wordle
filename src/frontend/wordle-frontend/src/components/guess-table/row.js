// src/Row.js
import React, { useState, useEffect } from "react";
import Square from "./square";
import "./row.css";

//, onCharacterAdded this was an input here
const Row = ({ isActive, onEnterPress, markings }) => {
  const [squares, setSquares] = useState(["", "", "", "", ""]);
  const [currentSquare, setCurrentSquare] = useState(0);

  useEffect(() => {
    if (!isActive) return;

    const handleKeyPress = (event) => {
      const key = event.key;
      if (/^[a-zA-Z]$/.test(key) && currentSquare < squares.length) {
        const newSquares = [...squares];
        newSquares[currentSquare] = key;
        setSquares(newSquares);
        setCurrentSquare(currentSquare + 1);
        //onCharacterAdded();
      } else if (key === "Backspace") {
        const newSquares = [...squares];
        newSquares[currentSquare - 1] = "";
        setSquares(newSquares);
        if (currentSquare > 0) {
          setCurrentSquare(currentSquare - 1);
        }
      } else if (key === "Enter") {
        if (currentSquare === squares.length) {
          const word = squares.join("");
          onEnterPress(word);
        }
      }
    };

    window.addEventListener("keydown", handleKeyPress);

    return () => {
      window.removeEventListener("keydown", handleKeyPress);
    };
    //, onCharacterAdded this was down here
  }, [isActive, currentSquare, squares, onEnterPress]);

  return (
    <div className="row">
      {squares.map((char, index) => (
        <Square
          key={index}
          character={char}
          marking={markings ? markings[index] : "white-square"}
        />
      ))}
    </div>
  );
};

export default Row;
