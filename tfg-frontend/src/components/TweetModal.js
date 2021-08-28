import React, {useState, useEffect} from 'react';
import Modal from 'react-modal';

function TweetModal(props) {
    const [modalIsOpen, setIsOpen] = useState(false);
    const [tweetData, setTweetData] = useState({
        id:"",
        fecha:"",
        localizacion:"",
        n_likes:"",
        n_menciones:"",
        n_respuestas:"",
        n_retweets:"",
        sentimiento:"",
        texto:"",
        total_interacciones:"",
        usuario:"",
        link_tweet:""
    });

    let customStyles = {
        content: {
            top: '50%',
            left: '50%',
            right: 'auto',
            bottom: 'auto',
            marginRight: '-50%',
            transform: 'translate(-50%, -50%)',
            width:"50%",
            height:"50%"
        },
    };

    useEffect(() => {
        setIsOpen(props.modalShow);
        console.log(props.modalShow)
    }, [props.modalShow])

    useEffect(() => {
        props.data!==undefined &&
        setTweetData(props.data)
        console.log(props.data)
    }, [props.data])

    return (
        <Modal
            isOpen={modalIsOpen}
            onRequestClose={props.onCloseModal}
            style={customStyles}
        >
            <h2>La información del tweet seleccionado es:</h2>
            <ul>
                <li><b>Id:</b> {tweetData.id}</li>
                <li><b>Autor:</b> @{tweetData.usuario}</li>
                <li><b>Texto:</b> {tweetData.texto}</li>
                <li><b>Sentimiento:</b> {tweetData.sentimiento}</li>
                <li><b>Fecha:</b> {tweetData.fecha.replace(/T[\w\W]*/gm,"")}</li>
                <li><b>Número de likes:</b> {tweetData.n_likes}</li>
                <li><b>Número de retweets:</b> {tweetData.n_retweets}</li>
                <li><b>Número de menciones:</b> {tweetData.n_menciones}</li>
                <li><b>Número de respuestas:</b> {tweetData.n_respuestas}</li>
                <li><b>Localización:</b> {tweetData.localizacion!==null?tweetData.localizacion:"No aparece"}</li>
                <li><b>Link del tweet:</b> {tweetData.link_tweet}</li>
            </ul>
            <button style={{float:"right"}} onClick={()=>props.onCloseModal()}>Cerrar</button>
        </Modal>
    );
}

export default TweetModal;
