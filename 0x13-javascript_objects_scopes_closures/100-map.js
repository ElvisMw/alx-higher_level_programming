#!/usr/bin/node
/*
Your script must import list from the file 100-data.js
You must use a map. Tips
A new list must be created with each value equal to the
value of the initial list, multipled by the index in the list
Print both the initial list and the new list
*/
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
