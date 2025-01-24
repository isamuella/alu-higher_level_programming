#!/usr/bin/node
const args = process.argv.slice(2).map(Number); // Convert arguments to numbers
if (args.length <= 1) {
  console.log(0); // If no arguments or only one argument, print 0
} else {
  args.sort((a, b) => b - a); // Sort in descending order
  console.log(args[1]); // Print the second biggest number
}

