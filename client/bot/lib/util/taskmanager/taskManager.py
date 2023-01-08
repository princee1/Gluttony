from requestable_interface import Requestable,RequestState
from threading import Semaphore,BoundedSemaphore,Thread,Event


MAX_ALIVE_TRHEAD=50
N=1
commSem=BoundedSemaphore(N)


class Task(Thread):
    def __init__(self,request:Requestable,index:int,semOut,semData):
        super().__init__(self,daemon=False)
        self.request = request
        self.index=index
        self.semOut=semOut
        self.semData=semData
        
    def  run(self):
        
        while self.request.state != RequestState.DONE or self.request.state != RequestState.ERROR:
            
            if self.request.state == RequestState.INIT:
                pass
            elif self.request.state == RequestState.AUTHENTICATED:
                pass
            elif self.request.state == RequestState.PROXY_ERROR:
                pass
            elif self.request.state == RequestState.SUCCESS:
                pass
            elif self.request.state == RequestState.PAUSE:
                pass
            
            pass
        
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
    
    def waitThreads(self):
        for t in self.taskList:
            t.join()
        
        pass
    
    def communicate(self):
        pass
    
    pass
