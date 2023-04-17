#!/usr/bin/node
const fs = require('fs');
const pathF = process.argv[2];

fs.readFile(pathF, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
