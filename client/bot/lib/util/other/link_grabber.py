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
    """
    It connects to the gmail account, then it extracts the mail from the sender, then it extracts the
    link from the mail, then it writes the link in a file
    
    :param file: the file to write the activation token to
    :param fromWho: the sender's email address
    :param subjet: the subject of the email
    :param module: int
    :type module: int
    :return: A list of links
    """
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
    """
    It takes a list of strings, and returns a list of strings
    
    :param var: IMAP4_SSL
    :type var: IMAP4_SSL
    :param data: list of emails
    :param module: int
    :type module: int
    :return: A list of links
    """
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
    """
    It takes an IMAP4_SSL object, a sender's email address, and a subject line as input, and returns a
    list of message IDs
    
    :param var: IMAP4_SSL - This is the variable that contains the IMAP4_SSL object
    :type var: IMAP4_SSL
    :param fromWho: The email address of the sender
    :type fromWho: str
    :param subject: The subject of the email you want to extract
    :type subject: str
    :return: A list of message IDs
    """
    var.select("INBOX")
    _, result = var.search(None,f'(FROM "{fromWho}")',
                           f'(SUBJECT "{subject}")', 'UNSEEN')
    data = result[0].split()
    status(f"Total Messages from {fromWho}:  {len(data)}")
    return data


def load_allToken(file):
    """
    It takes a file, reads it line by line, and creates an ActivationToken object for each line
    
    :param file: the file that contains the tokens
    :return: A list of ActivationToken objects.
    """
    list_link=[]
    for element in file_to_list(file):
        list_link.append(ActivationToken(str(element)))

    return list_link

class ActivationToken:
    """
    It's a class that represents an activation token
    
    """
    def __init__(self, token:str) -> None:
        self.token:str = token

    def to_json(self):
        return {"activationToken": self.token}

    def __repr__(self) -> str:
        return self.token
