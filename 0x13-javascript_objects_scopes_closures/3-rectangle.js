#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let e = 0; e < this.height; e++) {
      let b = '';
      for (let m = 0; m < this.width; m++) {
        b += 'X';
      }
      console.log(b);
    }
  }
}

module.exports = Rectangle;

