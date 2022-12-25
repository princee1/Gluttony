from string import digits,ascii_letters,hexdigits
from random import choice

len_session=24
alpha_numeric=digits.__add__(ascii_letters)
request_list=[8,4,4,4,12]
session_id_suffix=".fzcexflapipdb928881"

def request_id():
    """
    It takes a list of numbers, converts each number to a hexadecimal string, and joins them together
    with a hyphen
    :return: A string of hex numbers separated by dashes.
    """
    return '-'.join(hex_number(x) for x in request_list)  
    
def session_id():
    """
    It returns a string of length `len_session` (default: 32) consisting of random characters from the
    string `alpha_numeric` (default: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    followed by the string `session_id_suffix` (default: '_session')
    :return: A string of random characters of length len_session, plus the string session_id_suffix.
    """
    return ''.join(choice(alpha_numeric) for x in range(len_session)).__add__(session_id_suffix)

def hex_number(size:int):
    """
    It generates a random hexadecimal number of the specified size.
    
    :param size: the number of characters in the string
    :type size: int
    :return: A string of random hexadecimal digits.
    """
    return ''.join(choice(hexdigits.lower()) for x in range(size))
