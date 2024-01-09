#!/usr/bin/node
function getSecMax (list) {
  let max = parseInt(list[0]);
  let SecMax = parseInt(list[1]);
  if (SecMax > max) {
    const temp = max;
    max = SecMax;
    SecMax = temp;
  }
  for (let num of list) {
    num = parseInt(num);
    if (num > max) {
      SecMax = max;
      max = num;
    }
  }
  return SecMax;
}
if (isNaN(process.argv[3])) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2, process.argv.length);
  const result = getSecMax(numbers);
  console.log(result);
}
