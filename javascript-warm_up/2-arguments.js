#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
      
// function myFunction (a, b, c) {

//   if (arguments.length === 0) {
//     console.log('No argument');
//   } else if (arguments.length === 1) {
//       console.log('Argument found');
//   } else {
//       console.log('Arguments found');
//   }
  
// }

// myFunction();

// myFunction(1);

// myFunction(1, 2);
