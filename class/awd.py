from uuid import uuid4
from datetime import datetime, date
class PEP:

    def __init__(self, cosas):
        self.last_accessed = datetime.now()
        self.cosas = cosas

    def set_time(func):
        def wrapper_set_time(self, *args, **kwargs):
            self.last_accessed = datetime.now()
            return func(self, *args, **kwargs)
        return wrapper_set_time
    
    @set_time
    def change_cosas(self):
        self.cosas = 32

p1 = PEP(21)
print(p1.last_accessed)
p1.change_cosas()
print(p1.last_accessed)
