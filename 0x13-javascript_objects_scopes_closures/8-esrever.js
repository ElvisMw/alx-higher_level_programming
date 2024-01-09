#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let e = 0;
  while ((len - e) > 0) {
    const aux = list[len];
    list[len] = list[e];
    list[e] = aux;
    e++;
    len--;
  }
  return list;
};

