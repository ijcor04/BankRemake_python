class Account:
    
    def __init__(self,Accnum,type,name,bal):
        self._Accnum = Accnum
        self.type = type
        self.name = name
        self._bal= bal
        
    def getAccnum(self): 
        return self._Accnum
    def get_type(self):
        return self.type
    def get_name(self):
        return self.name
    def get_accbal(self):
        return self._bal
    
    def set_Accnum(self,x):
        self._Accnum = x
    def set_type(self, x):
        self.type = x
    def set_name(self, x):
        self.name = x
    def set_acc_bal_(self, x):
        self._bal = x

class Date:

    def __init__(self, m, d, y):
        self.month = m
        self.day = d
        self.year = y

    def get_month(self):
        return self.month 
    def get_day(self):
        return self.day
    def get_year(self):
        return self.year
    
    def set_month(self, m):
        self.month = m
    def set_day(self,d):
        self.day = d
    def set_year(self,y):
        self.year = y

    

    


        
