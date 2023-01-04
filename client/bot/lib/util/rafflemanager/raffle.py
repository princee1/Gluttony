from time import time,ctime,mktime

# A class that represents a raffle, with a sku, name, date, and dateRaffle, and has methods to get the
# elapsed time, deconstruct, and check if it's active.
class Raffle:
    
    def __init__(self,sku:str,name:str,date,dateRaffle):
        self.sku = sku
        self.name = name
        self.date = date
        self.dateRaffle=dateRaffle
        pass
    
    def __init__(self,values):
        self.sku,self.name,self.date,self.dateRaffle=values
        pass
    
    def getElapsedTime(self):
        now= time()
        pass
    
    def deconstruct(self,value):
        pass
    
    def isActive(self)-> bool:
        pass
    pass

def raffleReader(file,handler):
    """
    It reads a file, and for each line, it calls a handler function that returns a Raffle object. 
    
    The handler function is a function that takes a list of strings and returns a Raffle object. 
    
    The handler function is passed as a parameter to the raffleReader function. 
    
    The raffleReader function returns a list of Raffle objects. 
    
    The raffleReader function is a function that takes a file name and a handler function and returns a
    list of Raffle objects. 
    
    :param file: the file name
    :param handler: a function that takes a list of strings and returns a Raffle object
    :return: A list of Raffle objects
    """
    listRaffle=[]
    values=[]
    with open(file,"r") as fd:
        while values!=None:
            try:
                values = fd.readline().split(",")
            except:
                values=None
                pass
            tempRaffle:Raffle
            tempRaffle=handler(values)
            if tempRaffle.isActive():
                listRaffle.append()
    return listRaffle
    
