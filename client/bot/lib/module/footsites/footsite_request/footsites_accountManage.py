from footsites_session import FootsiteSession,FoositeAuth
from common.footsites_account import FootsiteAccount

account_url = "https://www.champssports.ca/api/v4/users"
activation_link = "https://www.champssports.ca/api/v4/activation"


class FoostiteCreateAccount(FootsiteSession):
    
    def __init__(self, proxy, useragents,account):
        super().__init__(proxy, useragents)
        self.account:FootsiteAccount = account
    
    def moduleRequest(self):
        return super().moduleRequest(account_url, "POST", self.account.to_json(), 201, "Account Sucessfully Created !")
    pass

class FoostiteConfirmAccount(FootsiteSession):
  
    def __init__(self, proxy, useragents,token):
        super().__init__(proxy, useragents)
        self.acctoken=token
    
    def moduleRequest(self):
        values= super().moduleRequest(activation_link, "POST", self.acctoken.to_json(), 200, "Account Succesfully Confirmed")
        try:
            if self.response.json()["activationStatus"] == "tokenExpired":
                return None, f"Activation Token expired - {self.response.json()['userId']}"
        except:
            pass
        return values
    
    pass

class FoostiteRenameAccount(FoositeAuth):
    pass

class FoostiteIds(FoositeAuth):
    pass
