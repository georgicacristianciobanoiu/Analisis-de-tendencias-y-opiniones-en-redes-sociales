import * as api from '../api';
import {useEffect, useState} from "react";

function EntityInformation(){
    const [state, setState] = useState();
    const [loading, setLoading] = useState(0);
    useEffect(()=>{
        api.getEntidad().then((result)=>{
            setState(result);
            setLoading(1);
            console.log(result);
        })
    },[]);

    let fecha;
    return(
        loading!==0 &&
        <div className="card" style={{marginTop:"20px",marginLeft:"20px",boxShadow: "3px 3px 6px 1px rgba(0,0,0,0.25)"}}>
            <div className="card-header">
                {console.log(state)}
                <b>Entidad seleccionada: {state[0]["nombre_entidad"]}</b>
            </div>
            <ul className="list-group list-group-flush">
                <li className="list-group-item"><h6>Titulares</h6></li>
                {state.map(x=>(
                    <li className="list-group-item">{x["titular_origen"]} | {x["fecha"]} </li>
                ))}
            </ul>
        </div>
    );
}
export default EntityInformation;