import React, {useState, useEffect} from 'react';
import tweetsData from "../fonts/localizacion_tweets.json";
import {WorldMap} from "react-svg-worldmap";
import {Line} from "react-chartjs-2";

let countries = require("i18n-iso-countries")
countries.registerLocale(require("i18n-iso-countries/langs/es.json"));

function Map() {
    const [state, setState] = useState([]);

    useEffect(() => {
        let data = []
        tweetsData.map((x) => {
            let countryCode = countries.getAlpha2Code(x.localizacion, "es")
            data.push({country: countryCode, value: x.numero});
        })
        setState(data);
    }, [])

    return (
        <div className="card" style={{width:"95%",marginTop:"50px", marginLeft:"20px", marginRight:"20px",boxShadow: "3px 3px 6px 1px rgba(0,0,0,0.25)"}}>
            <div className="card-header">
                <b>Localización de los tweets</b>
            </div>
            <ul className="list-group list-group-flush">
                <li className="list-group-item">Gráfica que muestra el número de tweets emitidos en cada país.
                </li>
            </ul>
            <div className="card-body">
                <WorldMap color="red"
                          value-suffix="tweets" size="responsive" data={state}
                          />
            </div>
        </div>
    );
}

export default Map;