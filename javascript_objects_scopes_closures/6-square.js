#!/usr/bin/node
const Square = require('./5-rectangle.js');

module.exports = class Square extends Square {
  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for ( i = 0; i < this.height; i++) cosole.log(c.repeat(this.width));
    }
  }
};
