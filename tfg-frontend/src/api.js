import axios from 'axios';

let apiRoot= "http://localhost:8080";

export function getTweetSimilarityRelations() {
    return axios.get(apiRoot + '/api/relacion_similares')
        .then(function (response) {
            return response.data;
        })
        .catch(function (error) {
            console.log(error);
        });
}

export function getTweet(id) {
    return axios.get(apiRoot + '/api/tweet/' + id)
        .then(function (response) {
            return response.data;
        })
        .catch(function (error) {
            console.log(error);
        });
}

export function getEntidad() {
    return axios.get(apiRoot + '/api/entidad')
        .then(function (response) {
            return response.data;
        })
        .catch(function (error) {
            console.log(error);
        });
}
