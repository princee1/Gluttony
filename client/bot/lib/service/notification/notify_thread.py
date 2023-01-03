from win10toast import ToastNotifier
from threading import Event,Thread,Semaphore
from time import sleep


# It's the duration of the toast notification.
DURATION = 2
WAITING = DURATION + 1

N_SEM=1
TIMEOUT:int

# It's declaring the variables e and t as global variables.
global e,t,s

class NotifyThread(Thread):
    """
    It's a thread that waits for a signal to show a toast notification
    """
    MAX_TOBESHOWED=5
    
    def __init__(self) -> None:
        super().__init__()
        self.title=None
        self.message=None
        self.active=True
        self.listNotif=[]
        
    def run(self) -> None:
        self.privatenotify()
    
    def addNotify(self,title,message):
        self.listNotif.append((title,message))

    def killThread(self):
        """
        The function sets the event e to true, which causes the thread to exit the while loop and end
        the thread
        """
        self.active=False
        e.set()
    
    def privatenotify(self):
        """
        It waits for an event to be set, then it shows a toast notification, then it clears the event.
        """
        while self.active:
            try:
                e.wait(TIMEOUT)
                if self.active:
                    s.acquire()
                    tempList=self.notifDataToBeShowed()
                    s.release()
                    self.showNotif(tempList)                    
                e.clear()
            except:
                pass

    def notifDataToBeShowed(self):
        tempList:list
        iteration:int
        n=len(self.listNotif)
        if n==0:
            return []
        if NotifyThread.MAX_TOBESHOWED > n:
            iteration=  n-NotifyThread.MAX_TOBESHOWED  
        else:
            iteration= -1
             
        for i in range(n-1,iteration,-1):
            tempList.append((self.listNotif.pop(i)))
            
        return tempList

    def showNotif(self,tempList):
        for title,message in tempList:
            test = ToastNotifier()
            test.show_toast(title=title,msg=message,threaded=True)
            del test
            sleep(DURATION + 2)
        
    
    pass

def notify(title,message):
    """
    It sets the title and message of the notification, and then sets the event
    
    :param title: The title of the notification
    :param message: The message to be displayed
    """
    s.acquire()    
    t.addNotify(title,message)
    s.release
    if e.isSet():
        e.set()
    

e=Event()
s=Semaphore(N_SEM)
t=NotifyThread()
t.start()




