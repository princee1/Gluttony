#from __future__ import print_function, unicode_literals
from prompt_toolkit.styles.base import Style
from whaaaaat import prompt, style_from_dict,Token,Separator
from print_cli import print_principalOption

#TODO sytle builder

style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#001aff',  # default
    #Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})

def selectOption(list: list, message) -> int:
    question = {
        'type': 'list',
        'name': 'option',
        'message': message,
        'choices': list
    }
    return list.index(prompt(question).get('option'))


def checkBoxOption(list: list, message):
    listDict = []
    for x in list:
        listDict.append({'name': x})

    question = [{
        'type': 'checkbox',
        'name': 'value',
        'message': message,
        'choices': listDict
    }]
    return prompt(question).get('value')


def simpleQuestion(message: str):
    question = [
        {'type': 'input',
         'name': 'value',
         'message': message,
         #'validator':lambda x:str(x)
         }
    ]
    return prompt(question).get('value')


def confirm(message) -> bool:
    question = [
        {
            'type': 'confirm',
            'name': 'value',
            'message': message
        }
    ]

    return prompt(question).get('value')


def enterPassWord(message):
    question = [{
        'type': 'password',
        'name': 'value',
        'message': message
    }
    ]
    return prompt(question).get('value')
    

def addSeparator(list, index):
    pass
