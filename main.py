
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

    user_in = 0
    while (user_in != 5):
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        user_in = int(input("Enter your choice: "))
        if user_in == 1:
            Accnum = input("Enter Account Number: ")
            type = input("Enter Account Type: ")
            name = input("Enter Account Name: ")
            bal = float(input("Enter Account Balance: "))
            account = Account(Accnum, type, name, bal)
            print("Account created successfully!")
        elif user_in == 2:
            amount = float(input("Enter amount to deposit: "))
            account.set_acc_bal_(account.get_accbal() + amount)
            print("Deposit successful!")
        elif user_in == 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount > account.get_accbal():
                print("Insufficient balance!")
            else:
                account.set_acc_bal_(account.get_accbal() - amount)
                print("Withdrawal successful!")
        elif user_in == 4:
            print("Account Balance: ", account.get_accbal())
        elif user_in == 5:
            print("Exiting...")
        else:
            print("Invalid choice! Please try again.")
            

        
