
from imaplib import IMAP4_SSL
from emailConnector import EmailConn
from enum import Enum
#from json_interface import Settings


class IMAPHost(Enum):
    GMAIL=""
    YAHOO=""

class IMAPMailConn(EmailConn):
    def __init__(self,host:IMAPHost) -> None:
        self.host:IMAPHost=host
        super().__init__()
        
    
    def login(self):
        try: 
            self.var:IMAP4_SSL =IMAP4_SSL(host=str(self.host))
            status,message=self.var.login(user="", password="")
            if status=='OK':
                self.status=True
                #success(str(message[0]))
            else :
                self.status=False
                #error(str(message[0]))
                return
        except:
            self.status=False
        pass
    
    def decorationStatus(self,handler):
        if self.status:
            handler()
            pass
        
    #TODO ajouter un decorator
    def extractMail(self,fromWho, subject,mailBox="INBOX"):
        #BUG potentiel: peut etre mieux de mettre un raise Error 
        try:
            self.var.select(mailBox)
            _, result = self.var.search(None,f'(FROM "{fromWho}")',
                                f'(SUBJECT "{subject}")', 'UNSEEN')
            self.data = result[0].split()
            #status(f"Total Messages from {fromWho}:  {len(data)}")
        except:
            pass
        pass
    
    def extractData(self,handler,*args):
        for data in self.data:
            _,mail = self.var.fetch(data, '(RFC822)')
            self.listData.append(handler(mail,args))
        pass
   
    pass

test = IMAPMailConn(IMAPHost.GMAIL)