#!/usr/bin/python3
"""
definimos las clases
"""
import uuid

class User():
    def __init__(self, Email, First_name, Last_name):
        self.ID = uuid.uuid4()
        self.Email = Email
        self.First_name = First_name
        self.Last_name = Last_name
        #self.Create_at = Create_at
        #self.Update_at = Update_at

    @property
    def ID(self):
        return self.__ID
    
    @property
    def Email(self):
        return self.__Email
    
    @property
    def First_name(self):
        return self.__First_name
    
    @property
    def Last_name(self):
        return self.__Last_name
    
    @property
    def create_at(self):
        return self.__create_at
    
    @property
    def update_at(self):
        return self.__update_at
    
    @ID.setter
    def ID(self, ID):
        self.__ID = ID
    
    @Email.setter
    def Email(self, Email):
        if type(Email) is not str:
            raise TypeError("The email user must be a string")
        self.__Email = Email


    @First_name.setter
    def First_name(self, First_name):
        if type(First_name) is not str:
            raise TypeError("First name must be a string")
        elif First_name == "":
            raise ValueError("First name is requerid")
        self.__First_name = First_name

    @Last_name.setter
    def Last_name(self, Last_name):
        if type(Last_name) is not str:
            raise TypeError("Last name must be a string")
        elif Last_name == "":
            raise ValueError("Last name is requerid")
        self.__Last_name = Last_name