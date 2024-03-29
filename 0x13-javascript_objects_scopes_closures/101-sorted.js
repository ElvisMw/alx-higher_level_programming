#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const e in valsUniq) {
  const list = [];
  for (const b in totalist) {
    if (totalist[b][1] === valsUniq[e]) {
      list.unshift(totalist[b][0]);
    }
  }
  newDict[valsUniq[e]] = list;
}
console.log(newDict);
