from win10toast import ToastNotifier
from threading import Event,Thread


# It's the duration of the toast notification.
DURATION = 2

# It's declaring the variables e and t as global variables.
global e,t

class NotifyThread(Thread):
    """
    It's a thread that waits for a signal to show a toast notification
    """
    def __init__(self) -> None:
        super().__init__()
        self.title=None
        self.message=None
        self.active=True
        
    def run(self) -> None:
        self.privatenotify()
    
    def setValue(self,title,message):
        """
        It sets the value of the message and title variables to the message and title variables passed
        in.
        
        :param title: The title of the message box
        :param message: The message to be displayed
        """
        self.message=message
        self.title=title
        
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
                e.wait()
                if self.active:
                    test = ToastNotifier()
                    test.show_toast(title=self.title,msg=self.message,threaded=True)
                    del test
                e.clear()
            except:
                pass
        
    pass

def notify(title,message):
    """
    It sets the title and message of the notification, and then sets the event
    
    :param title: The title of the notification
    :param message: The message to be displayed
    """
    t.setValue(title,message)
    e.set()
    

e=Event()
t=NotifyThread()
t.start()
