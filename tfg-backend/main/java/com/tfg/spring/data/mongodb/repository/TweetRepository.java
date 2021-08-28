package com.tfg.spring.data.mongodb.repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.mongodb.repository.MongoRepository;
import com.tfg.spring.data.mongodb.model.Tweet;

public interface TweetRepository extends MongoRepository<Tweet, String> {
    List<Tweet> findTweetByLocalizacion(String localizacion);
    List<Tweet> findTweetBySentimiento(String sentimiento);
}
