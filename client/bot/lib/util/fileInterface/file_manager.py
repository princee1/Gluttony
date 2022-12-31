import os,sys,time

settings='Settings.json'
properties="Properties.properties"
userLockFile="user.glock"

FOOTSITE_INDEX=0
ADIDAS_INDEX=1

DATA_DIRNAME="data"
LOG_DIRNAME=".log"

MODULE_LIST=["Footsite","Adidas"]
commondata="CommonFiles"

MODULE_FILE={
    MODULE_LIST[FOOTSITE_INDEX]:["ActivationToken.txt,Accounts.csv,Settings.json"],
    MODULE_LIST[ADIDAS_INDEX]:["Accounts.csv,Settings.json"]
}

generalFiles=["Bulk_names.txt","Proxy.txt","Domains.txt"]

def fileCreator(filename):
    """
    It creates a file with the name of the argument passed to it.
    
    :param filename: The name of the file you want to create
    """
    try:
        open(f"{filename}","x")    
    except:
        pass

def writeFile(filename,buffer,inputMode="w"):
    """
    It writes a file.
    
    :param filename: The name of the file to write to
    :param buffer: The string to write to the file
    :param inputMode: The mode in which the file is opened, defaults to w (optional)
    """
    try:
        with open(filename,inputMode) as fd:
            fd.write(buffer)
            fd.close()
    except:
        pass
    pass

def toHideCmd(filename):
    command=f"attrib +h {filename}"
    os.system(command=command)
    

def createDirectory(dir):
    """
    It creates a directory.
    
    :param moduleName: the name of the module you want to create
    """
    #TODO faire pour les sous-dossiers aussi 
    try:
        os.mkdir(path=dir)
    except:
        pass
    pass

def createModule(module): 
    createDirectory(module)
    (fileCreator(module.__add__(file)) for file in MODULE_FILE.get(module))
    pass
    

def createSettingsFile():
    """
    It creates a file called settings.json and writes {} in it.
    """
    fileCreator(settings)
    #TODO ecrire dans le fichier
    writeFile(settings,'''{}''')
    pass

def createPropertiesFile():
    """
    It creates a file called properties.txt and writes the following to it:
    [DEFAULT]
    """
    fileCreator(properties)
    writeFile(properties,"[DEFAULT]","a")
    writeFile(properties,"","a")
    writeFile(properties,"[OPTIONS]","a")
    pass

def initUserBotData():
    """
    It creates a bunch of files and folders for the user's data
    """
    
    hashTime = hash(time.time())
    fileCreator(userLockFile)
    writeFile(userLockFile,f"new-time~{hashTime}")
    
    createDirectory(commondata)
    createDirectory(DATA_DIRNAME)
    (createModule(dataPath().__add__(mod)) for mod in MODULE_LIST)
    
    createPropertiesFile()
    createSettingsFile()
    
    (fileCreator(file) for file in generalFiles)
    
    #TODO create file for footsite module
    #TODO create file for adidas module
    
    
    pass

def isNewBotData():
    """
    If the userLockFile doesn't exist, create it.
    """
    try:
        open(userLockFile,"r")
    except:
        initUserBotData()

def commonFilePath(file):
    return f"{commondata}/{file}"

def dataPath(file=""):
    return f"{DATA_DIRNAME}/{file}"

def footsitePath(file):
    return f"{dataPath()}{MODULE_LIST[FOOTSITE_INDEX]}/{file}"

def adidasPath(file):
    return f"{dataPath()}{MODULE_LIST[ADIDAS_INDEX]}/{file}"

def logPath(file):
    return f"{LOG_DIRNAME}/{file}"


