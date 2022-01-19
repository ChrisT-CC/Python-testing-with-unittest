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

        # test to see if alert_santa() method returns the expected output
        self.assertTrue(student.naughty_list)

    def test_email(self):
        """ 3rd test """
        # create an instance of the student class
        student = Student("John", "Doe")

        # test to see if email() method returns the expected output
        self.assertEqual(student.email, "john.doe@email.com")


if __name__ == "__main__":
    unittest.main()
