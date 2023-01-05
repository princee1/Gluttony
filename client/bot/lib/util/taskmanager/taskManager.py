from requestable_interface import Requestable
from threading import Semaphore,BoundedSemaphore,Thread,Event


MAX_ALIVE_TRHEAD=50
N=1

class Task(Thread):
    def __init__(self,request:Requestable,index:int,semOut,semData):
        super().__init__(self,daemon=False)
        self.request = request
        self.index=index
        self.semOut=semOut
        self.semData=semData
        
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

class TaskManager():
    
    def __init__(self,taskList):
        self.taskList:list[Task] = taskList
        self.eventList:list[Event]= []
        self.thradComm=Thread(target=self.communicate)
    
    def start(self):
        pass
    
    def waitThread(self):
        pass
    
    def communicate(self):
        pass
    
    pass
