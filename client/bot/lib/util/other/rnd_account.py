from rnd_accData import gen_birthday, gen_password, gen_number , BirthFormat
from util.fileInterface.text_interface import file_to_list
from file_manager import commonFilePath
from constant import names,domain,rnd_lname,rnd_fname
from random import choice
from util.fileInterface.csv_interface import appendAccount_csv

rnd_lastName = file_to_list(commonFilePath(rnd_lname))
rnd_firstName = file_to_list(commonFilePath(rnd_fname))
fullNames = file_to_list(commonFilePath(names))
dom = file_to_list(commonFilePath(domain))


def gen_email():
    """
    It takes a random first name, a random last name, a random number, and a random domain, and
    concatenates them together to form an email address
    :return: A string
    """
    return choice_toStr(rnd_firstName).__add__(
        choice_toStr(rnd_lastName)).__add__(gen_number()).__add__("@").__add__(choice_toStr(dom))


def gen_list_account(amount: int, full_name: tuple):
    first, last = full_name
    list = []
    for _ in range(amount):
        list.append(Account(firstName=first, lastName=last))

    return list


def choice_toStr(list):
    """
    It takes a list of strings and returns a random string from that list
    
    :param list: The list of items to choose from
    :return: A random element from the list.
    """
    return str(choice(list))


def gen_all_account(amount: int):
    list = []
    for person in fullNames:
        temp = str(person).split(":")
        full_name = (temp[0], temp[1])
        list.extend(gen_list_account(amount, full_name))

    return list



class Account:

    def __init__(self, firstName, lastName,birthdatType:BirthFormat):
        self.firstName: str = firstName
        self.lastName: str = lastName
        self.email = gen_email()
        self.password = gen_password()
        self.birthday = gen_birthday(birthdatType)

    def to_json(self):
        pass
    
    def appendToFile(self,file):
        appendAccount_csv(file,self.writeInFile())
        pass

    def writeInFile(self):
        return (self.firstName,self.lastName,self.email,self.password)

    def __str__(self) -> str:
        return self.firstName+"\n"+self.lastName+"\n"+self.birthday+"\n"+self.email+"\n"+self.password

    def __repr__(self) -> str:
        return self.email

