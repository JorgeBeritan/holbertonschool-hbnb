#!/usr/bin/python3
"""
definimos las clases
"""


class User():
    def __init__(self, ID, Email, First_name, Last_name, Create_at, Update_at):
        self.ID = ID
        self.Email = Email
        self.First_name = First_name
        self.Last_name = Last_name
        self.Create_at = Create_at
        self.Update_at = Update_at

    @property
    def ID(self):
        return self.ID
    
    @property
    def Email(self):
        return self.Email
    
    @property
    def First_name(self):
        return self.First_name
    
    @property
    def Last_name(self):
        return self.Last_name
    
    @property
    def create_at(self):
        return self.__create_at
    
    @property
    def update_at(self):
        return self.__update_at
    
    @Email.setter
    def Email(self, Email):
        pass

    @First_name.setter
    def First_name(self, First_name):
        if type(First_name) is not str:
            raise TypeError("First name must be a string")
        elif First_name is None:
            raise ValueError("First name is requerid")
        self.__First_name = First_name

    @Last_name.setter
    def Last_name(self, Last_name):
        if type(Last_name) is not str:
            raise TypeError("Last name must be a string")
        elif Last_name is None:
            raise ValueError("Last name is requerid")
        self.__Last_name = Last_name