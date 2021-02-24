from CourseManager.course_classes.address import Address
from datetime import date


class Person:
    """
    Represents a Person

    Args:
        first_name (str): Is used to determine a first name of a Person
        last_name (str): Is used to determine a last name of a Person
        phone (str): Is used to determine a phone number of a Person
        date_of_birth (datetime.date): Is used to determine a date of birth of a Person
        address (Address): Is used to determine an Address of a Person

    Attributes:
        __first_name (str): Stores first_name
        __last_name (str): Stores last_name
        __phone (str): Stores phone
        __date_of_birth (datetime.date): Stores date_of_birth
        __address (Address): Stores address

    """
    def __init__(self, first_name, last_name, phone, date_of_birth: date, address):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__date_of_birth = date_of_birth
        self.__address = address

    def get_first_name(self):
        """
        Returns:
            __first_name
        """
        return self.__first_name

    def get_last_name(self):
        """
        Returns:
            __last_name
        """
        return self.__last_name

    def get_full_name(self):
        """

        Returns:
            Full name of a Person (last name + first name)
        """
        return f"{self.__last_name} {self.__first_name}"

    def get_phone(self):
        """
        Returns:
            __phone
        """
        return self.__phone

    def get_age(self):
        """

        Returns:
            Age of a Person
        """
        today = date.today()
        born = self.__date_of_birth
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def get_address(self):
        """
        Returns:
            __address
        """
        return self.__address











