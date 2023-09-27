#!/usr/bin/node
function computeFactorial(n) {
    // Base case: If n is NaN or less than 0, return 1
    if (isNaN(n) || n < 0) {
      return 1;
    }
    
    // Base case: If n is 0, return 1 (0! = 1)
    if (n === 0) {
      return 1;
    }
  
    // Recursive case: Compute the factorial by multiplying n with factorial of (n-1)
    return n * computeFactorial(n - 1);
  }
  
  // Check if the script is called with the correct number of arguments
  if (process.argv.length !== 3) {
    console.log("Usage: node factorial.js <integer>");
    process.exit(1);
  }
  
  // Parse the integer argument from the command line
  const input = parseInt(process.argv[2]);
  
  // Call the computeFactorial function and print the result
  const factorial = computeFactorial(input);
  console.log(`Factorial of ${input} is ${factorial}`);
