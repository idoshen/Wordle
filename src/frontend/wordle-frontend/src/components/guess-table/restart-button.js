import React from "react";

const RestartButton = ({ onRestart }) => {
  return (
    <button onClick={onRestart} style={styles.button}>
      Restart Game
    </button>
  );
};

const styles = {
  button: {
    padding: "10px 20px",
    fontSize: "16px",
    backgroundColor: "#4CAF50", // Green background
    color: "white", // White text
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
};

export default RestartButton;
