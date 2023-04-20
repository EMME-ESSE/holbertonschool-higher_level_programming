#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
if (args[0] === 'https://swapi-api.hbtn.io/api/films/') {
  args[0] = 'https://swapi-api.alx-tools.com/api/films/';
}
request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      const characters = film.characters;
      if (characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)) {
        count++;
      }
    }
    console.log(count);
  }
});
