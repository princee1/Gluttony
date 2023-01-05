from urllib.request import proxy_bypass
from client.bot.lib.util.proxyManager.proxie_parser import Proxy
from util.taskmanager.requestable_interface import Requestable
import headers_gen as hg
from enum import Enum
from common.footsties_csvData import Footsite_CSV

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
    def __init__(self, proxy, useragents):
        super().__init__(proxy, useragents)
        self.getDatadome()
        self.getCrsfToken()

    def getDatadome(self):
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
        self.sessionid=cookies.get("JSESSIONID")
        self.headers["x-flapi-session-id"]=self.sessionid
        self.cookies['JSESSIONID']=self.sessionid
    
    def __repr__(self) -> str:
        return f"CSRF Token {self.cr} - Session Id {self.sessionid} "

    def footsiteRequest(self,url,method,data,successCode=None):
        try:
            response =self.request(method,url,headers=self.headers
                         ,cookies=self.cookies,
                         proxies=self.proxies,
                         json=data)   
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
        pass
        
        return 
    pass


class FoositeAuth(FootsiteSession):
    
    def __init__(self, proxy, useragents,footstiteData):
        super().__init__(proxy, useragents)
        self.footsiteData:Footsite_CSV=footstiteData
        
    def footsiteRequest(self,successCode):
        cookie= super().footsiteRequest(auth_url_champs, "POST", self.footsiteData.login_data()).cookies
        self.updaterHeaders(cookie)
        self.cookies["datadome"]=cookie.get("datadome")        
        

    pass


