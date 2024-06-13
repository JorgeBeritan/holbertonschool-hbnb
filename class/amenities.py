#!/usr/bin/pyhon3


class Amenities:
    def __init__(self, amenities):
        self.__amenities = amenities
    
    @property
    def amenities(self):
        return self.__amenities

    @amenities.setter
    def amenities(self, amenities):
        if not isinstance(amenities, list):
            raise TypeError("Amenities must be a list")
        self.__amenities = amenities

    def append_amenities(self, amenity):
        if amenity in self.amenities:
            raise ValueError("amenity is inside the list")
        self.amenities.append(amenity)

# Example usage
a1 = Amenities(["Wi-fi", "Ducha", "Piscina", "Cocina"])
print(a1.amenities)
a1.append_amenities("TV")
print(a1.amenities)