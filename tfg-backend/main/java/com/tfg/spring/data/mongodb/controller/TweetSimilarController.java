package com.tfg.spring.data.mongodb.controller;
import com.tfg.spring.data.mongodb.model.Tweet;
import com.tfg.spring.data.mongodb.model.Tweet_similar;
import com.tfg.spring.data.mongodb.repository.TweetRepository;
import com.tfg.spring.data.mongodb.repository.TweetSimilarRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@CrossOrigin(origins = "http://localhost:8081")
@RestController
@RequestMapping("/api")
public class TweetSimilarController {
    @Autowired
    TweetSimilarRepository tweetSimilarRepository;

    @GetMapping("/tweets_similares")
    public ResponseEntity<List<Tweet_similar>> getAllSimilarTweets() {
        try {
            List<Tweet_similar> tweets = new ArrayList<>(tweetSimilarRepository.findAll());

            if (tweets.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }

            return new ResponseEntity<>(tweets, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }


    @GetMapping("/tweet_similar/{id}")
    public ResponseEntity<Tweet_similar> getTweetSimilarById(@PathVariable("id") String id) {
        Optional<Tweet_similar> tweetSimilar = tweetSimilarRepository.findById(id);

        return tweetSimilar.map(tweet -> new ResponseEntity<>(tweet, HttpStatus.OK)).orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }
}
