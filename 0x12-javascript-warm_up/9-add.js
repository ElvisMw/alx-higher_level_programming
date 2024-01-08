#!/usr/bin/node

function add(a, b) {
    return parseInt(a) + parseInt(b);
  }
  
  const result = add(process.argv[2], process.argv[3]);
  
  if (isNaN(result)) {
    console.log('NaN');
  } else {
    console.log(result);
  }
