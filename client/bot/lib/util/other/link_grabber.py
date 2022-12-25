import imaplib,re
from text_interface import file_to_list, write_list, email as e
from urllib.parse import unquote
from print_cli import*
from json_interface import e_mail,password
from print_cli import error,status,success




gmail_host = 'imap.gmail.com'
link_prefix = "https://www.champssports.ca/user-activation.html?activationToken=3D"


def grab_activationToken():
    var = imaplib.IMAP4_SSL(host=gmail_host)
    status,message=var.login(user=e_mail, password=password)
    if status=='OK':
        success(str(message[0]))
    else :
        error(str(message[0]))
        return
    
    var.select("INBOX")
    _, result = var.search(None,'(FROM "Champs Sports")',
                           '(SUBJECT "Finish Activating Your Account")', 'UNSEEN')
    data = result[0].split()
    status(f"Total Messages from Champs Sports:  {len(data)}")

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
            
        value = str(temp_list[index]).replace(
            "=\\r\\n", "").split("&")[0].removeprefix(link_prefix)
        list_link.append(unquote(value))

    write_list(file=e, data=list_link)

def load_allToken():
    
    list_link=[]
    for element in file_to_list(e):
        list_link.append(ActivationToken(str(element)))

    return list_link

class ActivationToken:
    def __init__(self, token:str) -> None:
        self.token:str = token

    def to_json(self):
        return {"activationToken": self.token}

