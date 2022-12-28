import csv
from pyexcel import sheet
import pyexcel as pe
from print_cli import error


def test():
    sheet = pe.get_sheet(file_name=testAcc, name_columns_by_row=0)
    cpt=0
    for s in sheet:
        print(cpt,s,sep="-")
        cpt+=1
    
    print(sheet[0,"Email"])
    #sheet.save_as(testAcc)
    # print(sheet)
class CSVData:
    def __init__(self, file_index, list: list) -> None:
        self.file_index = file_index
        self.lname = list[0]
        self.fname = list[1]
        self.email = list[2]
        self.passw = list[3]
        self.fullName = self.fname+self.lname   
        
    def __init__(self,email):
        self.email=email 

    def __repr__(self) -> str:
        return self.email

    def __str__(self) -> str:
        return f"{self.file_index}-{self.email}"

    def __eq__(self, __o: object) -> bool:
        return self.email == __o.__repr__()

    pass

#FIXME: Tester les objet listbuilder
class ListBuilder:
    def __init__(self,file,names=None) -> None:
        self.list=[]
        self.initSheet(file)
        self.names=names
        pass

    def condition(self,s,cpt):
        pass
    
    def build(self):
        cpt=0
        for s in self.sheet:
            if not self.names == None and not self.names.__contains__(s[0]): #FIXME plus tard avec full name
                    continue
            self.condition(s,cpt)
            cpt+=1
        return self.list   
    
    def initSheet(self,file):
        self.sheet=pe.get_sheet(file_name=mapFile.get(file), name_columns_by_row=0)

    
    def __init__(self,names) -> None:
        super().__init__("e", names)
        
    def condition(self, s, cpt):
        self.list.append(CSV_Entries(cpt,s))
    
    pass
#==========================================

def appendAccount_csv(file,data: tuple):
    with open(file, 'a', newline='') as csvAccount:
        writer = csv.writer(csvAccount)
        writer.writerow(data)
        
def updateValue(file,data:CSVData,):
    
    sheet = pe.get_sheet(file_name=file, name_columns_by_row=0)
    index=data.file_index
    #TODO le rendre plus general
    sheet[index,"CustomerID"]=data.customerID
    sheet[index,"CCore"]=data.cCore
    saveFile(sheet,data)
    pass

def updateName(file,data:CSVData):
  
    sheet = pe.get_sheet(file_name=file, name_columns_by_row=0)
    index=data.file_index
    sheet[index,"FirstName"]=data.fname
    sheet[index,"LastName"]=data.lname
    saveFile(sheet,file)
    pass

def search(email:str,list:list):
    #FIXME tester
    temp=CSVData(email)
    for element in list:
        element:CSVData
        if element.__eq__(temp):
            return element.file_index
    return None

def saveFile(sheet:sheet.Sheet,destFile):
    sheet.save_as(destFile)

def find(file,email):
    list=listBuilder(file)
    return search(email,list)
   
def copyRow(email:str,sku:str):
    #TODO implementer plus tard
    pass

def deleteRow(email:str,file):
    index=find(file,email)
    delete([index],file)
    
def delete(index,file):
   try:
       sheet= pe.get_sheet(file_name=file, name_columns_by_row=0)
       sheet.delete_rows(index)
       saveFile(sheet,file)
       return True,"Value deleted !"
    
   except TypeError:
       return False,"Value Not Found..."
    
def saveAll(src,dest):
    sheet=pe.get_sheet(file_name=src, name_columns_by_row=0)
    saveFile(sheet,dest)
    
#TODO a faire
def getRow(find,email):
    find("")

# ========================== #TODO NOT IMPLEMENTED FUNCTION==========================================

def updateEntry():
    
    raise NotImplementedError
    
    sheet = pe.get_sheet(file_name=entries, name_columns_by_row=0)
    index=data.file_index
    sheet[index,"Reserveid"]=data.reserveId
    saveFile(sheet,entries)

def createFileCopy(file):
    pass

def parse_txtToCSVAccount(line: str):
    pass

def initialize():
    pass
