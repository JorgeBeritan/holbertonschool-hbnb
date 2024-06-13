#!/usr/bin/python3
"""
definimos las clases
"""
import uuid

class Review:

    def __init__(self, place_id, user_id, rating, comment):
        self.review = uuid.uuid4()
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        #self.create_at = datetime.now()
        #self.update_at = datetime.now()


    @property
    def review(self):
        return self.__review
    
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

    @review.setter
    def review(self, value):
        if type(value) is not uuid.UUID:
            raise TypeError("The review ID must be a type uuid.UUID")

        self.__review = value

    @place_id.setter
    def place_id(self, value):
        if type(value) is not uuid.UUID:
            raise TypeError("The type of place_id must be a uuid.UUID")

        self.__place_id = value
    
    @user_id.setter
    def user_id(self, value):
        if type(value) is not uuid.UUID:
            raise TypeError("The type of user_id must be a uuid.UUID")
    
        self.__user_id = value

    @rating.setter
    def rating(self, value):
        if type(value) is not int:
            raise TypeError("The rating must be a int")
        if value != range(10):
            raise ValueError("The rating of a place is from 0 to 10")

        self.__rating = value

    @comment.setter
    def comment(self, value):
        if type(value) is not str:
            raise TypeError("The comment must be a string")
        self.__comment = value






