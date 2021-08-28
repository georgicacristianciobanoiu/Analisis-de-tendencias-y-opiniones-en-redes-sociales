import logo2 from "../fonts/loki3.png";
import image from "../fonts/charts.png";
import reactLogo from "../fonts/react-logo.svg";
import React from "react";
import "../styles/Home.css";
import NavigationBar from "./NavigationBar";

function Home(){

    return(
        <>
            <NavigationBar/>
            <div className="Home-body">
                <img src={logo2} className="loki-logo"/>
                <h1 className="titulo">¿Qué es Appate?</h1>
                <div style={{float:"left"}}>
                    <div className="texto">¡Hola! Mi nombre es Georgica Cristian Ciobanoiu y soy un estudiante de Ingenieria Informática en la Universidad Carlos III de Madrid.
                        Appate es la primera versión de una futura aplicación web que debería servir para que los usuarios puedan visualizar diferentes gráficas sobre tweets
                        relacionados con una noticia falsa con el objetivo de que puedan realizar un análisis para obtener diferentes conclusiones.
                    </div>
                </div>
                <div style={{float:"right"}}>
                    <img src={reactLogo} className={"React-logo"}/>
                    <img src={image} className={"charts-logo"}/>
                </div>
            </div>
        </>
    )
}
export default Home;