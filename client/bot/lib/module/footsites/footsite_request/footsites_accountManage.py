from footsites_session import FootsiteSession,FoositeAuth
from common.footsites_account import FootsiteAccount,FoostiteActivationToken
from common.footsties_csvData import Footsite_Account_CSV


account_url = "https://www.champssports.ca/api/v4/users"
activation_link = "https://www.champssports.ca/api/v4/activation"
resentCode_url = 'https://www.champssports.ca/api/v4/users/activation/resend-code'
accountInfo_url = 'https://www.champssports.ca/api/v4/users/account-info'



class FoostiteCreateAccount(FootsiteSession):
    """This class is a subclass of the FootsiteSession class, and it's purpose is to create an account on
the Footsite
    """
    def __init__(self, proxy, useragents,account):
        super().__init__(proxy, useragents)
        self.account:FootsiteAccount = account
    
    def moduleRequest(self):
        return super().moduleRequest(account_url, "POST", self.account.to_json(), 201, "Account Sucessfully Created !")
    
    def end(self):
        self.account.appendToFile()
        pass
    
    pass

class FoostiteConfirmAccount(FootsiteSession):
    """This class is used to confirm the account by sending a POST request to the activation link with the
activation token as the payload
    """
    def __init__(self, proxy, useragents,token):
        super().__init__(proxy, useragents)
        self.acctoken:FoostiteActivationToken=token
    
    def moduleRequest(self):
        values= super().moduleRequest(activation_link, "POST", self.acctoken.to_json(), 200, "Account Succesfully Confirmed")
        try:
            if self.response.json()["activationStatus"] == "tokenExpired":
                return None, f"Activation Token expired - {self.response.json()['userId']}"
        except:
            pass
        return values
    
    def end(self):
        self.acctoken.deleteActivated()
        pass
    
    pass

class FoostiteRenameAccount(FoositeAuth):
    """This class is a subclass of the FoositeAuth class. It takes in the same parameters as the
FoositeAuth class, but also takes in an account object. It then uses the account object to make a
POST request to the account_url

    """
    FIRST:str
    LAST:str
    
    def __init__(self, proxy, useragents, footstiteData,account:Footsite_Account_CSV):
        super().__init__(proxy, useragents, footstiteData)
        self.account=account
    
    def moduleRequest(self):
        return super().moduleRequest(account_url, "POST", self.account.login_data(), 201, "Name Changed and Saved")

    def end(self):
        self.account.updateName(self.FIRST,self.LAST)
    
    @classmethod
    def changeName(self=None,first=None,last=None):
        FoostiteRenameAccount.FIRST=first
        FoostiteRenameAccount.LAST=last
        
        pass
    pass


class FoostiteIds(FoositeAuth):
    """This class inherits from the FoositeAuth class and uses the moduleRequest method to make a request
to the accountInfo_url and returns the response

    """
    def moduleRequest(self):
        return super().moduleRequest(accountInfo_url, "GET", None, 200,"Ids Gathered And Saved!")
    
    def end(self):
        self.footsiteData.customerID = self.response.json()["customerID"]
        self.footsiteData.cCore = self.response.json()["cCoreCustomerId"]
        ##self.footsiteData.updateValue("customerID", self.footsiteData.customerID)
    pass

class FoostiteResendToken(FoositeAuth):
    """This class is a subclass of the FoositeAuth class. It inherits the moduleRequest method from the
FoositeAuth class. It overrides the moduleRequest method by calling the superclass's moduleRequest
method and passing in the resentCode_url, "POST", self.footsiteData.tokenData(), 200, "Token Resent
To Email" arguments
    """
    def moduleRequest(self):
        return super().moduleRequest(resentCode_url, "POST", self.footsiteData.tokenData(), 200, "Token Resent To Email")
    pass