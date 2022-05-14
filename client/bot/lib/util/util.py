import os
from configparser import DEFAULTSECT, ConfigParser
from print_cli import print_succes,print_error,print_info
properties="Properties.properties"
config=ConfigParser(comment_prefixes='#',delimiters="=")
config.read(properties)
path_section="User Path"
defaultSec="DEFAULT USER NAME"
defaultPath=config[defaultSec]["name"]




#TODO Finir d'implementer le module 

def init(name,path):
    try:
        raise NotImplemented
        config.add_section(defaultSec)
        config[defaultSec][name]=path
        save()
    except FileNotFoundError():
        pass
    except:
        pass
    pass

def reset():
    raise NotImplemented
    
    save()
    pass

def setDefaultValue(value:str):
    list=config.options(path_section)
    if list.__contains__(value):
        config["DEFAULT USER NAME"]["name"]=value
    
    else:
        print_error("Value not found in the file...")
    
    save()
    pass

def addValue(option,value):
    value={option:value}
    config.read_dict({path_section:value})
    save()
    pass

def setValue(option,value):
    config.set(path_section,option,value)
    save()
    pass

def getAllUser():
    return config.options(path_section)

def printAllUser():
    
    for x in getAllUser():
        print(config.get(path_section,x))
    
def deleteValue(option):
    config.remove_option(path_section,option)
    save()
    pass

def save():
    with open(properties, 'w') as configfile:
        config.write(configfile)

def to_path(file: str):
    return f"data\\{file}"

def saveBackUp(user,type):
    pass


