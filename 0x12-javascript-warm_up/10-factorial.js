#!/usr/bin/node
const num = parseInt(process.argv[2]);
function fact (n) {
  if (n === 1) return 1;
  return (n * fact(n - 1));
}
if (isNaN(num)) {
  console.log(1);
} else {
  const result = fact(num);
  console.log(result);
}
