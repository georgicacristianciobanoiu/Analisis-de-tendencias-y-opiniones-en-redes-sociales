package com.tfg.spring.data.mongodb.model;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.io.Serializable;

@Document(collection = "Relacion_similares")
public class Relacion_similares implements Serializable {

    @Id
    private String _id;
    private String usuario;
    private String tweet_principal_texto;
    private int tweet_principal_interacciones;
    private Tweet_similar[] tweets_similares;

    public Relacion_similares() {
    }

    public Relacion_similares(String _id, String usuario, String tweet_principal_texto, int tweet_principal_interacciones, Tweet_similar[] tweets_similares) {
        this._id = _id;
        this.usuario = usuario;
        this.tweet_principal_texto = tweet_principal_texto;
        this.tweet_principal_interacciones = tweet_principal_interacciones;
        this.tweets_similares = tweets_similares;
    }

    public String getId() {
        return _id;
    }

    public void setId(String _id) {
        this._id = _id;
    }

    public String getUsuario() {
        return usuario;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    public String getTexto() {
        return tweet_principal_texto;
    }

    public void setTexto(String texto) {
        this.tweet_principal_texto = texto;
    }

    public int getTweet_principal_interacciones() {
        return tweet_principal_interacciones;
    }

    public void setTweet_principal_interacciones(int tweet_principal_interacciones) {
        this.tweet_principal_interacciones = tweet_principal_interacciones;
    }

    public Tweet_similar[] getSimilares() {
        return tweets_similares;
    }

    public void setSimilares(Tweet_similar[] similares) {
        this.tweets_similares = similares;
    }
}
