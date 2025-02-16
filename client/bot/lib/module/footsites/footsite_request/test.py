

from abc import abstractclassmethod
from pprint import pprint
from turtle import goto
from typing import ClassVar
from urllib import response
from requests import auth, post, get, Response, request, Session
from requests.adapters import ProxyError, SSLError
from requests.exceptions import ReadTimeout
from requests.sessions import session
#from csv_interface import CSV_Account, CSV_Data, appendAccount_csv, updateIds, updateName
#from text_interface import deleteElement_inFile, email
import headers_gen as hd
#from rnd_account import Account
#from proxie_parser import Proxy, parseProxy
#from link_grabber import ActivationToken
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


def test_get_datadome():
    print("testing datadome...")

    reponse = post(
        # proxies=proxie,
        # verify=False,
        timeout=2,
        # auth=proxie.get_auth(),
        url=datadome_url,
        headers={
            # 'accept': '*/*',
            # 'accept-encoding': 'gzip, deflate, br',
            # 'accept-language': "en-US,en;q=0.9,fr-CA;q=0.8,fr;q=0.7",
            # content-length: 4189
            # 'content-type': 'application/x-www-form-urlencoded',
            # 'dnt': '1',
            'origin': 'https://www.champssports.ca',
            # 'referer': 'https://www.champssports.ca/',
            # 'sec-ch-ua': '''" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"''',
            # 'sec-ch-ua-mobile': "?0",
            # sec-ch-ua-platform: "Windows"
            # sec-fetch-dest: empty
            # sec-fetch-mode: cors
            # sec-fetch-site: cross-site
            'user-agent': """Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36"""
        }, data={
            # 'jsType': 'ch',
            # 'cid': 'uSrfjF3l2frIXcg2FqsqistVILdF4BVsEWkGJA4-vfz0uJSnMKnkFlugbB.yG1DxAKl~EXK0iGw90fJTYP8fkEf-Q~Nb~EKQ~9kC2n8mhF84j2Ra8JLxpq49hkHqAaa',
            'ddk': datadome_api_key,
            'Referer': '''https%3A%2F%2Fwww.champssports.ca%2F''',
            # 'request': '%2F',
            'responsePage': 'origin',
            # 'ddv': '4.1.73'
        }
    )

    assert reponse.json()['status'] == 200, "Test Failed"
    print('Test Passed')


def test_get_csrfToken():
    response = get(url=session_url,
                   # verify=False,
                   #  proxies=self.proxy,
                   # auth=self.proxy.get_auth(),
                   headers={
                       # 'accept': 'application/json',
                       # 'x-api-lang': 'en-CA',
                       # 'accept-encoding': 'gzip, deflate, br',
                       # 'accept-language': 'en-CA,en;q=0.9',
                       # 'referer': 'https://www.champssports.ca/',
                       'origin': 'https://www.champssports.ca',
                       'x-fl-request-id': hd.request_id(),
                       'user-agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36"
                   },
                   cookies={
                       # 'datadome': "a48YgSnSN_XF.Tcu2xCx_lKXMwK9f5lgKmytJVjlZN79edfCkreKli9JBv5zauaNyAKKUVjH.Z7zsodTsEf_QslmvMS0u36HHrR2c2I5vXtnbetZV_zZFvRiMsTe02",
                       # 'userVIP': 'unknown',
                       # 'aa_pageHistory': '''[{"n":"","t":"","p":""},{"n":"CSCA: W: Homepage","t":"Home","p":"/"}]''',
                       'JSESSIONID': hd.session_id(),
                       # 'userStatus': 'registered'
                   })
    # print(self.proxy)
    print(response.content)
   # assert response.json()['status']==200, "Test Failed"
    csrfToken = response.json()['data']['csrfToken']
    sessionid2 = response.cookies.get("JSESSIONID")
   
    print(csrfToken)
    print(sessionid2)


def test_create_account(csrf, session,):
    response = get(url=account_url,
                   # verify=False,
                   #  proxies=self.proxy,
                   # auth=self.proxy.get_auth(),
                   headers={
                       # 'accept': 'application/json',
                       # 'x-api-lang': 'en-CA',
                       # 'accept-encoding': 'gzip, deflate, br',
                       # 'accept-language': 'en-CA,en;q=0.9',
                       # 'referer': 'https://www.champssports.ca/',
                       #'content-type': 'application/json',
                       #'accept': 'application/json',
                       'x-fl-request-id': hd.request_id(),
                       'x-flapi-session-id': session,
                       'x-csrf-token': csrf,
                       'user-agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36"
                   },
                   cookies={
                        'datadome': "a48YgSnSN_XF.Tcu2xCx_lKXMwK9f5lgKmytJVjlZN79edfCkreKli9JBv5zauaNyAKKUVjH.Z7zsodTsEf_QslmvMS0u36HHrR2c2I5vXtnbetZV_zZFvRiMsTe02",
                       # 'userVIP': 'unknown',
                       # 'aa_pageHistory': '''[{"n":"","t":"","p":""},{"n":"CSCA: W: Homepage","t":"Home","p":"/"}]''',
                       'JSESSIONID': session,
                       # 'userStatus': 'registered'
                   }, json={"optIn": False,
                            "firstName": "Prince",
                            "lastName": "David",
                            "uid": "fddq32d@chefkochkuchen.com",
                            "password": "Allo1234$",
                            "birthday": "02/13/1998",
                            "wantToBeVip": False}
                   )
    print(response.text)
    print(response.content)

#test_get_datadome()
#test_get_csrfToken()
test_create_account("ea0cf97b-798c-4ff7-aec2-2410e71bd53f","1vhp9nmoy4wz31wmr1nundoyn0.fzcexflapipdb928881")