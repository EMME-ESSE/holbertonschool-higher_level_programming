#!/usr/bin/node
const [arg1] = process.argv.slice(2);
if (arg1) {
  console.log(arg1);
} else {
  console.log('No argument');
}
