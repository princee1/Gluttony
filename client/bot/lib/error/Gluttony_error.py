from builtins import BaseException
from ui.print_cli import *

ERROR_FILE:str

class GluttonyException(BaseException):
    
    def __init__(self, *args: object,errorCode,message,reason=None,solution=None) -> None:
        super().__init__(*args) 
        self.errorCode=errorCode
        self.message=message
        self.reason=reason
        self.solution=solution
        self.buildReason()
        self.buildSolution()
        
    def applySolution(self):
        pass
    
    def createSolution(self):
        pass
    
    def createReason(self):
        pass
    
    def buildReason(self):
        if self.reason == None:
            return
        self.createReason()  
        pass

    def buildSolution(self):
        if self.solution == None:
            return
        self.createSolution()  
        pass

    def logger(self):
        
        pass
    
    #TODO faire le format
    def __repr__(self) -> str:
        superRepr=super().__repr__()
    