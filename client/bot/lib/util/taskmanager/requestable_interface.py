##TODO: Trouver des meilleurs nom de methodes
from requests import Session
from util.other.proxie_parser import Proxy


class Requestable(Session):
    def __init__(self,proxy:Proxy,useragents):    
        pass
    
    def rotateProxies(self):
        pass
    def start(self):
        pass
    def end(self):
        pass
    
    pass
