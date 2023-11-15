#!/usr/bin/node
/*
 an instance method called charPrint(c) that prints the
rectangle using the character c
If c is undefined, use the character X
*/
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let e_m = 0; e_m < list.length; e_m++) {
    if (searchElement === list[e_m]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
