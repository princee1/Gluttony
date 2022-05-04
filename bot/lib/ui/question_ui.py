#from __future__ import print_function, unicode_literals
from prompt_toolkit.styles.base import Style 
from whaaaaat import prompt,style_from_dict
from print_cli import print_principalOption


def selectOption(list:list,message):
    question={
        'type':'list',
        'name':'option',
        'message':message,
        'choices':list
    }
    return list.index(prompt(question).get('option'))
    
def checkBoxOption(list:list,message):
    listDict=[]
    for x in list:
        listDict.append({'name':x})

    question=[{
        'type':'checkbox',
        'name':'value',
        'message':message,
        'choices':listDict
    }]
    return prompt(question).get('value')  

def simpleQuestion(message:str):
    question=[
        {'type':'input',
        'name':'value',
        'message':message
        }  
    ]
    return prompt(question).get('value')

def confirm(message):
    question=[
        {
            'type':'confirm',
            'name':'value',
            'message':message
            
        }
    ]
   
    return prompt(question).get('value')

def addSeparator(list,index):
    pass


