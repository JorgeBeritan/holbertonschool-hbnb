from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4

class BaseClass(ABC):

    def __init__(self):
        self.__id = uuid4()
        self.__create_at = datetime.now()
        self.__update_at = datetime.now()

    def set_time(func):
        def wrapper_set_time(self, *args, **kwargs):
            self.__update_at = datetime.now()
            return func(self, *args, **kwargs)
        return wrapper_set_time
