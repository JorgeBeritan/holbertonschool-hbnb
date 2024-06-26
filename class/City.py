#!/usr/bin/python3
from datetime import datetime
import uuid
"""
definimos las clases
"""


class City():
    def __init__(self, Name, Country_code):
        self.__id = str(uuid.uuid4())
        self.Name = Name
        self.Country_code = Country_code 
        self.Create_at = datetime.now()
        self.Update_at = datetime.now()
    
    @property
    def id(self):
        return self.__id
    
    @property
    def Name(self):
        return self.__Name
    
    @property
    def Country_code(self):
        return self.__Country_code
    
    @property
    def create_at(self):
        return self.__create_at
    
    @property
    def update_at(self):
        return self.__update_at
    
    @id.setter
    def id(self, id):
        if type(id) is not str:
            raise TypeError("The ID must be a string")
        self.__id = id
    
    @Name.setter
    def Name(self, Name):
        if type(Name) is not str:
            raise TypeError("Name must be a string")
        elif Name is None:
            raise ValueError("Name is required")
        self.__Name = Name
    
    @Country_code.setter
    def Country_code(self, Country_code):
        if Country_code is None:
            raise ValueError("Country code is required")
        self.__Country_code = Country_code
    