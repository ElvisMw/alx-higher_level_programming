#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (b) {
    if (b === undefined) {
      b = 'X';
    }
    for (let e_m = 0; e_m < this.height; e_m++) {
      let a = '';
      for (let m = 0; m < this.width; m++) {
        a += b;
      }
      console.log(a);
    }
  }
}

module.exports = Square;
