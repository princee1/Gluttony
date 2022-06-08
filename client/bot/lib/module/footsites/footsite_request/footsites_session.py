from urllib.request import proxy_bypass
from client.bot.lib.util.other.proxie_parser import Proxy
from util.taskmanager.requestable_interface import Requestable
import headers_gen as hg
from requests import Session
from enum import Enum




##TODO: completer l'objet footsite session
datadome_url = "https://api-js.datadome.co/js/"
datadome_api_key = 'A55FBF4311ED6F1BF9911EB71931D5'

session_url_champs = "https://www.champssports.ca/api/v4/session"
auth_url_champs = 'https://www.champssports.ca/api/v4/auth'


class FootsiteType(Enum):
    CHAMPS=1
    FOOTLOCKER=2
    pass

class FootsiteSession(Requestable,Session):
    pass

class FoositeAuth(FootsiteSession):
    pass