#!/usr/bin/node
const args = process.argv.slice(2);

if ((args.length === 0) || (args.length === 1)){
  console.log(0);
} else {
  const nums = args.map(Number);
  const max = Math.max(...nums);
  const secondMax = Math.max(...nums.filter(num => num !== max));
  console.log(secondMax);
}
