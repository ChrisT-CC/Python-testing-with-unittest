import unittest
from evens import even_number_of_evens


# create a test case
# to make use of Unittest's functionality, our class needs to inherit from the
# unittest.TestCase class
class TestEvens(unittest.TestCase):
    # Python is expecting an indented block after the use of a colon
    # when you have no code using the pass statement is valid and allows your
    # code to run error free
    pass
    # write a test to check everything works and our setup is correct
    # def test_function_returns_True(self):
        # create one or many asserts
        # self.assertTrue(even_number_of_evens([]))



# add a pass statement and unittest.main. So we can run the file without
# specifying the unit test module
if __name__ == "__main__":
    unittest.main()
