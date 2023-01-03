from util.other.winResponse import Win
from util.rafflemanager.raffle import Raffle

WINFILE:str


class AdidasRaffle(Raffle):
    pass

class AdidasWin(Win):
    def deconstruct(self, response):
        pass
    
    def toFile(self,buffer):
        return super().toFile(WINFILE, buffer)
    
    def toDiscordEmbedValue(self) -> tuple:
        pass
    
    pass
