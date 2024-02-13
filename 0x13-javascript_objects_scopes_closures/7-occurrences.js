#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  for (const num of list) {
    if (num === searchElement) {
      cnt += 1;
    }
  }
  return cnt;
};
