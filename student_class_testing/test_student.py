import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """ Test case """

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        """ create the setUp method """
        print("setUp")
        # create an instance of the student class
        self.student = Student("John", "Doe")

    def tearDown(self):
        """ create the setUp method """
        print("tearDown")

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


if __name__ == "__main__":
    unittest.main()
