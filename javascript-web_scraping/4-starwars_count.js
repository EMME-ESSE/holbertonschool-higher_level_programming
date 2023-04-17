#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = 18;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } 
    const films = JSON.parse(body);
    let count = 0;
      if (films.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)) {
        count++;
      }
    
    console.log(count);

});
