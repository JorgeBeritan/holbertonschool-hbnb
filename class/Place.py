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

    @id.setter
    def id(self):
        pass

    @host_id.setter
    def host_id(self):
        pass

    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise TypeError("Name must be a string")
        elif name == None:
            raise ValueError("Name is requerid")
        self.__name = name
    
    @description.setter
    def description(self, description):
        if type(description) is not str:
            raise TypeError("Description must be a string")
        if description == None:
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
    
    @max_gues.setter
    def max_guest(self, max_guest):
        if type(max_guest) is not int:
            raise TypeError("Max guest must be an integer")
        if max_guest < 0:
            raise ValueError("Max Guest must be a positive number")
        self.__max_guest = max_guest

    @price_per_night.setter
    def price_per_night(self, price_per_night):
        if type(price_per_night) is not int:
            raise TypeError("Price per night must be an integer")
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
    def city_id(self, city_id):
        pass
    @amenity_id.setter
    def amenity_id(self, amenity_id):
        pass