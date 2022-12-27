import re
from imaplib import IMAP4_SSL
from text_interface import file_to_list, write_list, email as e
from urllib.parse import unquote
from json_interface import Settings
from print_cli import error,status,success

settings = Settings()
e_mail=""
password=""

gmail_host = 'imap.gmail.com'


link_prefix = {0:"https://www.champssports.ca/user-activation.html?activationToken=3D"}


def grab_activationToken(file,fromWho,subjet,module:int):
    var:IMAP4_SSL =IMAP4_SSL(host=gmail_host)
    status,message=var.login(user=e_mail, password=password)
    if status=='OK':
        success(str(message[0]))
    else :
        error(str(message[0]))
        return
    
    data = extract_mail(var,fromWho,subjet,module)
    list_link = extractLink(var, data)
    write_list(file,list_link)

def extractLink(var:IMAP4_SSL, data,module:int):
    list_link = []

    for m in data:
        _, mail = var.fetch(m, '(RFC822)')

        temp_list = re.findall("(?P<url>https?://[^\s]+)", str(mail))
        #print(temp_list)
        size = len(temp_list)
        if size == 20:
            index = -3
        else:
            index = -4
            
    value = str(temp_list[index]).replace("=\\r\\n", "").split("&")[0].removeprefix(link_prefix.get(module))
    list_link.append(unquote(value))
    return list_link

def extract_mail(var:IMAP4_SSL,fromWho:str,subject:str):
    var.select("INBOX")
    _, result = var.search(None,f'(FROM "{fromWho}")',
                           f'(SUBJECT "{subject}")', 'UNSEEN')
    data = result[0].split()
    status(f"Total Messages from {fromWho}:  {len(data)}")
    return data


def load_allToken(file):
    list_link=[]
    for element in file_to_list(file):
        list_link.append(ActivationToken(str(element)))

    return list_link

class ActivationToken:
    def __init__(self, token:str) -> None:
        self.token:str = token

    def to_json(self):
        return {"activationToken": self.token}

