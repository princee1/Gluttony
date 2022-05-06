from random import choice
from proxie_parser import Proxy, load_proxy
from link_grabber import load_allToken
import text_interface as ti
import print_cli as ui
from request_cs import RequestCS_Account, RequestCS_Auth, RequestCS_Confirm, RequestCS_IDS,RequestType
from rnd_account import Account
import csv_interface as ci
from request_cs import RequestType
from random import choice
from request_builder import createRequest_NS, createRequestAcount
from seqTask_manager import startAllTask

list_userAgents = ti.file_to_list(ti.user_agents)
list_proxy = load_proxy()

# 'isometric3'



def genAccount():
    try:
        amount = int(input("How many account do you want to gen: "))
        for x in range(amount):
            test_Account()
    except ValueError:
        ui.print_error("Error d'écriture")

def test_Account():
    rq = RequestCS_Account(account=Account("Prince", "Madzou"), proxie=choice(
        list_proxy), useragents=choice(list_userAgents))
    status, rep = rq.request()
    if status:
        ui.print_succes(rep)
        ci.appendAccount_csv(rq.account.writeInFile())
    else:
        ui.print_error(rep)

def test_confirm():
    for token in load_allToken():
        rq = RequestCS_Confirm(activationToken=token, proxie=choice(
            list_proxy), useragents=choice(list_userAgents))
        status, rep = rq.request()
        if status:
            ui.print_succes(rep)
            # ci.appendAccount_csv(rq.account.writeInFile())
        else:
            ui.print_error(rep)

def test_auth():
    ip,port,user,passw="34.149.128.53:9200:country-ca-session-a1281665a194419ea3eb3a6f65712bfb:bb7d9157-86da-4117-9a35-e2fab09f3990".split(":")
    proxie= Proxy(ip,port,user,passw)
    p=choice(list_proxy)
    u=choice(list_userAgents)
    req = RequestCS_Auth(account=ci.CSV_Data(-1,["Madzou","Prince David","mxdzz.bus04@gmail.com","Snkrs20201$","","","",""]),proxie=p,
                         useragents=u,requestType=RequestType.IDS)
    status, rep = req.request()
    if status:

        ui.print_succes(rep)
        status2,rep2= req.succes_method()
        if status2:
            #ui.print_succes(rep2)
            print(req.second_rqcs.data)
        else:
            ui.print_error(rep2)
        
    else:
        ui.print_error(rep)

def test_ids():
    req = RequestCS_Auth(None,'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
                  ci.CSV_Account(file_index=22,data=['Prince','Madzou','PrinceMadzou89064@chefkochkuchen.com','Allo1234$','','','','']),RequestType.IDS )
    status,rep=req.request()
    print(rep)
    if status:
        status,rep=req.succes_method()
        print(rep)
# ================

def taskTest():
    ui.print_status("Initializing Tasks... Might Take A While")
    startAllTask(createRequest_NS(requestType=RequestType.IDS))

#test_ids()

def taskaAcc():
    ui.print_status("Initializing Tasks... Might Take A While")
    startAllTask(createRequestAcount(20))
    

#test_auth()