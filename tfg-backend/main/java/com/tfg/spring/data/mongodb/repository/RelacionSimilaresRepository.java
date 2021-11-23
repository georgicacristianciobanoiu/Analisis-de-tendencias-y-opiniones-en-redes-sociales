package com.tfg.spring.data.mongodb.repository;

import com.tfg.spring.data.mongodb.model.Relacion_similares;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RelacionSimilaresRepository extends MongoRepository<Relacion_similares,String> {
}
