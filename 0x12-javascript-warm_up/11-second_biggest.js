#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let max = parseInt(process.argv[2]);
  let secMax = parseInt(process.argv[2]);
  for (const n of process.argv) {
    const num = parseInt(n);
    if (num > max) {
      secMax = max;
      max = num;
    } else if (num < max && num > secMax) {
      secMax = num;
    }
  }
  console.log(secMax);
}
