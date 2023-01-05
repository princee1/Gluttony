##TODO: Trouver des meilleurs nom de methodes
from requests import Session
from enum import Enum

class RequestState(Enum):
    ERROR=0,
    SUCCESS=1,
    PROXY_ERROR=2,
    RETRY=3,
    NEXT=4,
    
    pass

class Requestable(Session):
    def __init__(self,proxy,useragents):  
        self.proxies=proxy.proxy()
        self.useragents=useragents
        self.state:RequestState
        pass
    def rotateProxies(self,proxy):
        self.proxies=proxy
        pass
    def start(self):
        pass
    def restart():
        pass
    def end(self):
    
        pass
     
    pass
