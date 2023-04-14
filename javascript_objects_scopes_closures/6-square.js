#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    let i = 0;
    if (c === undefined) {
      c = 'X';
    }
    for (i; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
