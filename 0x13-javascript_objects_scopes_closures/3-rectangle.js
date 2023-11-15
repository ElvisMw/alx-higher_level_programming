#!/usr/bin/node
// a class Rectangle that defines a rectangle
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
}

module.exports = Rectangle;
