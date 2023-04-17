#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    const users = {};

    tasks.forEach((task) => {
      if (task.completed) {
        if (!users[task.userId]) {
          users[task.userId] = 1;
        } else {
          users[task.userId]++;
        }
      }
    });
    console.log(completedUser);
  }
});
