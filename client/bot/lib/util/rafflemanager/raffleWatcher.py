from threading import Timer
from raffle import Raffle
from math import ceil,floor


class RaffleTimer(Timer):
    def __init__(self,raffle,processToStart):
        self.process=processToStart
        self.raffle:Raffle= raffle
        super().__init__(self.raffle.getElapsedTime(),self.target)
        
        
    def run(self) -> None:
        print("  Watching the Raffle:")
        print(self.raffle)
        print(f"Raffle starts in {convertToSeconds(self.interval)}")
        super().run()
        
    def target(self):
        #TODO manipulate the process to start
        pass


def convertToSeconds(time):
    h= (time / 3600)
    m = (round(h-floor(h),5) *3600)/60
    s = (m-floor(m))*60
    return f"{floor(h)}(h) - {floor(m)}(min) - {round(s,1)}(sec)"
