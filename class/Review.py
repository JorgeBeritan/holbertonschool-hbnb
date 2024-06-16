#!/usr/bin/python3
"""
definimos las clases
"""
import uuid

class Review:

    def __init__(self, place_id, user_id, rating, comment):
        self.__id = str(uuid.uuid4())
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        #self.create_at = datetime.now()
        #self.update_at = datetime.now()


    @property
    def id(self):
        return self.__id
    
    @property
    def place_id(self):
        return self.__place_id

    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def rating(self):
        return self.__rating
    
    @property
    def comment(self):
        return self.__comment

    @id.setter
    def id(self, value):
        if type(value) is not str:
            raise TypeError("The review ID must be a type string")

        self.__id = value

    @place_id.setter
    def place_id(self, value):
        if type(value) is not str:
            raise TypeError("The type of place_id must be a string")

        self.__place_id = value
    
    @user_id.setter
    def user_id(self, value):
        if type(value) is not str:
            raise TypeError("The type of user_id must be a string")
    
        self.__user_id = value

    @rating.setter
    def rating(self, value):
        if type(value) is not int:
            raise TypeError("The rating must be a int")
        if value not in range(1, 5):
            raise ValueError("The rating of a place is from 0 to 5")

        self.__rating = value

    @comment.setter
    def comment(self, value):
        if type(value) is not str:
            raise TypeError("The comment must be a string")
        self.__comment = value
