import { Line } from 'react-chartjs-2';
import React, { useState,useEffect } from 'react';
import tweetsData from '../fonts/numero_tweets_dia.json';

function LineChart() {
    const [state, setState] = useState();
    let data = {
        labels: [],
        datasets: [
            {
                label: 'Número de Tweets por día',
                data: [],
                fill: false,
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgba(255, 99, 132, 0.2)',
            },
        ],
    };

    useEffect(() => {
        let labels = [];
        let number_tweets = [];
        tweetsData.map((x) => {
            labels.push(x.fecha);
            number_tweets.push(x.numero_tweets);
        })
        data.labels = labels;
        data.datasets[0].data = number_tweets;
        setState(data);
        console.log(state);
    }, []);

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: false,
                    },
                },
            ],
        },
    };
    return (
        <div className="card" style={{marginTop:"20px", marginLeft:"20px", marginRight:"20px",boxShadow: "3px 3px 6px 1px rgba(0,0,0,0.25)"}}>
            <div className="card-header">
                <b>Número de tweets por día</b>
            </div>
            <ul className="list-group list-group-flush">
                <li className="list-group-item">Gráfica que muestra el número de tweets emitidos en cada fecha.
                </li>
            </ul>
            <div className="card-body">
                <div className="chart-container" style={{position: 'relative', height:'378px', width:'540px'}}>
                    <Line data={state} options={options} />
                </div>
            </div>
        </div>
    );
}


export default LineChart;