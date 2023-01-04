##TODO: Trouver des meilleurs nom de methodes
from requests import Session
from util.other.proxie_parser import Proxy


class Requestable(Session):
    def __init__(self,proxy:Proxy,useragents):  
        self.proxies=proxy.proxy()
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
