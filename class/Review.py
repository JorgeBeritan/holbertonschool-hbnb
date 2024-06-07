#!/usr/bin/python3
"""
definimos las clases
"""


class Review():
    def __init__(self, Review, Place_id, User_id, Rating, Comment, Create_at, Update_at):
        self.Review = Review
        self.Place_id = Place_id
        self.User_id = User_id
        self.Rating = Rating
        self.Comment = Comment
        self.Create_at = Create_at
        self.Update_at = Update_at
    
    @property
    def Review(self):
        return self.Review
    
    @property
    def Place_id(self):
        return self.Place_id
    
    @property
    def User_id(self):
        return self.User_id
    
    @property
    def Rating(self):
        return self.Rating
    
    @property
    def Comment(self):
        return self.Comment
    
    @property
    def create_at(self):
        return self.__create_at
    
    @property
    def update_at(self):
        return self.__update_at
