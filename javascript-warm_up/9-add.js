#!/usr/bin/node
function add(a, b){
    a + b;
}
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (isNaN(arg1) || isNaN(arg2)) {
    console.log('NaN');
} else {
    const result = add(arg1, arg2);
    console.log(result);
<<<<<<< HEAD
}
=======
}
>>>>>>> 2c186b2b877209ab97c483ff71065f642a284d14
