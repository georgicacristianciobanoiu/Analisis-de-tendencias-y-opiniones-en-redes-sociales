import * as api from '../api';
import React, {useState, useEffect} from 'react';
import {Graph} from "react-d3-graph";
import TweetModal from "./TweetModal";

function SimilarityGraph() {
    const [state, setState] = useState();
    const [loading, setLoading] = useState(0);
    const [showModal, setShowModal] = useState(false);
    const [selectedTweetData, setSelectedTweetData] = useState();

    let config = {
        height: 1020,
        width: 720,
        linkHighlightBehavior: true,
        highlightDegree: 1,
        highlightOpacity: 0.2,
        node:{
            labelProperty:"autor"
        }
    }

    function generateRandomColor() {
        let letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

    useEffect(() => {
        let data;
        let nodes = []
        let links = []
        api.getTweetSimilarityRelations().then((result) => {
            data = result;
            console.log(data)
            for (let i = 0; i < data.length; i++) {
                let principal_tweet_id;
                let group_color = generateRandomColor();
                principal_tweet_id = data[i]['id'];
                nodes.push({
                    'id': principal_tweet_id, 'size': data[i]['tweet_principal_interacciones'] * 10,
                    'symbolType': "star", 'color': group_color, 'autor':"@"+data[i]['usuario']
                })
                console.log(data[i]['tweet_principal_interacciones']);
                let array_similares = data[i]['similares'];
                for (let j = 0; j < array_similares.length; j++) {
                    nodes.push({
                        'id': array_similares[j]['tweet_id'],
                        'size': array_similares[j]['total_interacciones'],
                        'color': group_color,
                        'renderLabel': false
                    })
                    links.push({
                        'source': array_similares[j]['tweet_id'],
                        'target': principal_tweet_id,
                        'strokeWidth': array_similares[j]['distancia_coseno'] * 10,
                        'color': "#D6D6D6"
                    })
                }
            }
            setState({
                nodes: nodes,
                links: links
            })
            setLoading(1);
        });

    }, []);

    const onClickNode = function (nodeId) {
        api.getTweet(nodeId).then((result) => {
            let tweetData={
                id:result.id,
                fecha:result.fecha,
                localizacion:result.localizacion,
                n_likes:result.n_likes,
                n_menciones:result.n_menciones,
                n_respuestas:result.n_respuestas,
                n_retweets:result.n_retweets,
                sentimiento:result.sentimiento,
                texto:result.texto,
                total_interacciones:result.total_interacciones,
                usuario:result.usuario,
                link_tweet:result.link_tweet
            }
            setSelectedTweetData(tweetData);
        });
        setShowModal(true);
    };

    function onCloseModal() {
        setShowModal(false);
    }

    const onClickLink = function (source, target) {
        window.alert(`Clicked link between ${source} and ${target}`);
    };

    return (
        loading !== 0 &&
            <div className="card" style={{marginTop:"20px",marginLeft:"20px",boxShadow: "3px 3px 6px 1px rgba(0,0,0,0.25)"}}>
                <div className="card-header">
                    <b>Similitud entre tweets</b>
                </div>
                <ul className="list-group list-group-flush">
                    <li className="list-group-item">Grafo que muestra la relacion entre los diferentes tweets extraidos. Pulsando sobre cualquier nodo podremos
                        ver la informacion del tweet asociado a ese nodo.
                    </li>
                </ul>
                <div className="card-body">
                    <TweetModal data={selectedTweetData} modalShow={showModal} onCloseModal={onCloseModal}/>
                    <Graph
                        config={config}
                        id="graph-id" // id is mandatory
                        data={state}
                        onClickNode={onClickNode}
                        onClickLink={onClickLink}
                    />
                </div>
            </div>
    );
}


export default SimilarityGraph;