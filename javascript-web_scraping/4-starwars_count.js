#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, _, body) => {
  if (error) return console.error(error);
  console.log(JSON.parse(body).results.filter(
  f => f.characters.find(c => c.includes('/18/'))).length);
});
