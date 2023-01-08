from threading import Event,BoundedSemaphore,Thread
from enum import Enum

class CommType(Enum):
    PROXY=0,
    pass

class Message():
    pass

class CEvent(Event):
    def __init__(self,index) -> None:
        super().__init__()
        self.index=index
    
    def set(self,message:Message):
        self.message=message
    pass

class PEvent(Event):
    
    def set(self,index,commType:CommType):
        self.index=index
        pass
    pass
