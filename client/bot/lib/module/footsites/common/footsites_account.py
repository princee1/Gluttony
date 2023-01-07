from util.other.rnd_account import Account,BirthFormat
from util.fileInterface.file_manager import footsitePath
ACCOUNT_FILE:str = footsitePath("Account.csv")


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
