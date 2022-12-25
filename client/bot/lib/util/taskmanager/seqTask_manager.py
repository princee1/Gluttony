from request_builder import *
from print_cli import*
from time import sleep
from random import randint
from datetime import datetime
from request_cs import RequestCS, setUseProxie
from question_ui import confirm

class Integer:
    
    def __init__(self,value:int=0) -> None:
        self.value:int=value
    
    def toNull(self):
        self.value:int=0
    
    def increment(self):
        self.value+=1
    
    def __str__(self) -> str:
        return str(self.value)
        
    def __repr__(self) -> str:
        return self.__str__()

succes=Integer(0)
failed=Integer(0)

def startAllTask(list:list,reverse:bool=False):
    useProxy()
    print(f"- Total of {coloredString(value=list.__len__(),color='BLUE')} task -")
    
    if reverse:
        list.reverse()
    
    for element in list:
        element:RequestCS
        task=TaskSeq(randint(1000,10000),element)
        print_info(task.__str__()) 
        task.run()
        #sleep(randint(5,8))
    
    stats()  

def printHeader():
    pass
    
def useProxy():
    #print(RequestCS.USE_PROXIE)
    value=confirm('Do you want to use Proxy')
    setUseProxie(value)
    #print(RequestCS.USE_PROXIE)
    print('')
    
def stats():
    try:
        total=succes.value+failed.value
        ratio=int((succes.value/total)*100)
        strRatio=format(ratio,"02d")
    except:
        return
    print('')
    desc("====================================================")
    status("All Task Are Done")
    success(f"Succes: {succes}")
    error(f"Failed: {failed}")
    desc(f"Total Task: {total} - ",False)
    desc(f"Ratio : {strRatio} %" )
    desc("====================================================")
    succes.toNull()
    failed.toNull()
    
class TaskSeq:
    def __init__(self,taskNumber,request:RequestCS) -> None:
        self.request:RequestCS=request
        self.name=self.request.name
        self.id=taskNumber
        
    def run(self):
        #try
        status,message=self.request.request()
        
        
        if not status:
            failed.increment()
            error(message)
            if status==False:
                return
        
        status(message) 
        status,message=self.request.succes_method()
        if status:
            success(message)
            succes.increment()
        else:
            error(message)
            failed.increment()
        #except:
            #pass
                
    def __repr__(self) -> str:
        return str(self.id)
    
    def __str__(self) -> str:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return f"[{current_time} Task: {self.id} - Name: {self.name}]"


