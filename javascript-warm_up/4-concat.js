#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('${argv[0]} is ${argv[1]}');
} else if (args.length === 1) {
  console.log('${argv[0]} is undefined');
} else {
  console.log('undefined is undefined');
}
