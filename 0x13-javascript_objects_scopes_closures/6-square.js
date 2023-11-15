#!/usr/bin/node
/*
a class Square that defines a square and inherits from Square of 5-square.js:
-the class notation for defining your class and extends
-This instance method called charPrint(c)prints the rectangle using the character c
If c is undefined, use the character X
*/
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let e_m = 0; e_m < this.height; e_m++) {
      let s = '';
      for (let m = 0; m < this.width; m++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
