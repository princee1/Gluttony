from util.other.rnd_account import Account,BirthFormat

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
    