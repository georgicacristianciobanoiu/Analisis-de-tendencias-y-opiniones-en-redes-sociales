package com.tfg.spring.data.mongodb.controller;


import com.tfg.spring.data.mongodb.model.Entidad;
import com.tfg.spring.data.mongodb.repository.EntidadRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@CrossOrigin(origins = {"http://localhost:3000", "http://localhost:8081"})
@RestController
@RequestMapping("/api")
public class EntidadController {

    @Autowired
    EntidadRepository entidadRepository;

    @GetMapping("/entidad")
    public ResponseEntity<List<Entidad>> getAllEntidades() {
        try {
            List<Entidad> entidades = new ArrayList<>(entidadRepository.findAll());

            if (entidades.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }

            return new ResponseEntity<>(entidades, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
