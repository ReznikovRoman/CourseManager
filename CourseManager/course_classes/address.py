

class Address:
    """
    Address of a Person

    Args:
        city (str): Is used to determine a city
        street (str): Is used to determine an address
        zip (str): Is used to determine a zip code

    Attributes:
        __city (str): Stores a ity
        __street (str): Stores a street
        __zip (str): Stores a code
    """
    def __init__(self, city, street, zip=None):
        self.__city = city
        self.__street = street
        self.__zip = zip

    def get_city(self):
        """
        Returns:
            __city
        """
        return self.__city

    def get_street(self):
        """
        Returns:
            __street
        """
        return self.__street

    def get_zip(self):
        """
        Returns:
            __zip
        """
        return self.__zip

    def print_address(self):
        """

        Returns:
            An address in a human-readable format
        """
        return f"City: {self.__city};  Street: {self.__street};  Zip Code: {self.__zip}"



