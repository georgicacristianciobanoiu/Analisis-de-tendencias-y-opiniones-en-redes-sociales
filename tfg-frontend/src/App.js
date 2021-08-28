import Wordcloud from "./components/wordcloud";
import PieChart from "./components/SentimientoTweets";
import LineChart from "./components/TweetsXDia";
import WorldMap from "./components/WorldMap";
import SimilarityGraph from "./components/SimilarityGraph";
import EntityInformation from "./components/EntityInformation";
import React from "react";
import "./App.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import NavigationBar from "./components/NavigationBar";
function App() {
    return (
        <>
            <NavigationBar/>
            <div style={{width: '60%', float: 'right'}}>
                <Wordcloud/>
                <PieChart/>
                <LineChart/>
                <WorldMap/>
            </div>
            <div style={{width: '40%', float: 'left'}}>
                <EntityInformation/>
                <SimilarityGraph/>
            </div>
        </>
)
    ;
}

export default App;
