from util.other.rnd_account import Account,BirthFormat
from util.fileInterface.file_manager import footsitePath
from service.email.link_grabber import ActivationToken

ACCOUNT_FILE:str = footsitePath("Account.csv")
ACITVATION_FILE:str =footsitePath("ActivationToken.txt")

class FoostiteActivationToken(ActivationToken):
    
    def to_json(self):
        return {"activationToken": self.token}
    
    def deleteActivated(self):
        return super().deleteActivated(ACITVATION_FILE)


class FootsiteAccount(Account):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName,BirthFormat.FOOTSITE)
    
    def to_json(self):
        return {
            "optIn": False,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "uid": self.email,
            "password": self.password,
            "birthday": self.birthday,
            "wantToBeVip": False
        }
    
    def appendToFile(self):
        return super().appendToFile(ACCOUNT_FILE)
