from emailConnector import EmailConn
from pyicloud import PyiCloudService 
raise NotImplementedError()

class Icloud(EmailConn):
    
    def login(self,user,passw):
        self.icloudService=PyiCloudService(user,passw)
        pass
    
    def extractData(self, handler, *args):
        pass
    
    def extractMail(self, mailBox, fromWho, subject):
        tempMails=self.icloudService.files['com~apple~mail']
        
        pass    
    def saveData(self, filename, handler, *args):
        return super().saveData(filename, handler, *args)
    pass
