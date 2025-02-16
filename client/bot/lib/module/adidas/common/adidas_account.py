from util.other.rnd_account import Account,BirthFormat
from util.fileInterface.file_manager import adidasPath
from service.email.link_grabber import ActivationToken

ACCOUNT_FILE:str = adidasPath("Account.csv")
ACITVATION_FILE:str =adidasPath("ActivationToken.txt")

class FoostiteActivationToken(ActivationToken):
    
    def to_json(self):
        return {}
    
    def deleteActivated(self):
        return super().deleteActivated(ACITVATION_FILE)


class FootsiteAccount(Account):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName,BirthFormat.ADIDAS)
    
    def to_json(self):
        return {
        }
    
    def appendToFile(self):
        return super().appendToFile(ACCOUNT_FILE)
