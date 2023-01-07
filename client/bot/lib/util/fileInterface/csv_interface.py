import csv
from pyexcel import sheet
import pyexcel as pe
from print_cli import error
    
# Classes =======================================================
class CSVData:
    """
     The class CSVData is a class that represents a single row of data from a CSV file. 
     
     The class has a constructor that takes a list of strings and assigns the first four elements of the
     list to the class variables lname, fname, email, and passw. 
     
     The class also has a constructor that takes a single string and assigns it to the class variable
     email. 
     
     The class has a method __repr__ that returns the value of the class variable email. 
     
     The class has a method __str__ that returns a string that contains the value of the class variable
     file_index and the value of the class variable email. 
     
     The class has a method __eq__ that compares the value of the class variable email to the value of
     the class variable email of the object passed to the method. 
     
     The class has a method pass that does nothing. 
     
     The class has a class variable full
    """
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
    
    def updateValue(self,file,*args):
        updateValue(file,args)
        pass
    
    def updateName(self,file,fname,lname):
        self.lname=lname
        self.fname=fname
        updateName(file,self)

    pass

class ListBuilder:
    """
    It reads a file and builds a list based on the content of the file
    """
    def __init__(self,file,names=None) -> None:
        self.initSheet(file)
        self.names=names
        self.build()
        pass

    def condition(self,row,cpt):
        pass
    
    def build(self):
        """
        It takes a row from a spreadsheet, and if the row meets a certain condition, it adds it to a list
        """
        self.list=[]
        cpt=0
        for row in self.sheet:
            if not self.names == None and not self.names.__contains__(row[0]): #FIXME plus tard avec full name
                    continue
            self.condition(row,cpt)
            cpt+=1
 
    def initSheet(self,file):
        """
        It takes a file name as an argument and returns a sheet object
        
        :param file: the file name of the excel file
        """
        self.sheet=pe.get_sheet(file_name=file, name_columns_by_row=0)
        
 
    pass
# Interface function ==========================================

def appendAccount_csv(file,data: tuple):
    """
    It opens the file in append mode, creates a writer object, and writes the data to the file
    
    :param file: the file name
    :param data: tuple
    :type data: tuple
    """
    with open(file, 'a', newline='') as csvAccount:
        writer = csv.writer(csvAccount)
        writer.writerow(data)
        
def updateValue(file,data,*args):
    """
    It takes a file, a data object, and updates the file with the data object
    
    :param file: the file to update
    :param data: the data to be written to the file
    :type data: CSVData
    """
    
    sheet = pe.get_sheet(file_name=file, name_columns_by_row=0)
    index=data.file_index
    #TODO le rendre plus general
    #sheet[index,"CustomerID"]=data.customerID
    #sheet[index,"CCore"]=data.cCore
    saveFile(sheet,file)
    pass

def updateName(file,data:CSVData):
    """
    It takes a file name and a CSVData object as parameters, and then updates the first and last name of
    the person in the file at the index specified in the CSVData object
    
    :param file: the file name
    :param data: CSVData
    :type data: CSVData
    """
  
    sheet = pe.get_sheet(file_name=file, name_columns_by_row=0)
    index=data.file_index
    sheet[index,"FirstName"]=data.fname
    sheet[index,"LastName"]=data.lname
    saveFile(sheet,file)
    pass

def saveFile(sheet:sheet.Sheet,destFile):
    """
    It takes a sheet object and a destination file name and saves the sheet to the destination file
    
    :param sheet: the sheet object you want to save
    :type sheet: sheet.Sheet
    :param destFile: The file you want to save the sheet to
    """
    sheet.save_as(destFile)
   
def copyRow(email:str,sku:str):
    #TODO implementer plus tard
    pass

def delete(index,file):
    """
    It deletes the row at the index specified in the file specified
    
    :param index: The index of the row you want to delete
    :param file: The name of the file you want to delete from
    :return: A tuple of two values.
    """
    try:
       sheet= pe.get_sheet(file_name=file, name_columns_by_row=0)
       sheet.delete_rows(index)
       saveFile(sheet,file)
       return True,"Value deleted !"
    
    except TypeError:
       return False,"Value Not Found..."
    
def saveAll(src,dest):
    """
    It takes a source file and a destination file, and then it opens the source file, and then it saves
    the source file to the destination file
    
    :param src: The source file
    :param dest: The destination file name
    """
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
