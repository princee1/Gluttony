import win32com.client.gencache as win
from emailConnector import EmailConn

#NOTE email, read from oulook client application
raise NotImplementedError()
class Outlook(EmailConn):
    def login(self):
        pass
    
    def extractData(self, handler, *args):
        pass
    
    def extractMail(self, mailBox, fromWho, subject):
        pass    
    def saveData(self, filename, handler, *args):
        return super().saveData(filename, handler, *args)
    pass
