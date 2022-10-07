#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  const c = parseInt(process.argv[2]);
  let i = 0;
  for (i = 0; i < c; i++) {
    console.log("C is fun");
  }
}

// if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
//   console.log('Missing number of occurences');
// } else {
//   console.log("C is fun\n".repeat(process.argv[2]));
// }
