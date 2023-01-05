from footsites_session import FootsiteSession,FoositeAuth
from common.footsites_account import FootsiteAccount

account_url = "https://www.champssports.ca/api/v4/users"

class FoostiteCreateAccount(FootsiteSession):
    
    def __init__(self, proxy, useragents,account):
        super().__init__(proxy, useragents)
        self.account:FootsiteAccount = account
    
    def moduleRequest(self):
        return super().moduleRequest(account_url, "POST", self.account.to_json(), 201, "Account Sucessfully Created !")
    pass

class FoostiteConfirmAccount(FoositeAuth):
    pass

class FoostiteRenameAccount(FoositeAuth):
    pass

class FoostiteIds(FoositeAuth):
    pass
