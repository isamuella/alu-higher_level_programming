#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], (error, _, body) => {
  if (error) return console.errror(error);
  fs.writeFile(process.argv[3], body, 'utf-8', console.error);
});
