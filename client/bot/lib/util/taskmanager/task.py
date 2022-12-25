from requestable_interface import Requestable
from threading import Thread


class Task(Thread):
    def __init__(self,request:Requestable):
        super().__init__(self,daemon=False)
        self.request = request
        
    def  run(self):
        pass
    
    def end(self):
        pass
    
    def __repr__(self) -> str:
        return super().__repr__()

    
    pass