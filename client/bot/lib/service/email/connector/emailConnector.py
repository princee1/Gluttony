from text_interface import write_list
class EmailConn():
    def __init__(self) -> None:
        self.listData=[]
        self.login()
        pass
    
    def login(self):
        """
        This function logs in the user.
        """
        pass
    
    def extractMail(self,mailBox,fromWho,subject):
        """
        This function extracts the mail from the mailbox, from the sender and with the subject
        
        :param mailBox: The mailbox to extract the mail from
        :param fromWho: The email address of the sender
        :param subject: The subject of the email you want to extract
        """
        pass
    
    def extractData(self,handler,*args):
        """
        A function that takes in a handler and an arbitrary number of arguments. It does not return
        anything.
        
        :param handler: The handler that is being used to extract the data
        """
        
        pass
    
    def saveData(self,filename,handler,*args):
        """
        It extracts data from the handler and saves it in the file
        
        :param filename: the name of the file to save the data in
        :param handler: the function that will be called to extract the data
        """
        self.extractData(handler,args)
        write_list(filename,self.listData)
        #TODO saving the data in the file
        pass