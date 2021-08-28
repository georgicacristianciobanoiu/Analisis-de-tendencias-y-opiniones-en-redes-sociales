import {Line, Pie} from 'react-chartjs-2';
import tweetsData from "../fonts/sentimiento_tweets.json";
import React, { useState,useEffect } from 'react';


function PieChart() {
    const [state, setState] = useState();
    let data = {
        labels: [],
        datasets: [
            {
                label: 'Cantidad de Tweets según la polaridad',
                data: [],
                backgroundColor: [
                    'rgba(117,0,0)',
                    'rgba(233,12,12)',
                    'rgb(191,178,166)',
                    'rgb(115,224,120)',
                    'rgba(39,255,0)',
                ],
                borderColor: [
                    'rgb(45,42,42)',

                ],
                borderWidth: 1,
            },
        ],
    };
    useEffect(() => {
        let labels = [];
        let numero_tweets_polaridad = [];
        tweetsData.map((x) => {
            labels.push(x.sentimiento);
            numero_tweets_polaridad.push(x.numero);
        })
        data.labels = labels;
        data.datasets[0].data = numero_tweets_polaridad;
        setState(data);
        console.log(state);
    }, []);
    return (

        <div className="card" style={{float:"right", width: '32%',marginTop:"20px", marginLeft:"20px", marginRight:"20px",boxShadow: "3px 3px 6px 1px rgba(0,0,0,0.25)"}}>
            <div className="card-header">
                <b>Polaridad de los tweets</b>
            </div>
            <ul className="list-group list-group-flush">
                <li className="list-group-item">Gráfica que muestra la polaridad de los tweets. Poniendo el cursor encima de cualquier porción de la gráfica podemos
                    ver el número de tweets que pertencen a esa polaridad.
                </li>
            </ul>
            <div className="card-body">
                <div className="chart-container">
                    <Pie data={state}/>
                </div>
            </div>
        </div>
    );
}

export default PieChart;