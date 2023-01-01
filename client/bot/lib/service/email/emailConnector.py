
class EmailConn():
    def __init__(self) -> None:
        self.listData=[]
        self.login()
        pass
    
    def login(self):
        pass
    
    def extractMail(self,mailBox,fromWho,subject):
        pass
    
    def extractData(self,handler,*args):
        
        pass
    
    def saveData(self,filename,handler,*args):
        self.extractData(handler,args)
        #TODO saving the data in the file
        pass