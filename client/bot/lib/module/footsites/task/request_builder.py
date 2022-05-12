from request_cs import  RequestCS_Account, RequestCS_Auth, RequestCS_Confirm, RequestType,setNewName
from rnd_account import  gen_all_account
from link_grabber import load_allToken
from proxie_parser import load_proxy
from text_interface import file_to_list,user_agents
from csv_interface import ListBuilder_Account, listBuilder
from random import choice

proxyList=load_proxy()
userAgentsList=file_to_list(file=user_agents)


def createRequest_NS(requestType,newName:tuple=None,names:list=None):
    
    if requestType==RequestType.NAMES:
        #FIXME Verifier si sa marche
        first,last=newName
        setNewName(first=first,last=last)
        pass
    
    List:list=[]
    for data in ListBuilder_Account(names,True).build():
        proxy=choice(proxyList) 
        userA=choice(userAgentsList)
        List.append(RequestCS_Auth(proxie=proxy,useragents=userA,account=data,requestType=requestType))

    return List

def createRequestAcount(amount:int):
    List:list=[]
    for account in gen_all_account(amount):
        proxy=choice(proxyList)
        userA=choice(userAgentsList)
        List.append(RequestCS_Account(account=account,proxie=proxy,useragents=userA))
    return List
    
def createRequestConfirm():
    List:list=[]
    for token in load_allToken():
        proxy=choice(proxyList)
        userA=choice(userAgentsList)
        List.append(RequestCS_Confirm(activationToken=token,proxie=proxy,useragents=userA))
    return List
   
  
   
#Implementer plus tard
 
#raise NotImplementedError
   
def createSingleChangeNameRequest(email:str,first,last):
    setNewName(first,last)
    pass
    
def manualRequest():
    pass
