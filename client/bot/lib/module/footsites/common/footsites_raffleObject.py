from util.other.winResponse import Win
WINFILE:str

class FootsitesWin(Win):
    
    def deconstruct(self, response):
        pass
    
    def toFile(self,buffer):
        return super().toFile(WINFILE, buffer)
    
    def toDiscordEmbedValue(self) -> tuple:
        pass
    pass