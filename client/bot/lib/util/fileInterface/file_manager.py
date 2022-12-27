import os,sys,time
#from properties_interface import properties

settings='Settings.json'
properties="Properties.properties"
userLockFile="user.glock"
command=f"attrib +h {userLockFile}"

FOOTSITE_INDEX=0
ADIDAS_INDEX=1
DATA_DIRNAME="data"

moduleList=["Footsite","Adidas"]
commondata="CommonDataFiles"

generalFiles=["Bulk_names.txt","Proxy.txt","Domains.txt"]
footsitesFiles=["ActivationToken.txt,Accounts.csv,Settings.json"]    
adidasFiles=["Accounts.csv,Settings.json"]


def fileCreator(filename):
    try:
        open(f"{filename}","x")    
    except:
        pass

def writeFile(filename,buffer,inputMode="w"):
    try:
        with open(filename,inputMode) as fd:
            fd.write(buffer)
            fd.close()
    except:
        pass
    pass


def createDirectory(moduleName):
    #TODO faire pour les sous-dossiers aussi 
    try:
        os.mkdir(path=moduleName)
    except:
        pass
    pass


def createSettingsFile():
    fileCreator(settings)
    #TODO ecrire dans le fichier
    writeFile(settings,'''{}''')
    pass

def createPropertiesFile():
    fileCreator(properties)
    writeFile(properties,"[DEFAULT]","a")
    writeFile(properties,"","a")
    writeFile(properties,"[OPTIONS]","a")
    pass

def initUserBotData():
    
    hashTime = hash(time.time())
    fileCreator(userLockFile)
    writeFile(userLockFile,f"new-time~{hashTime}")
    os.system(command=command)
    
    ##createDirectory(toPath(commondata))
    createDirectory(DATA_DIRNAME)
    (createDirectory(module) for module in moduleList)
    
    createPropertiesFile()
    createSettingsFile()
    
    (fileCreator(file) for file in generalFiles)
    
    #TODO create file for footsite module
    #TODO create file for adidas module
    
    
    pass

def isNewBotData():
    try:
        open(userLockFile,"r")
    except:
        initUserBotData()


def dataPath():
    return f"{DATA_DIRNAME}/"

def footsitePath():
    return f"{dataPath()}{moduleList[FOOTSITE_INDEX]}/"

def adidasPath():
    return f"{dataPath()}{moduleList[ADIDAS_INDEX]}/"
    


