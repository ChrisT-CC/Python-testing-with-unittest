import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """ Test case """

    def test_full_name(self):
        """ 1st test """
        # create an instance of the student class
        student = Student("John", "Doe")

        # test the student instance to see if calling the full_name method
        # returns the expected value
        self.assertEqual(student.full_name, "John Doe")

    def test_alert_santa(self):
        """ 2nd test """
        # create an instance of the student class
        student = Student("John", "Doe")
        # call alert_santa() method
        student.alert_santa()

        self.assertTrue(student.naughty_list)


if __name__ == "__main__":
    unittest.main()
