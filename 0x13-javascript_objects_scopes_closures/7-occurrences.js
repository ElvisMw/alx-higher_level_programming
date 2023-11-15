#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let e_m = 0; e_m < list.length; e_m++) {
    if (searchElement === list[e_m]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
