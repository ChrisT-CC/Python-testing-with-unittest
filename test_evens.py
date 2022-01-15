""" test file """
import unittest
from evens import even_number_of_evens


# create a test case
class TestEvens(unittest.TestCase):
    """
    to make use of Unittest's functionality, our class needs to inherit from
    the unittest.TestCase class
    """
    def test_throws_error_if_value_in_is_not_list(self):
        """
        1st test TypeError raised if a list is not passed into the function
        """
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        """
        2nd test returns False if an empty list is passed in
        """
        self.assertEqual(even_number_of_evens([]), False)


# add a pass statement and unittest.main. So we can run the file without
# specifying the unit test module
if __name__ == "__main__":
    unittest.main()
