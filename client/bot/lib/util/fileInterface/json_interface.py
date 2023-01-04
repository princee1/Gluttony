import json5 as js

def loadJson(file):
    """
    It tries to open the file, and if it can't, it returns None
    
    :param file: The file to load the JSON from
    :return: A dictionary
    """
    try:
        with open(file, "r") as fd:
            return js.load(fd, "utf-8")
    except:
        return None
    
def writeJson(json,file):
    """
    It takes a json object and a file name as input, and writes the json object to the file
    
    :param json: the json object to write to the file
    :param file: The file to read from
    """
    try:
        with open(file, "w") as fd:
            js.dump(json,fd)
    except:
        pass

class Settings():
    """
    It's a class that allows you to store and manipulate data in a json file
    
    """
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

    def addData(self,key,data):
        self.setValue(key,data)
        pass
    
    def deleteData(self,key):
        self.settings.pop(key)
        self.save()
        pass

    pass