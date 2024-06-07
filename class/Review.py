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