#!/usr/bin/node
const argument = process.argv[2];

if (typeof argument === 'undefined') {
  console.log('No argument');
} else {
  console.log(argument);
}