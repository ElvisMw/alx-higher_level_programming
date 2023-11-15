#!/usr/bin/node
/* Prototype: exports.logMe = function (item)
Output format: <number arguments already
printed>: <current argument value></current>
*/
let narg = 0;

exports.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
