""" Student file """
# import "date" and "timedelta" methods from the datetime module, to allow us
# to define start and end dates
from datetime import date, timedelta


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
        self.naughty_list = True
