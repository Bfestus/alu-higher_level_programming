#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
const sortedArgs = args.sort((a, b) => b - a);

if (sortedArgs.length <= 1) {
  console.log(0);
} else {
  console.log(sortedArgs[1]);
<<<<<<< HEAD
}
=======
}
>>>>>>> 2c186b2b877209ab97c483ff71065f642a284d14
