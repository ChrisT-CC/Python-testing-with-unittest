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
        Create tests for a list
        """
        # 2nd test to return False if an empty list is passed in
        self.assertEqual(even_number_of_evens([]), False)
        # 3rd test to return True if number of even numbers is even
        self.assertEqual(even_number_of_evens([2, 4]), True)
        # 4th test to fail if only one even number is passed in
        self.assertEqual(even_number_of_evens([2]), False)
        # 5th test to fail if odd numbers in list
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


# add a pass statement and unittest.main. So we can run the file without
# specifying the unit test module
if __name__ == "__main__":
    unittest.main()
