#!/usr/bin/python3
import uuid
from persistneceABC import IPersistenceManager


class DataManager(IPersistenceManager):
    def __init__(self):
        self.__data = {}
    
    def save(self, entity):
        entity_type = type(entity).__name__
        entity_id = entity.id
        if entity_type not in self.__data:
            self.__data[entity_type] = {}
        elif entity_id in self.__data[entity_type]:
            raise ValueError("{} entity id already exist".format(entity_id))
        self.__data[entity_type][entity_id] = entity
    
    def get(self, entity_id, entity_type):
        if entity_type not in self.__data:
            raise ValueError("{} entity type not found".format(entity_type))
        if entity_id not in self.__data[entity_type]:
            raise ValueError("{} entity id not found".format(entity_id))
        return self.__data[entity_type][entity_id]
        
    
    def update(self, entity):
        entity_type = type(entity).__name__
        entity_id = entity.id
        if entity_type in self.__data:
            if entity_id in self.__data[entity_type]:
                self.__data[entity_type][entity_id] = entity
    
    def delete(self, entity_id, entity_type):
        if entity_type in self.__data:
            if entity_id in self.__data[entity_type]:
                del self.__data[entity_type][entity_id]
