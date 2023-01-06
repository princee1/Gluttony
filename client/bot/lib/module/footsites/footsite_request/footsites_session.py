from urllib.request import proxy_bypass
from client.bot.lib.util.proxyManager.proxie_parser import Proxy
from util.taskmanager.requestable_interface import Requestable,RequestState
import headers_gen as hg
from enum import Enum
from common.footsties_csvData import Footsite_Account_CSV

# TODO: completer l'objet footsite session
datadome_url = "https://api-js.datadome.co/js/"
datadome_api_key = 'A55FBF4311ED6F1BF9911EB71931D5'
session_url_champs = "https://www.champssports.ca/api/v4/session"
auth_url_champs = 'https://www.champssports.ca/api/v4/auth'

class FootsiteType(Enum):
    CHAMPS = 1
    FOOTLOCKER = 2
    pass

class FootsiteSession(Requestable):
    """
    It's a class that creates a session with the Footsite, and then allows you to make requests to the
    Footsite
    """
     
    def __init__(self, proxy, useragents):
        """
        The function gets the datadome cookie and crsf token from the website
        
        :param proxy: The proxy you want to use
        :param useragents: A list of user agents to use
        """
        super().__init__(proxy, useragents)
        self.getDatadome()
        self.getCrsfToken()

    def getDatadome(self):
        """
        It gets the datadome cookie and the session id and then sets the cookies to the datadome cookie
        and the session id.
        """
        self.sessionid = hg.session_id()
        reponse = self.post(
            proxies=self.proxies,
            url=datadome_url,
            headers={
                'origin': 'https://www.champssports.ca',
                'referer': 'https://www.champssports.ca/',
                'user-agent': self.useragents
            }, data={
                'ddk': datadome_api_key,
                'Referer': '''https%3A%2F%2Fwww.champssports.ca%2F''',
                'responsePage': 'origin',
            }
        )
        datadome = reponse.json()['cookie'].split(";")[0].split("=")[1]
        self.cookies = {
            'datadome':  datadome,
            'JSESSIONID': self.sessionid,
        }
        pass

    def getCrsfToken(self):
        """
        It gets the csrfToken from the session_url_champs and updates the headers and cookies.
        """
        self.headers={
            'accept': 'application/json',
            'x-api-lang': 'en-CA',
            'referer': 'https://www.champssports.ca',
            'origin': 'https://www.champssports.ca',
            'x-fl-request-id': self.sessionid,
            'user-agent': self.useragents
        }
        response=self.get(session_url_champs,
                          proxies=self.proxies,
                          headers=self.headers,
                            cookies=self.cookies
                          )
        self.csrfToken = response.json()['data']['csrfToken']
        self.headers['x-csrf-token']=response.json()['data']['csrfToken']
        self.updaterHeaders(response.cookies)
        pass

    def updaterHeaders(self, cookies):
        """
        It takes a cookie object and updates the headers and cookies of the class instance
        
        :param cookies: the cookies that are returned from the request
        """
        self.sessionid=cookies.get("JSESSIONID")
        self.headers["x-flapi-session-id"]=self.sessionid
        self.cookies['JSESSIONID']=self.sessionid
    
    def __repr__(self) -> str:
        return f"CSRF Token {self.cr} - Session Id {self.sessionid} "
      
    pass


class FoositeAuth(FootsiteSession):
    """This class inherits from the FootsiteSession class and adds the ability to authenticate to the
    Footsite website
    """
    
    def __init__(self, proxy, useragents,footstiteData):
        """
        This function is the constructor for the Footsite_Scraper class. It takes in a proxy, a list of
        useragents, and a Footsite_CSV object. It then calls the constructor for the parent class, which
        is the Scraper class
        
        :param proxy: a list of proxies to use
        :param useragents: a list of user agents to use for the requests
        :param footstiteData: This is the Footsite_CSV class that we created earlier
        """
        super().__init__(proxy, useragents)
        self.footsiteData:Footsite_Account_CSV=footstiteData
        
    def authenticate(self):
        """
        It takes the response from the login request and updates the headers with the cookies from the
        response.The method calls the super().footsiteData method, which authenticates to the Footsite
        API
        
        :return: The result is a tuple of two elements. The first element is a boolean value that indicates
        whether the request was successful or not. The second element is the response object.
        """
        result=super().moduleRequest(auth_url_champs, "POST", self.footsiteData.login_data(),200,"Succesfully Logged in!")
        if result[0]:
            self.updaterHeaders(self.response.cookies)
            self.cookies["datadome"]=self.response.cookies.get("datadome")   
        return result
        
    pass




