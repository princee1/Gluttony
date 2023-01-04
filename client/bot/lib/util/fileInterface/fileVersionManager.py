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
    """
    It takes two arguments, a source file and a destination file, and copies the source file to the
    destination file
    
    :param source: The source file to copy
    :param dest: The destination folder
    """
    command = f"copy {source} {dest} /Y"
    system(command)
    pass

def createTempFile(source,dest,vsrc):
    """
    It creates a temporary file in the destination folder, and then copies the source file to the
    destination folder
    
    :param source: The source file
    :param dest: The destination file
    :param vsrc: the path to the settings file
    """
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
    """
    It deletes a file
    
    :param file: The file to be deleted
    """
    command = f"del {file} /F"
    system(command)
    pass


def checkFile(file,vsrc):
    """
    It checks if the file exists in the versions source, if it does, it checks if the file is smaller
    than the one in the versions source, if it is, it copies the file from the versions source to the
    file, if it isn't, it deletes the file and removes it from the versions source
    
    :param file: the file to be checked
    :param vsrc: the path to the settings file
    """
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