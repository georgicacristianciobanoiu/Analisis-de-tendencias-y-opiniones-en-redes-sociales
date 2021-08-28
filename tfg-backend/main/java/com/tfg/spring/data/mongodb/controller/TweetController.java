package com.tfg.spring.data.mongodb.controller;
import com.tfg.spring.data.mongodb.model.Tweet;
import com.tfg.spring.data.mongodb.repository.TweetRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@CrossOrigin(origins = {"http://localhost:3000", "http://localhost:8081"})
@RestController
@RequestMapping("/api")
public class TweetController {
    @Autowired
    TweetRepository tweetRepository;

    @GetMapping("/tweets")
    public ResponseEntity<List<Tweet>> getAllTweets() {
        try {
            List<Tweet> tweets = new ArrayList<>(tweetRepository.findAll());

            if (tweets.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }

            return new ResponseEntity<>(tweets, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }


    @GetMapping("/tweet/{id}")
    public ResponseEntity<Tweet> getTweetById(@PathVariable("id") String id) {
        Optional<Tweet> tweetData = tweetRepository.findById(id);

        return tweetData.map(tweet -> new ResponseEntity<>(tweet, HttpStatus.OK)).orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }
    

}
