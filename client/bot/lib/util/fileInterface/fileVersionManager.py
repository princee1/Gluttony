#NOTE a chq type run, so chq run d'un task manager sauvegarde la version du fichier davant avec comme nom (fichier + date/heure)
#NOTE lire le nom du fichier, et recuperer la date et le heure
#NOTE si rien se passe je supprime le fichier de base sinon je fait rien (je le garde)
#NOTE comparer pour trouver le plus recent, et overide la version original

from time import strftime
from os import system
from os.path import getsize
from file_manager import footsitePath,adidasPath
from json_interface import Settings

FOOTSITE = lambda x : footsitePath("Version")+f"/{x}"
ADIDAS= lambda x: adidasPath("Version")+f"/{x}"


def copy(source,dest):
    command = f"copy {source} {dest} /Y"
    system(command)
    pass

def createTempFile(source,dest,vsrc):
    versions = Settings(vsrc)
    tempDict={"time":strftime("%D %M %Y %H:%M:%S"),
              "size":getsize(source),
               "dest":dest}
    versions.setValue(source,tempDict)
    del versions
    del tempDict
    copy(source,dest)
    pass

def deleteTempFile(file):
    command = f"del {file} /F"
    system(command)
    pass


def checkFile(file,vsrc):
    try:
        versions = Settings(vsrc)
        tempdict=versions.getValue(file)
        if getsize(file)< tempdict["size"]:
            copy(tempdict["dest"],file)
        else :
            deleteTempFile(file)
            versions.deleteData(file)
        del versions
        del tempdict
    except:
        pass 