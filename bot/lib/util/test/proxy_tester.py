from requests.adapters import ProxyError
from proxie_parser import Proxy, parseProxy
from requests import Session


try:
    text="34.149.128.53:9200:country-ca-session-f212aa11f60d4593bbc37cf38b0239b8:bb7d9157-86da-4117-9a35-e2fab09f3990"
    ip,port,user,passw=text.split(":")
    proxy=Proxy(ip,port,user,passw)
    datadome_url = "https://api-js.datadome.co/js/"
    datadome_api_key = 'A55FBF4311ED6F1BF9911EB71931D5'
    proxies = {
                'http': 'http://{}:{}@{}:{}'.format(user, passw, ip, port),
                'https': 'http://{}:{}@{}:{}'.format(user, passw, ip, port)
            }
    session=Session()
    session.headers={
                'accept': '*/*',
                'origin': 'https://www.champssports.ca',
                'referer': 'https://www.champssports.ca/',
                'user-agent':'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'      
    }
    data={
                'ddk': datadome_api_key,
                'Referer': '''https%3A%2F%2Fwww.champssports.ca%2F''',
                'responsePage': 'origin',
            }
    reponse=session.post(url=datadome_url,proxies=proxies,data=data,allow_redirects=True,timeout=1)
    print(reponse.content)
    
    #print(proxy.get_proxyUrl())
except TimeoutError as e:
    print("The handshake operation timed out")
except ProxyError as e:
    print(e.__repr__())
    pass