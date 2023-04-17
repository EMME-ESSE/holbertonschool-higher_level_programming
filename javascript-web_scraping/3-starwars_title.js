#!/usr/bin/node
const request = require('request');
const mId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${mId}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
