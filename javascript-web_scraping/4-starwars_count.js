#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';

request.get({ url }, (error, response, data) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(data).results;
  let cont = 0;
  for (const film of films) {
    const characters = film.characters;
    if (characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}`)) {
      cont++;
    }
  }
  console.log(cont);
});
