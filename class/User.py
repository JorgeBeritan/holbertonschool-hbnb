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