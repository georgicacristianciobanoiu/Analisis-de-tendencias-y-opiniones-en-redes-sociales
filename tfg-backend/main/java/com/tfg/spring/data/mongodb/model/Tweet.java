package com.tfg.spring.data.mongodb.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.io.Serializable;

@Document(collection = "Tweets")
public class Tweet implements Serializable {
    @Id
    private String id;

    private String usuario;
    private int n_likes;
    private int n_retweets;
    private int n_respuestas;
    private int n_menciones;
    private String texto;
    private String fecha;
    private int total_interacciones;
    private String localizacion;
    private String sentimiento;
    private String link_tweet;

    public Tweet(){

    }
    public Tweet(String id, String usuario, int n_likes, int n_retweets, int n_respuestas, int n_menciones, String texto, String fecha, int total_interacciones, String localizacion, String sentimiento, String link_tweet) {
        this.id = id;
        this.usuario = usuario;
        this.n_likes = n_likes;
        this.n_retweets = n_retweets;
        this.n_respuestas = n_respuestas;
        this.n_menciones = n_menciones;
        this.texto = texto;
        this.fecha = fecha;
        this.total_interacciones = total_interacciones;
        this.localizacion = localizacion;
        this.sentimiento = sentimiento;
        this.link_tweet = link_tweet;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUsuario() {
        return usuario;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    public int getN_likes() {
        return n_likes;
    }

    public void setN_likes(int n_likes) {
        this.n_likes = n_likes;
    }

    public int getN_retweets() {
        return n_retweets;
    }

    public void setN_retweets(int n_retweets) {
        this.n_retweets = n_retweets;
    }

    public int getN_respuestas() {
        return n_respuestas;
    }

    public void setN_respuestas(int n_respuestas) {
        this.n_respuestas = n_respuestas;
    }

    public int getN_menciones() {
        return n_menciones;
    }

    public void setN_menciones(int n_menciones) {
        this.n_menciones = n_menciones;
    }

    public String getTexto() {
        return texto;
    }

    public void setTexto(String texto) {
        this.texto = texto;
    }

    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public int getTotal_interacciones() {
        return total_interacciones;
    }

    public void setTotal_interacciones(int total_interacciones) {
        this.total_interacciones = total_interacciones;
    }

    public String getLocalizacion() {
        return localizacion;
    }

    public void setLocalizacion(String localizacion) {
        this.localizacion = localizacion;
    }

    public String getSentimiento() {
        return sentimiento;
    }

    public void setSentimiento(String sentimiento) {
        this.sentimiento = sentimiento;
    }

    public String getLink_tweet() {
        return link_tweet;
    }

    public void setLink_tweet(String link_tweet) {
        this.link_tweet = link_tweet;
    }
}
