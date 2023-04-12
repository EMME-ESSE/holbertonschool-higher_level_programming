#!/usr/bin/node
const [arg] = process.argv.slice(2);

const shis = parseInt(arg);

if (isNaN(shis)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < shis; i++) {
    console.log('C is fun');
  }
}
