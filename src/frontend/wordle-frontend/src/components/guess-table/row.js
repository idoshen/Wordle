import Square from "./square";
import "./row.css"

function Row () {
    return (
        <div className="row"> 
        <Square/> 
        <Square/>
        <Square/>
        <Square/>
        <Square/>
        </div>
    );
}

export default Row;