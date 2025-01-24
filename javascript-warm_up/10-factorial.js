#!/usr/bin/node
function factorial (num) {
  if(isNaN(num) || num <= 1) {
    return 1;
  }
  return num * fcactorial(num - 1);
}
console.log(factorial(paseInt(process.argv[2])));
