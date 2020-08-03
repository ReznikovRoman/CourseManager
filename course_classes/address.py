
class Address:
    """ Address of a Person """
    def __init__(self, city, street, zip=None):
        self._city = city
        self._street = street
        self._zip = zip

    def get_city(self):
        return self._city

    def get_street(self):
        return self._street

    def get_zip(self):
        return self._zip

    def print_address(self):
        return f"City: {self._city};  Street: {self._street};  Zip Code: {self._zip}"



