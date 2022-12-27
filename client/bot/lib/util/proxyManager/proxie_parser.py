from util.fileInterface.text_interface import file_to_list,proxy as file_proxy
from requests.auth import HTTPProxyAuth
from random import choice

@DeprecationWarning
def parseProxy(p:str):
    """
    It takes a string of the form "ip:port:user:password" and returns a Proxy object with the
    corresponding values
    
    :param p: the proxy string
    :type p: str
    :return: A Proxy object
    """
    ip,port,user,password=p.split(":")
    return Proxy(ip,port,user,password)

def load_proxy():
    """
    It takes a list of proxies from a file, and returns a list of proxies
    :return: A list of proxies
    """
    list=[]
    for proxy in file_to_list(file_proxy):
        list.append(Proxy(proxy))
    
    return list

class Proxy:
    """
    It's a class that creates a proxy object that can be used in requests
    """
    def __init__(self,ip,port,user,passw) -> None:
        self.ip=ip
        self.port=port
        self.user=user
        self.passw=passw
        
    def __init__(self,ip,port,user,passw,auth:tuple) -> None:
        self.__init__(self,ip,port,user,passw)
        self.authUser,self.authPass=auth
        
    def __init__(self,proxyText:str) -> None:
        ip,port,user,passw=proxyText.split(":")
        self.__init__(self,ip,port,user,passw)
        pass
    
    def __init__(self,proxyText,auth:tuple) -> None:
        ip,port,user,passw=proxyText.split(":")
        self.__init__(self,ip,port,user,passw,auth)
        pass
        
    def proxy(self):
        return  {
                'http': 'http://{}:{}@{}:{}'.format(self.user, self.passw, self.ip, self.port),
                'https': 'http://{}:{}@{}:{}'.format(self.user, self.passw, self.ip, self.port)
            }    
        
    def get_auth(self,):
        return HTTPProxyAuth(username=self.authUser,password=self.authPass)
        
    def get_proxyUrl(self):
        return f'http://{self.user}:{self.passw}@{self.ip}:{self.port}'
    
    def get_fullProxy(self):
        return {'http':self.get_proxyUrl()}
    
    def __repr__(self) :
        return self.get_proxyUrl()
    
    def __str__(self) -> str:
        return self.get_proxyUrl()
    
    def __eq__(self, __o: object) -> bool:
        return self.__str__() == __o.__str__()
        

