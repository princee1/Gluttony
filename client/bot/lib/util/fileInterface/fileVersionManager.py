#NOTE a chq type run, so chq run d'un task manager sauvegarde la version du fichier davant avec comme nom (fichier + date/heure)
#NOTE lire le nom du fichier, et recuperer la date et le heure
#NOTE si rien se passe je supprime le fichier de base sinon je fait rien (je le garde)
#NOTE comparer pour trouver le plus recent, et overide la version original

from time import strftime
from os import system
from file_manager import footsitePath,adidasPath

FOOTSITE = lambda x : footsitePath("Version")+f"/{x}"
ADIDAS= lambda x: adidasPath("Version")+f"/{x}"

def createTempFile(source,dest):
    command = f"copy {source} {dest} /Y"
    system(command)
    pass

def deleteTempFile(file):
    command = f"del {file} /F"
    system(command)
    pass


