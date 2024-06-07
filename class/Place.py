#!/usr/bin/python3

class Place:


    def __init__(self, id, host_id, name, description, number_of_rooms, number_of_bathrooms, max_guest, price_per_night, latitude, longitude, city_id, amenity_id):
        self.id = id
        self.host_id = host_id
        self.name = name
        self.description = description
        self.numbert_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guest = max_guest
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = city_id
        self.amenity_id = amenity_id
        self.create_at = "2024-05-10"
        self.update_at = "2024-05-19"

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
    def max_gues(self):
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