import ReactWordcloud from 'react-wordcloud';
import React, {useState, useEffect} from 'react';
import {Resizable} from "re-resizable";
import "tippy.js/dist/tippy.css";
import "tippy.js/animations/scale.css";

function Wordcloud() {

    const [state, setState] = useState();
    const options = {
        colors: ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"],
        enableTooltip: true,
        deterministic: false,
        fontFamily: "impact",
        fontSizes: [12, 60],
        fontStyle: "normal",
        fontWeight: "normal",
        padding: 1,
        rotations: 3,
        rotationAngles: [0, 90],
        scale: "sqrt",
        spiral: "archimedean",
        transitionDuration: 1000
    };

    useEffect(() => {
        let json = require('../fonts/wordcloud.json');
        setState(json);
    }, []);

    return (
        <div className="card" style={{marginTop:"20px", marginLeft:"20px", marginRight:"20px",boxShadow: "3px 3px 6px 1px rgba(0,0,0,0.25)"}}>
            <div className="card-header">
                <b>Nube de palabras</b>
            </div>
            <ul className="list-group list-group-flush">
                <li className="list-group-item">Gráfica que contiene las palabras mas mencionadas en los tweets. Poniendo el cursor encima de la palabra se puede ver
                    el numero de veces que se ha mencionado esa palabra.
                </li>
            </ul>
            <div className="card-body">
                <ReactWordcloud words={state} options={options}/>
            </div>
        </div>
    );
}

export default Wordcloud;