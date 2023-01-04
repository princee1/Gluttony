from time import time,ctime,mktime

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
        pass
    
    return listRaffle
    
