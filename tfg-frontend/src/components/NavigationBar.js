import Navbar from "react-bootstrap/Navbar";
import logo2 from "../fonts/loki3.png";
import React from "react";

function NavigationBar(){

    return(
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand href="/">
                <img
                    alt=""
                    src={logo2}
                    width="27px"
                    height="31px"
                    className="d-inline-block align-top"
                />{" "}
                Appate
            </Navbar.Brand>
            <Navbar.Brand href="/">
                Home
            </Navbar.Brand>
            <Navbar.Brand href="/resultados">
                Resultados
            </Navbar.Brand>
        </Navbar>
    )
}
export default NavigationBar;