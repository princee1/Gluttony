from requestable_interface import Requestable,RequestState
#from threading import BoundedSemaphore,Thread
from taskCommunication import *
from time import sleep

MAX_ALIVE_TRHEAD=50
N=1
commSem=BoundedSemaphore(N)
manEvent = PEvent()


class Task(Thread):
    def __init__(self,request:Requestable,index:int,semOut,semData,cEvent):
        super().__init__(None,daemon=False)
        self.request = request
        self.index=index
        self.semOut=semOut
        self.semData=semData
        self.cEvent:CEvent=cEvent
        self.isDone=False
        
    def  run(self):
        
        while self.request.state != RequestState.DONE or self.request.state != RequestState.ERROR:
            
            if self.request.state == RequestState.INIT:
                pass
            
            elif self.request.state == RequestState.AUTHENTICATED:
                pass
            
            elif self.request.state == RequestState.SUCCESS:
                pass
            
            elif self.request.state == RequestState.READY:
                pass
            
            elif self.request.state == RequestState.PAUSE:
                pass
            
            elif self.request.state == RequestState.PROXY_ERROR:
                pass
            
            self.end()
            pass
        
        pass
    
    def end(self):
        self.isDone=True
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
        self.threadComm=Thread(target=self.communicate)
    
    
    def start(self):  
        self.threadComm.start()
        
        for t in self.taskList:
            t.start()
        
        self.waitThreads()    
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
        while True: #NOTE when all thread are done
            manEvent.wait()
            mess=manEvent.commMessage
            self.treatComm(mess)
            manEvent.clear()
            commSem.release(N)
        pass
    
    def treatComm(self,mess:CommMessage):
        """
        It takes a commMessage, treats it, and then sets the event that was waiting for it
        
        :param index: the index of the event in the eventList
        """
        if False:
            if cm.type==CommType.PROXY:
                pass
            elif cm.type==CommType.PROXY_FLAG: 
                pass
            #treating the commMessage
            pass 
        self.eventList[mess.index].set(Message())
        pass
    
    def flagProcess(self):
        pass
    
    def checkIsDone(self)->bool:
        raise NotImplementedError()
        complete=True
        
        for t in self.taskList:
            if t.isDone !=True:
                complete=False
                return complete
        
        return complete
    
    def stats(self):
        pass
    
    pass

