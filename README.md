# Python testing with Unittest

Python provides us with a batteries-included  test module that is part of the Python standard library. This testing framework  is called Unittest.

---

## Building tests in Python

### Project overview

To learn about the  Unittest testing framework and to see how tests run successfully we are going to write a function. 

This function accepts a list of numbers and returns true if the list contains an even number of even numbers. 

It should also raise a TypeError if anything  other than a list is passed into the function.

---

### Suggested tests

1. Our function should raise a "TypeError" with an error message if a list isn't passed in as an argument.
1. It should return False when numbers is empty
1. It should return False when the number of even numbers is odd
1. It should return False when the number of even numbers is 0
1. It should return True if the number of even numbers is even

---

### Set up files

- create `evens.py` file to build the function
- create `test_evens.py` file to write the tests

Unittest requires that our test  filename starts with the word "test", followed by an underscore and a descriptive name of what we're testing.

---

### Create the test case

- import unittest
- create class `TestEvens(unittest.TestCase)` - To make use of Unittest's functionality, the class needs to inherit from the unittest.TestCase class
- add a pass statement and unittest.main, so we can run the file without specifying the unit test module
- in `evens.py` create the function `even_number_of_evens()` and call it in a `print()` method with arg "5"

---

### Start testing

- create a basic test to check the setup
- import the function from `evens.py`
- create a method that starts wit the word "test" and arg "self"
- create either a single assert or many asserts
- run the test to see if it fails
- in `evens.py` modify code to pass the test
- create 1st test to check if TypeError is raised if a list is not passed into the function and write the code to pass the test
- create 2nd test to return False if an empty list is passed in and write the code to pass the test
- create 3rd test to return True if number of even numbers is even and write the code to pass the test
- create 4th test to fail if only one even number is passed in and write the code to pass the test
- create 5th test to fail if odd numbers in list and write the code to pass the test
- refactoring the code
    - remove if/else statement
    - replace the for-loop with a list comprehension
    - convert the if/else statement into a conditional expression

*__Important__*
- *Python is expecting  an indented block after the use of a colon, so when you have no code using the pass statement  is valid and allows your code to run error free*
- *when Python runs a file directly, it names it `__main__`*

--- 