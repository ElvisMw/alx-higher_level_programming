#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let e_j = 0; e_j < this.height; e_j++) {
      let b = '';
      for (let m = 0; m < this.width; m++) {
        b += 'X';
      }
      console.log(b);
    }
  }
}

module.exports = Rectangle;
