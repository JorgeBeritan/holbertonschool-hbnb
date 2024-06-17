#!/usr/bin/python3
import uuid
class Amenity:

    def __init__(self, name):
        self.__id = str(uuid.uuid4())
        self.name = name

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        if type(value) is not str:
            raise TypeError("Must be a string")
        self.__id = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise TypeError("Name must be a string")
        if name == "":
            raise ValueError("Name is required")
        
        self.__name = name