from threading import Timer
from raffle import Raffle
from math import floor


# The RaffleTimer class is a subclass of the Timer class. It has a constructor that takes in a Raffle
# object and a process to start. It has a run method that prints out the raffle and the time until the
# raffle starts. It has a target method that manipulates the process to start
class RaffleTimer(Timer):
    def __init__(self,raffle,processToStart):
        self.process=processToStart
        self.raffle:Raffle= raffle
        super().__init__(self.raffle.getElapsedTime(),self.target)
        
        
    def run(self) -> None:
        print("  Watching the Raffle:")
        print(self.raffle)
        print(f"Raffle starts in {convertTime(self.interval)}")
        super().run()
        
    def target(self):
        #TODO manipulate the process to start
        pass


def convertTime(time):
    """
    It converts a time in seconds to hours, minutes and seconds.
    
    :param time: The time in seconds
    """
    h= (time / 3600)
    m = (round(h-floor(h),5) *3600)/60
    s = (m-floor(m))*60
    return f"{floor(h)}(h) - {floor(m)}(min) - {round(s,1)}(sec)"
