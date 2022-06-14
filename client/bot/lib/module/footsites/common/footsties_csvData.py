from util.fileInterface.csv_interface import CSV_Data
import util.fileInterface.csv_interface as csvi

class Footsite_CSV(CSV_Data): 
    
    def __init__(self, file_index, data: list):
        super().__init__(file_index,data)
    
    def login_data(self):
        return {
            'uid': self.email,
            'password': self.passw
        }

    pass

class CSV_Test(CSV_Data):
    def __init__(self,email,sku) -> None:
        self.email=email
        self.sku=sku
        
    def __str__(self) -> str:
        return self.sku
class Footsite_Account_CSV(Footsite_CSV): 
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
    def save(self):
        pass
    
    def tokenData(self):
        return {
            'userid':self.email
        }
    pass

class Footsite_Entries_CSV(Footsite_CSV): 
    def __init__(self, file_index, list: list) -> None:
        super().__init__(file_index, list)
        self.sku=list[4]
        self.reserveId=list[5]
        self.customerId=list[6]
        self.cartId=list[7]
        self.ccore=list[8]
    
    def __eq__(self, __o: object) -> bool:
        __o: CSV_Test
        return super.__eq__(__o) and self.sku==__o.__str__()
    pass

class Footsite_Win_CSV(Footsite_CSV): 
    pass
