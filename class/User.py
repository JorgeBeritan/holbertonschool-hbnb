#!/usr/bin/python3
"""
definimos las clases
"""
import uuid
from validator import validator_email

class User():
    number_of_instance = 0
    __emails = set()

    def __init__(self, email, First_name, Last_name):
        self.ID = uuid.uuid4()
        self.email = email
        self.First_name = First_name
        self.Last_name = Last_name
        User.number_of_instance += 1
        #self.Create_at = Create_at
        #self.Update_at = Update_at

    @property
    def ID(self):
        return self.__ID
    
    @property
    def email(self):
        return self.__email
    
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
    
    @email.setter
    def email(self, email):
        if type(email) is not str:
            raise TypeError("The email user must be a string")
        if not validator_email(email):
            raise ValueError("The email is not valid")
        if email in self.__emails:
            raise ValueError("Email is already exist")
        self.__emails.add(email)
        self.__email = email

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
