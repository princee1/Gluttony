from threading import Event,BoundedSemaphore,Thread
from enum import Enum

class CommType(Enum):
    PROXY=0,
    PROXY_FLAG=1
    pass

class CommMessage():
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
        self.commMessage=None
    
    def set(self,index,commMessage):
        super().set()
        self.index=index
        self.commMessage = commMessage
        pass
    pass
