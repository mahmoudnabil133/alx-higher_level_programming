#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else if (num > 0) {
  const arr = [];
  for (let i = 0; i < num; i++) {
    let str = '';
    for (let j = 0; j < num; j++) {
      str += 'X';
    }
    arr.push(str);
  }
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
  }
}
