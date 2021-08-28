package com.tfg.spring.data.mongodb.model;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.io.Serializable;

@Document(collection = "Tweet_similar")
public class Tweet_similar implements Serializable {
    @Id
    private String _id;
    private String texto;
    private int total_interacciones;
    private double distancia_coseno;

    public Tweet_similar(){

    }
    public Tweet_similar(String _id, String texto, int total_interacciones, double distancia_coseno) {
        this._id = _id;
        this.texto = texto;
        this.total_interacciones = total_interacciones;
        this.distancia_coseno = distancia_coseno;
    }

    public String getTweet_id() {
        return _id;
    }

    public void setTweet_id(String _id) {
        this._id = _id;
    }

    public String getTexto() {
        return texto;
    }

    public void setTexto(String texto) {
        this.texto = texto;
    }

    public int getTotal_interacciones() {
        return total_interacciones;
    }

    public void setTotal_interacciones(int total_interacciones) {
        this.total_interacciones = total_interacciones;
    }

    public double getDistancia_coseno() {
        return distancia_coseno;
    }

    public void setDistancia_coseno(double distancia_coseno) {
        this.distancia_coseno = distancia_coseno;
    }
}
