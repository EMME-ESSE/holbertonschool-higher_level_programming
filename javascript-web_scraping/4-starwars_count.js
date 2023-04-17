#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

const characterId = 18;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } 
  if (response.statusCode !== 200) {
    console.error(`Unexpected response: ${response.statusCode}`);
    return;
  }
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      const characters = film.characters;
      if (characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)) {
        count++;
      }
    
    console.log(count);
  }
});
