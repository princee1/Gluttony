from threading import Event,BoundedSemaphore,Thread
from enum import Enum

class CommType(Enum):
    PROXY=0,
    PROXY_FLAG=1
    pass

class CommMessage():
    def __init__(self,index,commType,params=None) -> None:
        self.index = index
        self.commType = commType
        self.params=params
        pass
    pass
class Message():
    def __init__(self,value) -> None:
        self.value=value
        pass
    
    def __repr__(self) -> str:
        return self.value
    pass


class CEvent(Event):
    """The CEvent class is a subclass of the Event class. It has an index and a message. The index is used
to identify the event. The message is used to pass data to the event handler
    """
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
        self.commMessage:CommMessage=None
    
    def set(self,commMessage):
        super().set()
        self.commMessage = commMessage
        pass
    pass
