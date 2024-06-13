#!/usr/bin/pyhon3
import uuid

class Amenities:
    def __init__(self, amenities):
        self.__amenities = amenities
    
    @property
    def amenities(self):
        return self.__amenities

    @amenities.setter
    def amenities(self, amenities):
        if type(amenities) is not list:
            raise TypeError("Amenities must be a list")
        self.__amenities = amenities
    
    def append_amenities(self, amenity):
        if amenity in self.amenities:
            raise ValueError("amenity exist")
        self.amenities.append(amenity)

class amenity(Amenities):
    def __init__(self, name):
            self.__id = uuid.uuid4()
            self.name = name
        
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
        
    @id.setter
    def id(self):
        self.__id = self.id
        
    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise TypeError("amenity name must be a string")
        elif name == "":
            raise ValueError("amenity name is requerid")
        self.__name = name


# Example usage
a1 = Amenities(["Wi-fi", "Ducha", "Piscina", "Cocina"])
a_1 = amenity("Playa")
print(a1.amenities)
a1.append_amenities(a_1.name)
print(a1.amenities)