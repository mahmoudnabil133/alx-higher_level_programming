#!/usr/bin/node
// get response status code
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const felms = JSON.parse(body);
    let sum = 0;
    for (const felm of felms.results) {
      for (const char of felm.characters) {
        const charId = char.split('/')[5];
        if (charId === '18') {
          sum += 1;
          break;
        }
      }
    }

    console.log(sum);
  }
});
