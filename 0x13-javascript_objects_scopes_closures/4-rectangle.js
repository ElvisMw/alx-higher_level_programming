#!/usr/bin/node
/* a class Rectangle that defines a rectangle
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
*/

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let e_j = 0; e_j < this.height; e_j++) {
      let s = '';
      for (let m = 0; m < this.width; m++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
