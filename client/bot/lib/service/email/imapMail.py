
from imaplib import IMAP4_SSL
from emailConnector import EmailConn
from enum import Enum
from json_interface import Settings


class IMAPHost(Enum):
    GMAIL=""
    YAHOO=""

class IMAPMailConn(EmailConn):
    def __init__(self,host:IMAPHost) -> None:
        super().__init__()
        self.host:IMAPHost=host
    
    def login(self):
        self.var:IMAP4_SSL =IMAP4_SSL(host=str(self.host))
        status,message=self.var.login(user="", password="")
        if status=='OK':
            self.status=True
            #success(str(message[0]))
        else :
            self.status=False
            #error(str(message[0]))
            return
    
    def decoration_status(self,handler):
        if self.status:
            handler()
            pass
    #ajouter un decorator
    def extractMail(self,fromWho, subject,mailBox="INBOX"):
        self.var.select(mailBox)
        _, result = self.var.search(None,f'(FROM "{fromWho}")',
                            f'(SUBJECT "{subject}")', 'UNSEEN')
        self.data = result[0].split()
        #status(f"Total Messages from {fromWho}:  {len(data)}")
        pass
   
    pass