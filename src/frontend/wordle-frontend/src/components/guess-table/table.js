import React, { useState, useEffect } from "react";
import Row from "./row";
import RestartButton from "./restart-button";

const Table = () => {
  const [activeRow, setActiveRow] = useState(0);
  const [rowMarkings, setRowMarkings] = useState(Array(6).fill(null));
  const [rows, setRows] = useState(Array(6).fill(["", "", "", "", ""])); // Track squares for each row
  const [isGameFinished, setIsGameFinished] = useState(false);

  const restartGame = async () => {
    try {
      const response = await fetch("http://192.168.1.222:5000/restart-game", {
        method: "POST", // or 'GET' depending on your server setup
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      // Reset the game state
      setActiveRow(0);
      setRowMarkings(Array(6).fill(null));
      setRows(Array(6).fill(["", "", "", "", ""])); // Clear all rows
      setIsGameFinished(false);
    } catch (error) {
      console.error("Error restarting the game:", error);
    }
  };

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

      const data = await response.json();
      console.log(data);

      if (data.legal === false) {
        alert("word not in word bank");
      } else {
        // Update the active row after the request
        setRowMarkings((prevMarkings) => {
          const newMarkings = [...prevMarkings];
          newMarkings[activeRow] = data.marking.map((mark) => {
            if (mark === "green") {
              return "green-square";
            } else if (mark === "yellow") {
              return "yellow-square";
            } else {
              return "white-square";
            }
          });

          if (
            newMarkings[activeRow].every(
              (marking) => marking === "green-square"
            )
          ) {
            setIsGameFinished(true);
          }
          return newMarkings;
        });

        setActiveRow((prevActiveRow) => prevActiveRow + 1);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    if (isGameFinished) {
      alert("finished game");
    }
  }, [isGameFinished]);

  return (
    <div className="table">
      {rows.map((_, index) => (
        <Row
          key={index}
          isActive={index === activeRow}
          onEnterPress={handleEnterPress}
          markings={rowMarkings[index]}
          squares={rows[index]} // Pass down the squares state
        />
      ))}
      {isGameFinished && <RestartButton onRestart={restartGame} />}
    </div>
  );
};

export default Table;
