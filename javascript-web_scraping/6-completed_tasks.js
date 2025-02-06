#!/usr/bin/node
const request = require('require');
request(process.argv[2], (err, _, body) => {
  if (err) return console.error(err);

  const completedTasks = JSON.parse(body).reduce((acc, todo) => {
    if (todo.completed) acc[todo.userId] = (acc[todo.userId] || 0) + 1;
    return acc;
  }, {});

  console.log(completedTasks);
});
