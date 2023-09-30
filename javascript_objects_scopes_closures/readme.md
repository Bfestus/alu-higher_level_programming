# Javascript objects, closures and scopes 

## Objects:
In JavaScript, an object is a collection of key-value pairs. Think of it like a real-world object that has properties. For example, a car object could have properties like color, model, and year. Here's how you create an object:
```
let car = {
    color: 'red',
    model: 'sedan',
    year: 2020
};
```

## Scopes:
In JavaScript, scope refers to the context in which variables are declared. There are two types of scope: global scope and local scope.

### Global Scope: 
Variables declared outside any function or block have global scope, meaning they can be accessed from anywhere in your code.
###Local Scope: 
Variables declared inside a function have local scope, meaning they can only be accessed within that function.


##Closures:
A closure is a function that remembers the scope in which it was created. This allows the function to access and manipulate variables from its outer scope even after that outer function has finished executing. Closures are powerful and are commonly used for data encapsulation and creating private variables in JavaScript

writtn by programmer: Festus
