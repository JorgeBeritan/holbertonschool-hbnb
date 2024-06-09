#!/usr/bin/python3
"""
definimos las clases
"""


class City():
    def __init__(self, ID, Name, Country_code, Create_at, Update_at):
        self.ID = ID
        self.Name = Name
        self.Country_code = Country_code 
        self.Create_at = Create_at
        self.Update_at = Update_at
    
    @property
    def ID(self):
        return self.ID
    
    @property
    def Name(self):
        return self.Name
    
    @property
    def Country_code(self):
        return self.Country_code
    
    @property
    def create_at(self):
        return self.__create_at
    
    @property
    def update_at(self):
        return self.__update_at
    
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
    