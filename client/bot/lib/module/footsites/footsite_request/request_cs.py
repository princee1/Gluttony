

from abc import abstractclassmethod
from typing import ClassVar
from requests import auth, post, get, Response, request, Session
from requests.adapters import ProxyError, SSLError
from requests.exceptions import ReadTimeout
from requests.sessions import session
from csv_interface import CSV_Account, CSVData, appendAccount_csv, updateIds, updateName
from text_interface import deleteElement_inFile, email
import headers_gen as hd
from rnd_account import Account
from client.bot.lib.util.proxyManager.proxie_parser import Proxy, parseProxy
from client.bot.lib.service.email.link_grabber import ActivationToken
from json import JSONDecodeError
from enum import Enum


session_url = "https://www.champssports.ca/api/v4/session"
account_url = "https://www.champssports.ca/api/v4/users"
datadome_url = "https://api-js.datadome.co/js/"
datadome_api_key = 'A55FBF4311ED6F1BF9911EB71931D5'
activation_link = "https://www.champssports.ca/api/v4/activation"
auth_link = 'https://www.champssports.ca/api/v4/auth'
accountInfo_url = 'https://www.champssports.ca/api/v4/users/account-info'
resentCode_url = 'https://www.champssports.ca/api/v4/users/activation/resend-code'

map_statusCode_error = {
    403: "Captcha Found",
    400: "Request Error",
    418: "Teapot error",
    407: "Proxy Authentication Required",
    408: "Request timeout",
    429: "Too Many Request",
    503: "First byte timeout"
}


class RequestType(Enum):
    IDS = 1
    TOKEN = 2
    NAMES = 3


def get_datadome(proxie, user):
    reponse = post(
        proxies=proxie,
        url=datadome_url,
        headers={
            'origin': 'https://www.champssports.ca',
            'referer': 'https://www.champssports.ca/',
            'user-agent': user
        }, data={
            'ddk': datadome_api_key,
            'Referer': '''https%3A%2F%2Fwww.champssports.ca%2F''',
            'responsePage': 'origin',
        }
    )

    return reponse.json()['cookie'].split(";")[0].split("=")[1]



class RequestCS:

    USE_PROXIE = bool(True)

    def __init__(self, proxie: Proxy, useragents):

        self.proxy = ifProxie(proxie)
        self.useragents = useragents
        #self.useragents='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        self.requestData = None
        self.success = False
        self.sessionid2 = None
        self.sessionid = hd.session_id()
        self.headers = {
            'accept': 'application/json',
            'x-api-lang': 'en-CA',
            # 'accept-encoding': 'gzip, deflate, br',
            # 'accept-language': 'en-CA,en;q=0.9',
            'referer': 'https://www.champssports.ca',
            'origin': 'https://www.champssports.ca',
            'x-fl-request-id': hd.request_id(),
            'user-agent': self.useragents
        }
        self.response = None
        self.name = None

    def get_csrfToken(self):
        response = get(url=session_url,
                       # verify=False,
                       proxies=self.proxy,
                       # auth=self.proxy.get_auth(),
                       headers=self.headers,
                       cookies={
                           'datadome':  self.datadome,
                           # 'userVIP': 'unknown',
                           # 'aa_pageHistory': '''[{"n":"","t":"","p":""},{"n":"CSCA: W: Homepage","t":"Home","p":"/"}]''',
                           'JSESSIONID': self.sessionid,
                           # 'userStatus': 'registered'
                       })
        # print(self.proxy)
        # print(response.content)
        self.csrfToken = response.json()['data']['csrfToken']
        self.sessionid2 = response.cookies.get("JSESSIONID")

        return None

    def request(self, url, succes_code, text):
        try:
            # print(self.proxy)
            self.datadome = get_datadome(
                proxie=self.proxy, user=self.useragents)
            self.get_csrfToken()
            reponse = post(url=url,
                           proxies=self.proxy,
                           headers={
                               'content-type': 'application/json',
                               'accept': 'application/json',
                               'user-agent': f'{self.useragents}',
                               'x-fl-request-id': hd.request_id(),
                               'x-flapi-session-id': self.sessionid2,
                               'x-csrf-token': self.csrfToken,
                               'x-api-lang': 'en-CA'},
                           cookies={
                               'JSESSIONID': self.sessionid2,
                               # 'aa_pageHistory': '[{"n":"CSCA: W: Homepage","t":"Home","p":"/"},{"n":"CSCA: W: En: Account: Create","t":"Account","p":"/en/account/create"}]',
                               # 'attntv_mstore_email': f'''"{self.account.email}"''',
                               # 'userVIP': 'unknown',
                               # 'userStatus': 'registered',
                               'datadome': self.datadome,
                           },
                           json=self.requestData
                           )

        except KeyError: 
            return False, "Couldnt connect to the Server"
        except JSONDecodeError:
            return False, "Couldnt get a session"
        except TimeoutError:
            return False, "The handshake operation timed out"
        except ProxyError:
            return False, "Cannot connect to proxy"
        except SSLError:
            return False, "Permissions error"
        except ReadTimeout:
            return False, "Timeout Error"

        self.response = reponse
        return return_result(respone=reponse, succes_code=succes_code, text=text)

    def clone(self):
        pass

    def succes_method(self):
        pass


