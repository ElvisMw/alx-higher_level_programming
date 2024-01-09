#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let e = 0; e < list.length; e++) {
    if (searchElement === list[e]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};

