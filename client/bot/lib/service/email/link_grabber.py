import re
from text_interface import file_to_list
from urllib.parse import unquote
from json_interface import Settings

link_prefix = {0:"https://www.champssports.ca/user-activation.html?activationToken=3D"}



def link_searcher(mail,module=0):
    """
    It takes a string, finds all the links in it, and returns the last link in the string
    
    :param mail: the email body
    :param module: 0 for the first module, 1 for the second module, defaults to 0 (optional)
    :return: The link that is being returned is the link that is being searched for.
    """
    temp_list = re.findall("(?P<url>https?://[^\s]+)", str(mail)) 
    size = len(temp_list)
    if size == 20:
        index = -3
    else:
        index = -4
    value = str(temp_list[index]).replace("=\\r\\n", "").split("&")[0].removeprefix(link_prefix.get(module))
    return unquote(value)


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