class RequestCS_NextStep(RequestCS):

    # LOL=None
    def __init__(self, proxie: Proxy, useragents, requestType, account: CSVData):
        super().__init__(proxie, useragents)
        self.requestType = requestType
        self.data = None
        self.account = account

    def request(self, url, datadome, sessionid, text):
        self.datadome = datadome
        self.sessionid = sessionid
        self.headers.update({'x-flapi-session-id': self.sessionid})
        response = request(method=self.requestType,
                           proxies=self.proxy,
                           url=url,
                           json=self.requestData,
                           headers=self.headers,
                           cookies={
                               'JSESSIONID': self.sessionid,
                               'datadome': self.datadome,
                           }
                           )
        try:
            self.get_data(response)
        except:
            pass

        return return_result(respone=response, succes_code=200, text=text)

    def get_data(self, response):
        pass

    def succes_method(self):
        pass


class RequestCS_Account(RequestCS):

    def __init__(self, proxie: Proxy, useragents, account: Account):
        super().__init__(proxie, useragents)
        self.account = account
        self.requestData = account.to_json()
        self.name = self.account.email

    def request(self):
        return super().request(account_url, 201, "Account Sucessfully Created !")

    def __repr__(self) -> str:
        return

    def succes_method(self):
        appendAccount_csv(self.account.writeInFile())
        return True, "Account Saved !"


class RequestCS_Confirm(RequestCS):
    def __init__(self, proxie: Proxy, useragents, activationToken: ActivationToken):
        super().__init__(proxie, useragents)
        self.acitvationToken = activationToken
        self.requestData = activationToken.to_json()
        self.name = self.acitvationToken.token[:10]

    def request(self):
        value = super().request(activation_link, 200, "Account Succesfully Confirmed")
        try:
            if self.response.json()["activationStatus"] == "tokenExpired":
                return None, f"Activation Token expired - {self.response.json()['userId']}"
        except:
            pass
        return value

    def succes_method(self):
        deleteElement_inFile(self.acitvationToken.token, email)
        return True, "Link SuccessFully Deleted From File"

class RequestCS_Auth(RequestCS):

    RESEND_EMAIL: bool = False

    def __init__(self, proxie: Proxy, useragents, account: CSVData, requestType: RequestType):
        super().__init__(proxie, useragents)
        self.account = account
        self.second_rqcs = self.createSecondRqcs(requestType)
        self.requestData = account.login_data()
        self.sessionid_cook = None
        self.datadome_cook = None
        self.waiting_roo = None
        self.name = self.account.email

    def createSecondRqcs(self, requestType):
        if requestType == RequestType.IDS:
            return RequestCS_IDS(self.proxy, self.useragents, self.account)
        elif requestType == RequestType.NAMES:
            return RequestCS_ChangeName(self.proxy, self.useragents, self.account)
        elif requestType == RequestType.TOKEN:
            return RequestCS_ResendToken(self.proxy, self.useragents, self.account)

    def request(self):
        re = super().request(auth_link, 200, "Succesfully Logged in!")
        response = self.response
        try:
            cookk = response.cookies
            self.sessionid_cook = cookk.get("JSESSIONID")
            self.datadome_cook = cookk.get("datadome")
            return return_result(respone=response, succes_code=200, text="Succesfully Logged in!")
        except:
            return re

    def succes_method(self):
        status, rep = self.second_rqcs.request(
            datadome=self.datadome_cook, sessionid=self.sessionid_cook)
        if status:
            self.second_rqcs.succes_method()
        return status, rep

