#!/usr/bin/node
// get response status code
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const dec = {};
    for (const todo of data) {
      const id = todo.userId;
      if (dec[id] === undefined) {
        dec[id] = 0;
      }
      if (todo.completed) {
        dec[id] += 1;
      }
    }
    for (const k in dec) {
      if (dec[k] === 0) {
        delete dec[k];
      }
    }
    console.log(dec);
  }
});
