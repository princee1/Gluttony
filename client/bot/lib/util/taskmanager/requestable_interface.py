##TODO: Trouver des meilleurs nom de methodes
from json import JSONDecodeError
from ssl import SSLError
from httpx import ProxyError
from requests import ReadTimeout, Session
from enum import Enum

MAP_ERROR= {
    403: "Captcha Found",
    400: "Request Error",
    418: "Teapot error",
    407: "Proxy Authentication Required",
    408: "Request timeout",
    429: "Too Many Request",
    503: "First byte timeout"
}
class RequestState(Enum):
    INIT=0,
    ERROR=1,
    SUCCESS=2,
    PROXY_ERROR=3,
    RETRY=4,
    NEXT=5,
    
    pass

class Requestable(Session):
    
    def __init__(self,proxy,useragents):  
        self.proxies=proxy.proxy()
        self.useragents=useragents
        self.state:RequestState
        pass
    
    def rotateProxies(self,proxy):
        self.proxies=proxy
        pass
    
    def start(self):
        pass
    
    def moduleRequest(self,url,method,data,successCode,succesText):
        """
        It takes a url, method, data, successCode, and successText and returns a boolean and a string.
        
        :param url: The url to send the request to
        :param method: POST or GET
        :param data: is a dictionary of the data that is being sent to the server
        :param successCode: The code that the server returns when the request is successful
        :param succesText: The text that should be in the response if the request was successful
        :return: The returnState function is being called with the parameters successCode,
        self.response, and succesText.
        """
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
        self.response=response
        del response
        return self.returnState(successCode,self.response,succesText)
    
    def authenticate(self) -> None:
        pass
    
    def parse_error(self):
        """
        If the response is 400, return the error message from the response. Otherwise, return the error
        message from the MAP_ERROR dictionary
        
        :param response: The response object from the request
        :return: The response object
        """
        val = MAP_ERROR.get(self.response.status_code)
        try:
            return self.parse_error(val)
        except:
            pass
        return val

    def parse_error(self, val):
        pass

    def returnState(self,succes_code: int, respone, text: str):
        """
        If the status code of the response is equal to the success code, return True and the text, otherwise
        return False and the parsed error
        
        :param succes_code: The HTTP status code that indicates success
        :type succes_code: int
        :param respone: The response from the API
        :param text: The text to be sent to the user
        :type text: str
        :return: A tuple of two values.
        """
        status_code = respone.status_code
        if status_code == succes_code:
            return True, text
        else:
            return False, self.parse_error(respone)
    
    def restart(self):
        pass
    
    def end(self):
    
        pass
     
    pass

