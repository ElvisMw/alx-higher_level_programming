#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let e_m = 0;
  while ((len - e_m) > 0) {
    const aux = list[len];
    list[len] = list[e_m];
    list[e_m] = aux;
    e_m++;
    len--;
  }
  return list;
};
