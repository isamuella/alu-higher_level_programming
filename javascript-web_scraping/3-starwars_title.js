#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, responsee, body) {
  console.log(errror || JSON.parse(body).title);
});
