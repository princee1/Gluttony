from util.other.winResponse import Win
from util.rafflemanager.raffle import Raffle,raffleReader

WINFILE:str
RAFFLE_FILE:str

class AdidasRaffle(Raffle):
    
    def __init__(self,response):
        self.deconstruct(response)
        pass
    
    def __init__(self, values):
        super().__init__(values[:4])
    
    def deconstruct(self, value):
        #TODOsuper().__init__(ModuleEnum.ADIDAS)
        pass
    
    pass

class AdidasWin(Win):
    def deconstruct(self, response):
        pass
    
    def toFile(self,buffer):
        return super().toFile(WINFILE, buffer)
    
    def toDiscordEmbedValue(self) -> tuple:
        pass
    
    pass

def returnRaffle(values):
    return AdidasRaffle(values)
 
def getAdidasRaffle():
    return raffleReader(RAFFLE_FILE,returnRaffle)