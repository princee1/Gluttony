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
        self.message=None
    
    def set(self,message:Message):
        super().set()
        self.message=message
    pass

class PEvent(Event):
    
    def __init__(self):
        super().__init__()
        self.commType=None
    
    def set(self,index,commType:CommType):
        super().set()
        self.index=index
        self.commType = commType
        pass
    pass
