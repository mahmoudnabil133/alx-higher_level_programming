#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number is', num);
}
