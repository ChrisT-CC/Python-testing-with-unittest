# Python testing with Unittest

Python provides us with a batteries-included  test module that is part of the Python standard library. This testing framework  is called Unittest.

---

## Project overview

To learn about the  Unittest testing framework and to see how tests run successfully we are going to write a function. 

This function accepts a list of numbers and returns true if the list contains an even number of even numbers. 

It should also raise a TypeError if anything  other than a list is passed into the function.

---

## Suggested tests

1. Our function should raise a "TypeError" with an error message if a list isn't passed in as an argument.
1. It should return False when numbers is empty
1. It should return False when the number of even numbers is odd
1. It should return False when the number of even numbers is 0
1. It should return True if the number of even numbers is even

---

## Set up files

- create `evens.py` file to build the function
- create `test_evens.py` file to write the tests

Unittest requires that our test  filename starts with the word "test", followed by an underscore and a descriptive name of what we're testing.

---
