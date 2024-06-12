#!/usr/bin/python3
import pycountry

class Country:

    def __init__(self, code):
        self.code = code
        self.name = pycountry.countries.get(alpha_2=code)

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name
    
    @code.setter
    def code(self, code):
        if len(code) != 2:
            raise ValueError("Country code must be 2 characters long")
        if pycountry.countries.get(alpha_2=code) is None:
            raise ValueError("Invalid Country Code")
        self.__code = code

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Country name cannot be None")
        self.__name = name
