package com.tfg.spring.data.mongodb.controller;
import com.tfg.spring.data.mongodb.model.Relacion_similares;
import com.tfg.spring.data.mongodb.repository.RelacionSimilaresRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;



@CrossOrigin(origins = "http://localhost:8081")
@RestController
@RequestMapping("/api")
public class RelacionSimilaresController {
    @Autowired
    RelacionSimilaresRepository relacionSimilaresRepository;

    @GetMapping("/relacion_similares")
    @CrossOrigin(origins = "http://localhost:3000")
    public ResponseEntity<List<Relacion_similares>> getAllRelacionesSimilitud() {
        try {
            List<Relacion_similares> relacion_similares = new ArrayList<>(relacionSimilaresRepository.findAll());

            if (relacion_similares.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }

            return new ResponseEntity<>(relacion_similares, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
