#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  let i = list.length - 1;
  for (i; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
