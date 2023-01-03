from util.other.winResponse import Win
from util.rafflemanager.raffle import Raffle

WINFILE:str


class FootSiteRaffle(Raffle):
    pass


class FootsitesWin(Win):
    
    def deconstruct(self, response):
        pass
    
    def toFile(self,buffer):
        return super().toFile(WINFILE, buffer)
    
    def toDiscordEmbedValue(self) -> tuple:
        pass
    pass