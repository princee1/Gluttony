import sys
from traceback import print_stack
from link_grabber import grab_activationToken
from request_cs import RequestType
from text_interface import file_to_list, names,email
from csv_interface import account
from print_cli import print_principalOption,print_error, print_status
from question_ui import addSeparator, confirm, checkBoxOption, selectOption, simpleQuestion, style_from_dict
from request_builder import createRequestAcount,createSingleChangeNameRequest,createRequestConfirm, createRequest_NS
from seqTask_manager import startAllTask
from request_cs import setNewName
from util import deleteValue,setDefaultValue,setValue,addValue,getAllUser,reset

listOptionChoice = ['[x] - Account Generator', '[x] - Confirm Account',
                    '[x] - Link Grabber', '[x] - Gathering IDS', '[x] - Change Name', '[x] - More', '[x] - Quit']

moreOption=['[x] - Data Path','[x] - Settings','[x] - Back']

pathOption=['[x] - Set Default Path','[x] - Add Path','[x] - Delete Path','[x] - Set Path','[x] - Save BackUp','[x] - Reset','[x] - Back']
optionMessage = {
    0: f'Create Footsites account and add it the {account}',
    1: f'Confirm All Links found in the {email}',
    2: f'Grab Footsites link found in your email',
    3: f'Gather the bypass data and save in the {account}',
    4: f'Change the full of an account and update or delete in the {account}',
    5: f'More option',
    6: 'Quitting...',
}
namesOption = file_to_list(names)
allName='All Names'
namesOption.append(f"{allName}: ")


def inputInt(message):
    error=True
    while error:
        try:
            string=simpleQuestion(message)
            return int(string)
        except:
            print_error(f"{string} is not a number")
            error = True
                
def selectName():
    if not confirm('Do you want to select name from BulkNames'):
        value:str
        value=simpleQuestion("Enter First Name Separted with ';' : ")
        list=[]
        for x in value.split(";"):
            list.append(x.strip())
        return   list
    else:
        list=[]
        for x in namesOption:
            x:str
            list.append(x.split(":")[0])
        
        listNames = checkBoxOption(list,"Select Names ")
        if listNames.__contains__(allName):
            return None
        return listNames

def getUser():
    user=selectOption(getAllUser(),'Select a name')
    return getAllUser()[user]

def pathOptionLoop():
    while True:
        option = selectOption(pathOption, 'Select An Option')
        if option == 0:
           value=getUser()
           setDefaultValue(value)
        if option == 1:
            name=simpleQuestion("Enter the repertory name")
            value=simpleQuestion("Enter the repertory path")
            addValue(name,value)
        if option == 2:
            value=getUser()
            deleteValue(value)
            pass
        if option == 3:
            name=getUser()
            value=simpleQuestion("Enter the new repertory path")
            setValue(name,value)
        if option == 4:
            
            pass
        if option == 5:
            reset
        if option == 6:
            break   

def moreOptionLoop(): 
     while True:
        option = selectOption(moreOption, 'Select An Option')
        #print_principalOption(optionMessage.get(option))
        if option == 0:
            pathOptionLoop()
        if option == 1:  
            pass
        if option == 2:
            break

def main():
    # TODO match case plus tard
    while True:
        option = selectOption(listOptionChoice, 'Select An Option')
        print_principalOption(optionMessage.get(option))
        if option==0:
            print('')
            value=inputInt("How many account do you to create ?")
            startAllTask(createRequestAcount(value))
        if option==1:
            print('')
            startAllTask(createRequestConfirm())
        if option==2:
            print('')
            grab_activationToken()
        if option==3:
            print('')
            names=selectName()
            reverse=confirm("Do you wanna reverse your Task list")
            print_status("Preparing the requests...")
            startAllTask(createRequest_NS(RequestType.IDS,names=names),reverse)
            pass
        if option==4:
            try:
                raise NotImplementedError()
                email=simpleQuestion("Enter the email account that you want to change name")
                first=simpleQuestion("Enter the new First Name")
                first=simpleQuestion("Enter the new Last Name")
                startAllTask(createSingleChangeNameRequest(email,first,last))
            
            except:
                print_error("Not Implemented Yet")
            pass
        if option==5:
            moreOptionLoop()  
        if option==6:
            print('')
            print_principalOption('Bye...')
            sys.exit()
        print('')

