#!/usr/bin/node
// get response status code
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const char of characters) {
      request(char, (err2, res2, body2) => {
        if (err2) {
          throw err2;
        } else {
          const charName = JSON.parse(body2).name;
          console.log(charName);
        }
      });
    }
  }
});
