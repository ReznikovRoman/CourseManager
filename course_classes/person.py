from course_classes.address import Address
from datetime import date


class Person:
    def __init__(self, first_name, last_name, phone, date_of_birth: date, address):
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._date_of_birth = date_of_birth
        self._address = address

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_full_name(self):
        return f"{self._last_name} {self._first_name}"

    def get_phone(self):
        return self._phone

    def get_age(self):
        today = date.today()
        born = self._date_of_birth
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def get_address(self):
        return self._address











