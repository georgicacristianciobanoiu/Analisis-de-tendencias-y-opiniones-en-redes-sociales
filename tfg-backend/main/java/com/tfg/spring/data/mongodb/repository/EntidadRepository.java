package com.tfg.spring.data.mongodb.repository;

import com.tfg.spring.data.mongodb.model.Entidad;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface EntidadRepository extends MongoRepository<Entidad, ObjectId> {
}
