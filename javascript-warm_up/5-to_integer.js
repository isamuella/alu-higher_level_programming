#!/usr/bin/node
const Arg1 = process.argv[2];
const num = Number(Arg1);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(num)}`);
}
