#!/usr/bin/node

function factorial(n) {
    n = parseInt(n);
    if (isNaN(n)) {
      return 1;
    } else if (n < 0) {
      return "NaN";
    } else if (n === 0 || n === 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
  
  const result = factorial(process.argv[2]);
  console.log(result);
 