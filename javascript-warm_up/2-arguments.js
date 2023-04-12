#!/usr/bin/node
const variabl = process.argv.slice(2);
if (variabl.length === 0) {
  console.log('No argument');
} else if (variabl.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
