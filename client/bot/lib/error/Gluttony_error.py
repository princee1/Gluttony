from builtins import BaseException
#NOTE use logging module
import logging as log 
from ui.print_cli import *

ERROR_FILE:str
ERROR_LEVEL={}


class GluttonyException(BaseException):
    
    def __init__(self, *args: object,name,errorCode,message,reason=None,solution=None,) -> None:
        super().__init__(*args)
        self.name=name
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
        rpr:str= self.error_represation(False)
        pass   

    def __repr__(self) -> str:
        superRepr=super().__repr__()
        return self.error_represation(True)
       #TODO faire le format 
    def error_represation(self,isColored:bool):
        
        
        
        text=f"""
    
        
        """
        