import "./square.css";

function Square({ character, marking }) {
  return <div className={`square ${marking}`}>{character}</div>;
}

export default Square;
