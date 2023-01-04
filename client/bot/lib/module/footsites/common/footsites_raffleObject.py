from util.other.winResponse import Win
from util.rafflemanager.raffle import Raffle

WINFILE:str


# > The `FootsiteRaffle` class is a subclass of the `Raffle` class. It has a constructor that takes a
# `response` object as an argument. It has a method called `deconstruct` that takes a `value` as an
# argument
class FootsiteRaffle(Raffle):
    def __init__(self,response):
        self.deconstruct(response)
        pass
    
    def deconstruct(self, value):
        #TODOsuper().__init__()
        pass
    pass


# `FootsitesWin` is a subclass of `Win` that has a `deconstruct` method that takes a `response` as an
# argument and returns nothing, a `toFile` method that takes a `buffer` as an argument and returns the
# result of calling the `toFile` method of the `Win` class, and a `toDiscordEmbedValue` method that
# returns a tuple
class FootsitesWin(Win):
    
    def deconstruct(self, response):
        pass
    
    def toFile(self,buffer):
        return super().toFile(WINFILE, buffer)
    
    def toDiscordEmbedValue(self) -> tuple:
        pass
    pass