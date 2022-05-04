from rnd_pass_birth import gen_birthday, gen_password, gen_number
from text_interface import rnd_fname, rnd_lname, file_to_list, domain, names
from random import choice

rnd_lastName = file_to_list(rnd_lname)
rnd_firstName = file_to_list(rnd_fname)
fullNames = file_to_list(names)
dom = file_to_list(domain)



def gen_email():
    return choice_toStr(rnd_firstName).__add__(
        choice_toStr(rnd_lastName)).__add__(gen_number()).__add__("@").__add__(choice_toStr(dom))


def gen_list_account(amount: int, full_name: tuple):
    first, last = full_name
    list = []
    for x in range(amount):
        list.append(Account(firstName=first, lastName=last))

    return list


def choice_toStr(list):
    return str(choice(list))


def gen_all_account(amount: int):
    list = []
    for person in fullNames:
        temp = str(person).split(":")
        full_name = (temp[0], temp[1])
        list.extend(gen_list_account(amount, full_name))

    return list


class Account:

    def __init__(self, firstName, lastName):
        self.firstName: str = firstName
        self.lastName: str = lastName
        self.email = gen_email()
        self.password = gen_password()
        self.birthday = gen_birthday()

    def to_json(self):
        return {
            "optIn": False,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "uid": self.email,
            "password": self.password,
            "birthday": self.birthday,
            "wantToBeVip": False
        }
    
    def writeInFile(self):
        return (self.firstName,self.lastName,self.email,self.password)

    def __str__(self) -> str:
        return self.firstName+"\n"+self.lastName+"\n"+self.birthday+"\n"+self.email+"\n"+self.password

    def __repr__(self) -> str:
        return self.email

