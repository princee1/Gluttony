from string import digits,ascii_letters,hexdigits
from random import choice

len_session=24
alpha_numeric=digits.__add__(ascii_letters)
request_list=[8,4,4,4,12]
session_id_suffix=".fzcexflapipdb928881"

def request_id():
    return '-'.join(hex_number(x) for x in request_list)  
    
def session_id():
    return ''.join(choice(alpha_numeric) for x in range(len_session)).__add__(session_id_suffix)

def hex_number(size:int):
    return ''.join(choice(hexdigits.lower()) for x in range(size))
