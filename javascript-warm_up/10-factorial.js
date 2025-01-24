#!/usr/bin/node
function factorial (num) {
  if(isNaN(num) || num < 0) {
    return 1;
  }
  return num * fcactorial(num - 1);
}
console.log(factorial(paseInt(process.argv[2])));
