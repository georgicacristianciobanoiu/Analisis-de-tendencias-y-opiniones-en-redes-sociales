package com.tfg.spring.data.mongodb.model;

import org.springframework.data.mongodb.core.mapping.Document;

import java.io.Serializable;

@Document(collection = "Entidades")
public class Entidad implements Serializable {

    private String nombre_entidad;
    private String titular_origen;
    private String origen;
    private String fecha;

    public Entidad() {
    }

    public Entidad(String nombre_entidad, String titular_origen, String origen, String fecha) {
        this.nombre_entidad = nombre_entidad;
        this.titular_origen = titular_origen;
        this.origen = origen;
        this.fecha = fecha;
    }

    public String getNombre_entidad() {
        return nombre_entidad;
    }

    public void setNombre_entidad(String nombre_entidad) {
        this.nombre_entidad = nombre_entidad;
    }

    public String getTitular_origen() {
        return titular_origen;
    }

    public void setTitular_origen(String titular_origen) {
        this.titular_origen = titular_origen;
    }

    public String getOrigen() {
        return origen;
    }

    public void setOrigen(String origen) {
        this.origen = origen;
    }

    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

}

