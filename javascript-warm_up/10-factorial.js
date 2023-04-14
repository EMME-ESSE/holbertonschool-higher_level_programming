#!/usr/bin/node
function factos (n) {
  if (isNaN(n) || (n <= 1)) {
    return 1;
  } else {
    return n * factos(n - 1);
  }
}
const arg1 = parseInt(process.argv[2]);
console.log(factos(arg1));
