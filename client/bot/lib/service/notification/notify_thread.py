from win10toast import ToastNotifier
from threading import Event,Thread,Semaphore
from time import sleep
from random import randint

# It's the duration of the toast notification.
DURATION = 2
WAITING = DURATION + 1

# It's the number of semaphores and the timeout period.
N_SEM=1
TIMEOUT= 5*WAITING 

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
        print(f"Notify Thread Activy: {self.active}")
        self.privatenotify()
    
    def addNotify(self,title,message):
        """
        It adds a notification to the list of notifications
        
        :param title: The title of the notification
        :param message: The message to be displayed
        """
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
        It waits for a timeout period, then checks if there are any notifications to be shown, and if there
        are, it shows them.
        """
        while self.active:
            try:
                e.wait(TIMEOUT)
                if self.active:
                    s.acquire()
                    tempList=self.notifDataToBeShowed()
                    s.release(N_SEM)
                    self.showNotif(tempList)                    
                e.clear()
            except:
                pass

    def notifDataToBeShowed(self):
        """
        It takes the last MAX_TOBESHOWED elements from the list and returns them
        :return: A list of tuples.
        """
        tempList=[]
        n=len(self.listNotif)
        if n==0:
            return tempList
        if NotifyThread.MAX_TOBESHOWED < n:
            iteration=  n-NotifyThread.MAX_TOBESHOWED-1
        else:
            iteration= -1
             
        try:
            for i in range(n-1,iteration,-1):
                tempList.append((self.listNotif.pop(i)))
        except:
            pass   
        finally:
            return tempList

    def showNotif(self,tempList):
        """
        It takes a list of tuples, and for each tuple, it creates a ToastNotifier object, shows the toast,
        deletes the object, and waits for the duration of the toast plus 2 seconds.
        
        :param tempList: A list of tuples containing the title and message of the notification
        """
        for title,message in tempList:
            try:
                test = ToastNotifier()
                test.show_toast(title=title,msg=message,threaded=True,duration=DURATION)
                del test
            except:
                pass
            sleep(WAITING)
          
    pass

def notify(title,message):
    """
    It sets the title and message of the notification, and then sets the event
    
    :param title: The title of the notification
    :param message: The message to be displayed
    """
    s.acquire()    
    t.addNotify(title,message)
    s.release(N_SEM)
    if e.isSet():
        e.set()
    

e=Event()
s=Semaphore(N_SEM)
t=NotifyThread()
t.start()

