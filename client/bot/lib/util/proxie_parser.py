from text_interface import file_to_list,proxy as file_proxy
from requests.auth import HTTPProxyAuth
from random import choice

def parseProxy(p:str):
    ip,port,user,password=p.split(":")
    return Proxy(ip,port,user,password)

def load_proxy():
    list=[]
    for proxy in file_to_list(file_proxy):
        list.append(parseProxy(proxy))
    
    return list

class Proxy:
    
    def __init__(self,ip,port,user,passw) -> None:
        self.ip=ip
        self.port=port
        self.user=user
        self.passw=passw
    
    def proxy(self):
        return  {
                'http': 'http://{}:{}@{}:{}'.format(self.user, self.passw, self.ip, self.port),
                'https': 'http://{}:{}@{}:{}'.format(self.user, self.passw, self.ip, self.port)
            }
        
        
    def get_auth(self):
        return HTTPProxyAuth(username=self.user,password=self.passw)
    def get_proxy(self)->dict:
        return {
            #'https':f"https://{self.ip}:{self.port}",
            'http':f"http://{self.ip}:{self.port}"
            }
    def get_proxyUrl(self):
        return f'http://{self.user}:{self.passw}@{self.ip}:{self.port}'
    def get_fullProxy(self):
        return {'http':self.get_proxyUrl()}
    def __repr__(self) :
        return self.get_proxyUrl()
    
    
        

