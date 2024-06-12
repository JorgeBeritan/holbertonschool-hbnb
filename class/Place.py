#!/usr/bin/python3


from datetime import datetime
import uuid
from User import User
class Place:


    def __init__(self, name, description, number_of_rooms, number_of_bathrooms, max_guest, price_per_night, latitude, longitude, host_id, city_id):
        self.__id = uuid.uuid4()
        self.__host_id = host_id
        self.name = name
        self.description = description
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guest = max_guest
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = city_id
        self.amenity_id = uuid.uuid4()
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    @property
    def id(self):
        return self.__id
    
    @property
    def host_id(self):
        return self.__host_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    
    @property
    def number_of_rooms(self):
        return self.__number_of_rooms

    @property
    def number_of_bathrooms(self):
        return self.__number_of_bathrooms
    
    @property
    def max_guest(self):
        return self.__max_guest

    @property
    def price_per_night(self):
        return self.__price_per_night
    
    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude
    
    @property
    def city_id(self):
        return self.__city_id
    
    @property
    def amenity_id(self):
        return self.__amenity_id
    
    @property
    def create_at(self):
        return self.__create_at
    
    @property
    def update_at(self):
        return self.__update_at

    @id.setter
    def id(self):
        self.__id = self.id

    @host_id.setter
    def host_id(self, host_id):
        if type(host_id) is not uuid.UUID:
            raise TypeError("Must be a unique host id")
        self.__host_id = host_id

    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise TypeError("Name must be a string")
        elif name == "":
            raise ValueError("Name is requerid")
        self.__name = name
    
    @description.setter
    def description(self, description):
        if type(description) is not str:
            raise TypeError("Description must be a string")
        if description == "":
            raise ValueError("Description is required")
        
        self.__description = description

    @number_of_rooms.setter
    def number_of_rooms(self, number_of_rooms):
        if type(number_of_rooms) is not int:
            raise TypeError("Number of rooms must be an integer")
        if number_of_rooms < 0:
            raise ValueError("Number of rooms must be >= 0")
        self.__number_of_rooms = number_of_rooms

    @number_of_bathrooms.setter
    def number_of_bathrooms(self, number_of_bathrooms):
        if type(number_of_bathrooms) is not int:
            raise TypeError("Nomber of rooms must be an integer")
        if number_of_bathrooms < 0:
            raise ValueError("Number of bathrooms must be >= 0")
        self.__number_of_bathrooms = number_of_bathrooms
    
    @max_guest.setter
    def max_guest(self, max_guest):
        if type(max_guest) is not int:
            raise TypeError("Max guest must be an integer")
        if max_guest < 0:
            raise ValueError("Max Guest must be a positive number")
        self.__max_guest = max_guest

    @price_per_night.setter
    def price_per_night(self, price_per_night):
        if type(price_per_night) is not float:
            raise TypeError("Price per night must be a float")
        if price_per_night < 0:
            raise ValueError("Price per night must be  a positive number")
        self.__price_per_night = price_per_night

    @latitude.setter
    def latitude(self, latitude):
        if type(latitude) is not float:
            raise TypeError("Latitude must be a float")
        self.__latitude = latitude
    
    @longitude.setter
    def longitude(self, longitude):
        if type(longitude) is not float:
            raise TypeError("Longitude must be float")
        self.__longitude = longitude
    
    @city_id.setter
    def city_id(self, value):
        if type(value) is not uuid.UUID:
            raise TypeError("The id must be a uuid.UUID")
        self.__city_id = value
    @amenity_id.setter
    def amenity_id(self, value):
        self.__amenity_id = value

    @create_at.setter
    def create_at(self, value):
        self.__create_at = value

    @update_at.setter
    def update_at(self, value):
        self.__update_at = value
