#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (b) {
    if (b === undefined) {
      b = 'X';
    }
    for (let e = 0; e < this.height; e++) {
      let a = '';
      for (let m = 0; m < this.width; m++) {
        a += b;
      }
      console.log(a);
    }
  }
}

module.exports = Square;

