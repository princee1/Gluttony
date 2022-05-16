from string import ascii_lowercase,digits,ascii_uppercase
from random import choice,randint

max_lenght_pass=15
special_char="!@#$%"

def gen_birthday():
   return f"{format_date(12)}/{format_date(29)}/{randint(1980,2001)}"

def format_date(max:int):
    return format(randint(1,max),"02d")

def gen_password():
    
    return choice(ascii_uppercase).__add__(''.join(choice(ascii_lowercase)for x in range(4))).__add__(
        ''.join(choice(digits) for x in range(3))).__add__(choice(special_char))
    
def gen_number():
    return ''.join(choice(digits)for x in range(5))    
