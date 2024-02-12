#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else if (num > 0) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
// for (const val of arr) {
//   console.log(val);
// }
