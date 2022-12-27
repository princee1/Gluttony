import os
from configparser import DEFAULTSECT, ConfigParser,NoOptionError
#from print_cli import success,error,print_info

# Reading the properties file and storing it in a dictionary.
properties="Properties.properties"
config=ConfigParser(comment_prefixes='#',delimiters="=")
config.read(properties)

# Defining the section of the config file.
USER_KEYSECTION=DEFAULTSECT
USER_OPTIONSECTION="OPTIONS" 

def getValue(option,section):
    """
    If the option exists in the section, return the value. 
    If the option does not exist in the section, return None.
    
    :param option: The option you want to get the value of
    :param section: The section of the config file you want to get the value from
    :return: The value of the option in the section.
    """
    try:
        return config.get(option=option,section=section)
    except NoOptionError: 
        return None

def addValue(option,value,section):
    """
    It adds a value to a section in the config file
    
    :param option: The option to add
    :param value: The value you want to add
    :param section: The section of the config file you want to add the option to
    """
    value={option:value}
    config.read_dict({section:value})
    save()
    pass

def setValue(option,value,section):
    """
    It sets the value of the option in the section to the value
    
    :param option: The option you want to set
    :param value: The value you want to set the option to
    :param section: The section of the config file you want to set the option in
    """
    config.set(section,option,value)
    save()
    pass

def deleteValue(option,section):
    """
    It deletes a value from a section in the config file
    
    :param option: The option to delete
    :param section: The section of the config file
    """
    config.remove_option(section,option)
    save()
    pass

def save():
    """
    It saves the config file.
    """
    with open(properties, 'w') as configfile:
        config.write(configfile)

#TODO reset user option
@NotImplemented
def reset():
    raise NotImplemented
    save()
    pass

# The user bot key
USER_KEY=getValue("key",USER_KEYSECTION)
