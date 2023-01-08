from requestable_interface import Requestable,RequestState
#from threading import BoundedSemaphore,Thread
from taskCommunication import *


MAX_ALIVE_TRHEAD=50
N=1
commSem=BoundedSemaphore(N)
manEvent = PEvent()


class Task(Thread):
    def __init__(self,request:Requestable,index:int,semOut,semData,cEvent):
        super().__init__(self,daemon=False)
        self.request = request
        self.index=index
        self.semOut=semOut
        self.semData=semData
        self.cEvent:CEvent=cEvent
        
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
    
    def communicate(self,commMessage:CommMessage):
        commSem.acquire()
        manEvent.set(commMessage)
        self.cEvent.wait()
        message = self.cEvent.message
        self.cEvent.clear()
        return message
    
    def __repr__(self) -> str:
        return super().__repr__()

    
    pass

class TaskManager():
    
    def __init__(self,taskList,eventList):
        self.taskList:list[Task] = taskList
        self.eventList:list[Event]= eventList
        self.activeTaskList:list[Task]=[]
        self.thradComm=Thread(target=self.communicate)
    
    
    def start(self):
        pass
    
    def waitThreads(self):
        for t in self.taskList:
            t.join()
        
        pass
    
    def communicate(self):
        
        manEvent.wait()
        index=manEvent.index
        self.treatComm(index)
        manEvent.clear()
        commSem.release(N)
        pass
    
    def treatComm(self,index):

        with manEvent.commMessage as cm:
            if cm.type==CommType.PROXY:
                pass
            elif cm.type==CommType.PROXY_FLAG: 
                pass
            #treating the commMessage
            pass 
        self.eventList[index].set()
        pass
    
    def flagProcess():
        pass
    
    pass

