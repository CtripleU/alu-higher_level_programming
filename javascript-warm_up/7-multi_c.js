#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  console.log("C is fun\n".repeat(process.argv[2]));
}