class RequestCS_IDS(RequestCS_NextStep):
    core = 'cCoreCustomerId'
    customerId = 'customerId'
    MESSAGE = "Ids Gathered And Saved!"

    def __init__(self, proxie: Proxy, useragents, account: CSV_Account):
        super().__init__(proxie, useragents, "GET", account)
        self.account = account
        # print(account.file_index)

    def get_data(self, response: Response):
        # print(response.text)
        self.account.customerID = response.json()["customerID"]
        self.account.cCore = response.json()["cCoreCustomerId"]
        # print("dassad")

    def request(self, datadome, sessionid):
        return super().request(accountInfo_url, datadome, sessionid, RequestCS_IDS.MESSAGE)

    def succes_method(self):
        # print(self.data)
        updateIds(self.account)

class RequestFTL_CheckWins(RequestCS_NextStep):

    MESSAGE = ""

    def _init(self, proxie: Proxy, useragents, account: CSVData):
        super.__init__(proxie, useragents, "GET", account)

    def request(self, url, datadome, sessionid, text):
        return super().request(url, datadome, sessionid, RequestFTL_CheckWins.MESSAGE)


    def get_data(self, response):
        print(response)
        
    def succes_method(self):
        pass

class RequestFTL_ConfirmWins(RequestCS_NextStep):
    pass

class RequestCS_ResendToken(RequestCS_NextStep):
    MESSAGE = "Token Resent To Email"

    def __init__(self, proxie: Proxy, useragents, account: CSVData):
        super().__init__(proxie, useragents, "POST", account)
        self.requestData = account.tokenData()

    def request(self, datadome, sessionid):
        return super().request(resentCode_url, datadome, sessionid, RequestCS_ResendToken.MESSAGE)

class RequestCS_ChangeName(RequestCS_NextStep):
    MESSAGE = "Name Changed and Saved"
    NEW_NAME = None

    def __init__(self, proxie: Proxy, useragents, account: CSV_Account):
        super().__init__(proxie, useragents, "PUT", account)
        self.requestData: dict = RequestCS_ChangeName.NEW_NAME

    def succes_method(self):
        self.account.fname = self.requestData.get("firstName")
        self.account.lname = self.requestData.get("lastName")
        updateName(self.account)

    def request(self, datadome, sessionid):
        return super().request(account_url, datadome, sessionid, RequestCS_ChangeName.MESSAGE)


def setNewName(first, last):
    RequestCS_ChangeName.NEW_NAME = {
        'firstName': first,
        'lastName': last
    }


def setUseProxie(value: bool):
    RequestCS.USE_PROXIE = value


def ifProxie(proxie: Proxy):
    if RequestCS.USE_PROXIE:
        return proxie.proxy()
    else:
        return None


def setResendEmail(value: bool):
    RequestCS_Auth.RESEND_EMAIL = value


# TEST
# =====================================================================================================================================
# req = RequestCS_Auth(None,'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
#                  CSV_Account(file_index=1,data=['Prince','Madzou','PrinceMadzou46913@chefkochkuchen.com','Allo1234$','','','','']),RequestType.IDS )

# status,rep=req.request()
# print(rep)
# if status:
#    status,rep=req.succes_method()
#    print(rep)
# =====================================================================================================================================


# FIXEME: a implementer plus tard !!
# =====================================================================================================================================
#
#
# =====================================================================================================================================

#req=RequestCS_Account(proxie=None,useragents='Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',account=Account("Prince","Madzou"))
