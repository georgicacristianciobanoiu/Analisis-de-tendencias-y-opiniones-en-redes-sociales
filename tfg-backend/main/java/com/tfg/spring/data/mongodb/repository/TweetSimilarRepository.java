package com.tfg.spring.data.mongodb.repository;

import com.tfg.spring.data.mongodb.model.Tweet_similar;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface TweetSimilarRepository extends MongoRepository<Tweet_similar,String> {
}
