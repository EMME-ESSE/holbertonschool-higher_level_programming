#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
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
    console.log(Object.entries(users)
      .map(([userId, count]) => `User ${userId} completed ${count} tasks.`)
      .join('\n')
    );
  }
});
