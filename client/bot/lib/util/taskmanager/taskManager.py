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
        """
        The function waits for an availability from the manager, then sends a message to the manager, then
        waits for a response from the manager, then returns the response
        
        :param commMessage: This is the message that the manager is sending to the worker
        :type commMessage: CommMessage
        :return: The message that was sent to the manager.
        """
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
        """
        It waits for all the threads to finish before continuing
        """
        for t in self.taskList:
            t.join()
        
        pass
    
    def communicate(self):
        """
        The function waits for the event to be set, then it gets the index of the event, treats the
        communication, clears the event and releases the semaphore
        """
        
        manEvent.wait()
        index=manEvent.index
        self.treatComm(index)
        manEvent.clear()
        commSem.release(N)
        pass
    
    def treatComm(self,index):
        """
        It takes a commMessage, treats it, and then sets the event that was waiting for it
        
        :param index: the index of the event in the eventList
        """

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

