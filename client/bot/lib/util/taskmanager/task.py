from requestable_interface import Requestable
from threading import Thread



class Task(Thread):
    def __init__(self,request:Requestable,index:int,semOut,semData):
        super().__init__(self,daemon=False)
        self.request = request
        self.index=index
        
    def  run(self):
        pass
    
    def request(self):
        pass
    
    def end(self):
        pass
    
    def communicate(self):
        pass
    
    def __repr__(self) -> str:
        return super().__repr__()

    
    pass