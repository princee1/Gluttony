
from imaplib import IMAP4_SSL
from emailConnector import EmailConn
from enum import Enum
#from json_interface import Settings


class IMAPHost(Enum):
    """The IMAPHost class is an enumeration of the IMAP host names for the two email providers that I use
    """
    GMAIL="imap.gmail.com"
    YAHOO="imap.mail.yahoo.com"
    OUTLOOK="outlook.office365.com" #BUG potentiel : might not work


class IMAPMailConn(EmailConn):
    """
    It's a class that allows you to connect to an IMAP server, login, extract data from emails and then 
    close the connection
    """
    
    def __init__(self,host:IMAPHost,user,passw) -> None:
        self.host:IMAPHost=host
        super().__init__(user,passw)
           
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
        self.var.close()   
        pass
    pass