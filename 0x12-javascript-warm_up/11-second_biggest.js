#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let max = parseInt(process.argv[2]);
  let secMax = Number.NEGATIVE_INFINITY; 
  for (let i = 3; i < process.argv.length; i++) {
    const num = parseInt(process.argv[i]);
    if (num > max) {
      secMax = max;
      max = num;
    } else if (num < max && num > secMax) {
      secMax = num;
    }
  }
  console.log(secMax);
}
