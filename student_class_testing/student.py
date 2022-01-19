""" Student file """
# import "date" and "timedelta" methods from the datetime module, to allow us
# to define start and end dates
from datetime import date, timedelta
import requests


class Student:
    """ A student class as base for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    # add the @property decorator since this is a method to get data only
    @property
    def full_name(self):
        """
        a read-only method to get more detailed information about a student
        such as the student's full name
        """
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        """
        a method to modify the naughty_list property
        """
        self.naughty_list = True

    @property
    def email(self):
        """
        a read-only method to return a student's email
        """
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def apply_extension(self, days):
        """ a method to modify the end_date by '10' """
        self.end_date = self.end_date + timedelta(days=days)

    def course_schedule(self):
        """ a method to mock a fictional API call """
        response = requests.get(
            f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"
