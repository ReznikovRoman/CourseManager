from course_classes.address import Address
from datetime import date


class Person:
    def __init__(self, first_name, last_name, phone, date_of_birth: date, address):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__date_of_birth = date_of_birth
        self.__address = address

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_full_name(self):
        return f"{self.__last_name} {self.__first_name}"

    def get_phone(self):
        return self.__phone

    def get_age(self):
        today = date.today()
        born = self.__date_of_birth
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def get_address(self):
        return self.__address











