import json5 as js



def loadJson(file):
    try:
        with open(file, "r") as fd:
            return js.load(fd, "utf-8")
    except:
        return None
    
def writeJson(json,file):
    try:
        with open(file, "w") as fd:
            js.dump(json,fd)
    except:
        pass
    
class Settings():
    def __init__(self,module) -> None:
        self.modulePath=module
        self.settings:dict=loadJson(module)
        
    def setValue(self,key,data):
        self.settings[key]=data
        self.save()
        pass   
    
    def getValue(self,key):
        return self.settings[key]

    def save(self):
        writeJson(self.settings,self.modulePath)
        pass
    
    @DeprecationWarning
    def addData(self):
        pass
    @DeprecationWarning
    def deleteData(self):
        pass

    pass