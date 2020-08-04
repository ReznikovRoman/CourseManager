

class Address:
    """ Address of a Person """
    def __init__(self, city, street, zip=None):
        self.__city = city
        self.__street = street
        self.__zip = zip

    def get_city(self):
        return self.__city

    def get_street(self):
        return self.__street

    def get_zip(self):
        return self.__zip

    def print_address(self):
        return f"City: {self.__city};  Street: {self.__street};  Zip Code: {self.__zip}"



