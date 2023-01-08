from threading import Event
from enum import Enum

class CommType(Enum):
    PROXY=0,
    pass

class Message():
    pass

class CEvent(Event):
    def set(self,message:Message):
        self.message=message
    pass

class PEvent(Event):
    
    def set(self,index):
        self.index=index
        pass
    pass
