import csv
import os
from pyexcel import sheet
import pyexcel as pe
from print_cli import print_error

account = "Accounts.csv"
entries = "Entries.csv"
auto_conf = ""
testAcc = "Test.csv"
mapFile={
    "a":account,
    "e":entries
}

def parse_txtToCSVAccount(line: str):
    pass

def waitlist(id:str):
    pass

def test():
    sheet = pe.get_sheet(file_name=testAcc, name_columns_by_row=0)
    cpt=0
    for s in sheet:
        print(cpt,s,sep="-")
        cpt+=1
        
        
    print(sheet[0,"Email"])
    #sheet.save_as(testAcc)
    # print(sheet)


class CSV_Data:
    def __init__(self, file_index, list: list) -> None:
        self.file_index = file_index
        self.lname = list[0]
        self.fname = list[1]
        self.email = list[2]
        self.passw = list[3]
        self.fullName = self.fname+self.lname    

    def __repr__(self) -> str:
        return self.email

    def __str__(self) -> str:
        return f"{self.file_index}-{self.email}"

    def __eq__(self, __o: object) -> bool:
        __o: CSV_Test
        return self.email == __o.__repr__()

    def login_data(self):
        return {
            'uid': self.email,
            'password': self.passw
        }

    def save(self):
        pass
    
    def tokenData(self):
        return {
            'userid':self.email
        }
    
   
    pass

class CSV_Account(CSV_Data):

    def __init__(self, file_index, data: list):
        super().__init__(file_index,data)
        self.customerID=None
        self.cCore=None
        self.idReady = False
        if  not data[4]=='':
            self.idReady = True
            self.customerID=data[4]
            self.cCore=data[6]    
    def change_name(self,first, last):
        pass
    pass

class CSV_Entries(CSV_Data):
    def __init__(self, file_index, list: list) -> None:
        super().__init__(file_index, list)
        self.sku=list[4]
        self.reserveId=list[5]
        self.customerId=list[6]
        self.cartId=list[7]
    
    def __eq__(self, __o: object) -> bool:
        __o: CSV_Test
        return super.__eq__(__o) and self.sku==__o.__str__()
        
    pass

class CSV_Test(CSV_Data):
    def __init__(self,email,sku) -> None:
        self.email=email
        self.sku=sku
        
    def __str__(self) -> str:
        return self.sku
        
    
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

class ListBuilder_Account(ListBuilder):
    
    def __init__(self, names, active) -> None:
        super().__init__("a", names)
        self.active=active
    
    def condition(self, s,cpt):
        val=CSV_Account(cpt,s)
        if self.active:
                if not val.idReady:
                        self.list.append(val)
        else:
            self.list.append(val)
        
 
    pass

class ListBuilder_Entries(ListBuilder):
    
    def __init__(self,names) -> None:
        super().__init__("e", names)
        
    def condition(self, s, cpt):
        self.list.append(CSV_Entries(cpt,s))
    
    pass
#==========================================

def createFileCopy(file):
    pass

def appendAccount_csv(data: tuple):
    with open(account, 'a', newline='') as csvAccount:
        writer = csv.writer(csvAccount)
        writer.writerow(data)

def initialize():
    pass

def updateIds(data:CSV_Account):
    
    sheet = pe.get_sheet(file_name=mapFile.get('a'), name_columns_by_row=0)
    index=data.file_index
    sheet[index,"CustomerID"]=data.customerID
    sheet[index,"CCore"]=data.cCore
    saveFile(sheet,mapFile.get('a'))
    pass

def updateName(data:CSV_Data):
    
    raise NotImplemented
    
    sheet = pe.get_sheet(file_name=testAcc, name_columns_by_row=0)
    index=data.file_index
    sheet[index,"FirstName"]=data.fname
    sheet[index,"LastName"]=data.lname
    saveFile(sheet,testAcc)
    pass

def updateEntry(data:CSV_Entries):
    
    raise NotImplementedError
    
    sheet = pe.get_sheet(file_name=entries, name_columns_by_row=0)
    index=data.file_index
    sheet[index,"Reserveid"]=data.reserveId
    saveFile(sheet,entries)

def listBuilder(file,active:bool=False,name:list=None):
    List:list =[]
    try:
        if file=="e" and active:
            raise Exception()
        sheet=pe.get_sheet(file_name=mapFile.get(file), name_columns_by_row=0)
        if file=="e":
            pass
        elif file=="a":
            cpt=0
            for s in sheet:
                val = CSV_Account(cpt,s)
                if not name == None and name.__contains__(val.fname):
                    continue
                if active:
                    if not val.idReady:
                        List.append(val)
                else:
                    List.append(val)
                cpt+=1
    except:
        pass
    #print(List)
    return List

def search(email:str,list:list,sku=None):
    #FIXME tester
    temp=CSV_Test(email,sku)
    for element in list:
        element:CSV_Data
        print(element)
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
    #index=find("e",email)
    
    pass

def deleteRow(email:str):
    index=find("a",email)
    print(index)
    delete(index,testAcc)
    
def delete(index,file):
   try:
       sheet= pe.get_sheet(file_name=file, name_columns_by_row=0)
       sheet.delete_rows([index])
       saveFile(sheet,testAcc)
       return True,"Value deleted !"
    
   except TypeError:
       return False,"Value Not Found..."
    
def saveAll(src,dest):
    sheet=pe.get_sheet(file_name=src, name_columns_by_row=0)
    saveFile(sheet,dest)
    
def getRow(email):
    find("")

    

#==========================================


