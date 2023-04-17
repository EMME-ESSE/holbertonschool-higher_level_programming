#!/usr/bin/node
const fs = require('fs');

const pathF = process.argv[2];
const cont = process.argv[3];

fs.writeFile(pathF, cont, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
