from footsites_session import FootsiteSession,FoositeAuth
from common.footsites_account import FootsiteAccount
from footsites_session import Footsite_CSV

account_url = "https://www.champssports.ca/api/v4/users"
activation_link = "https://www.champssports.ca/api/v4/activation"
resentCode_url = 'https://www.champssports.ca/api/v4/users/activation/resend-code'
accountInfo_url = 'https://www.champssports.ca/api/v4/users/account-info'



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
    def __init__(self, proxy, useragents, footstiteData,account:Footsite_CSV):
        super().__init__(proxy, useragents, footstiteData)
        self.account=account
    
    def moduleRequest(self):
        return super().moduleRequest(account_url, "POST", self.account.login_data(), 201, "Name Changed and Saved")
    pass

class FoostiteIds(FoositeAuth):
    
    def moduleRequest(self):
        return super().moduleRequest(accountInfo_url, "GET", None, 200,"Ids Gathered And Saved!")
    pass

class FoostiteResendToken(FoositeAuth):
    def moduleRequest(self):
        return super().moduleRequest(resentCode_url, "POST", self.footsiteData.tokenData(), 200, "Token Resent To Email")
    pass