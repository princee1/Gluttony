from emailConnector import EmailConn
raise NotImplementedError()

class Icloud(EmailConn):
    
    def login(self):
        pass
    
    def extractData(self, handler, *args):
        pass
    
    def extractMail(self, mailBox, fromWho, subject):
        pass    
    def saveData(self, filename, handler, *args):
        return super().saveData(filename, handler, *args)
    pass
