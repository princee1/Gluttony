from util.taskmanager.requestable_interface import Requestable
import headers_gen as hg
from requests import Session


class FootsiteSession(Requestable,Session):
    
    pass

class FoositeAuth(FootsiteSession):
    pass