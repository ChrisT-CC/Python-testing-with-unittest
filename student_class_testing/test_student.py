""" Test file for student.py """
import unittest
from datetime import timedelta
from unittest.mock import patch
from student import Student


class TestStudent(unittest.TestCase):
    """ Test case """

    # @classmethod
    # def setUpClass(cls):
    #     print("setUpClass")

    # @classmethod
    # def tearDownClass(cls):
    #     print("tearDownClass")

    def setUp(self):
        """ create the setUp method """
        print("setUp")
        # create an instance of the student class
        self.student = Student("John", "Doe")

    # def tearDown(self):
    #     """ create the setUp method """
    #     print("tearDown")

    def test_full_name(self):
        """ 1st test """
        print("full_name")
        # test the student instance to see if calling the full_name method
        # returns the expected value
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        """ 2nd test """
        print("alert_santa")
        # call alert_santa() method
        self.student.alert_santa()

        # test to see if alert_santa() method returns the expected output
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        """ 3rd test """
        print("email")
        # test to see if email() method returns the expected output
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_apply_extension(self):
        """ 4th test """
        print("apply_extension")
        # test if apply_extension() method adds "days" to end_date
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(
            self.student.end_date, old_end_date + timedelta(days=5))

    # create a test for a successful request
    def test_course_schedule_success(self):
        """ mocking a call to fictional API - success test"""
        print("course_schedule_success")
        # set context manager
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    # create a test for a failed request
    def test_course_schedule_failed(self):
        """ mocking a call to fictional API - fail test"""
        print("course_schedule_failed")
        # set context manager
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(
                schedule, "Something went wrong with the request!")


if __name__ == "__main__":
    unittest.main()
