import os
from configparser import DEFAULTSECT, ConfigParser,NoOptionError
#from print_cli import success,error,print_info

properties="Properties.properties"
config=ConfigParser(comment_prefixes='#',delimiters="=")
config.read(properties)

USER_KEYSECTION=DEFAULTSECT
USER_OPTIONSECTION="OPTIONS" 

def getValue(option,section):
    try:
        return config.get(option=option,section=section)
    except NoOptionError: 
        return None

def addValue(option,value,section):
    value={option:value}
    config.read_dict({section:value})
    save()
    pass

def setValue(option,value,section):
    config.set(section,option,value)
    save()
    pass

def deleteValue(option,section):
    config.remove_option(section,option)
    save()
    pass

def save():
    with open(properties, 'w') as configfile:
        config.write(configfile)

#TODO reset user option
@NotImplemented
def reset():
    raise NotImplemented
    save()
    pass


USER_KEY=getValue("key",USER_KEYSECTION)
