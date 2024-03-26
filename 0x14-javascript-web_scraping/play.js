#!/usr/bin/node

const request = require('request');
const fs = require('fs')
const url = 'https://jsonplaceholder.typicode.com/users';

request(url, (error, response, body)=>{
  // console.log(JSON.parse(body))
  const users = JSON.parse(body); // users is a list of dictionaries each dec represent one user
  for (user of users){
    // console.log(user['name'], JSON.parse(response.body))
  }
});

let data = {
    'name':1,
    'age':2
};
data = JSON.stringify(data)
console.log(typeof(data))
fs.writeFile('file.json', data, 'utf-8', (err)=>{
    if (err) {
        console.log(err)
    }
})

fs.readFile('file.json', 'utf-8', (err, data)=>{
    if (err) throw err;
    console.log(typeof(data))
    data = JSON.parse(data)
    console.log(data)
})
