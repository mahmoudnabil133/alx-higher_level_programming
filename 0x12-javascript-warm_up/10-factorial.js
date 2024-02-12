#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  const num = parseInt(process.argv[2]);
  console.log(fact(num));
}
function fact (num) {
  if (num <= 1) {
    return 1;
  }
  return (num * fact(num - 1));
}
