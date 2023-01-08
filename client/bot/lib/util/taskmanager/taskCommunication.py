from threading import Event
from enum import Enum

class CommType(Enum):
    PROXY=0,
    pass

class Message():
    pass


class PEvent(Event):
    
    def set(self,index):
        self.index=index
        pass
    pass
