#!/usr/bin/node
/*
a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
-the class notation for defining your class and extends
-he constructor must take 1 argument: size
-the constructor of Rectangle must be called (by using super()) 
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
