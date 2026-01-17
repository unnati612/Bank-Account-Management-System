#BANK ACCOUNT MANAGEMENT SYSTEM
#name,bal,acc_no->attr/var
class BankAccount:
    def __init__(self,name,bal,acc_no):  #constructor
        self.name=name
        self.__bal=bal
        self.__acc_no=acc_no #private attribute
        

    def get_acc(self):  #method(getter)
        return self.__acc_no
    
    def get_balance(self):
        return self.__bal


    #try->to prevent program crashes 
    def deposit(self,damount):  #method
        try:
            damount=int(damount)
            if damount>0:
                self.__bal += damount
                return "Amount deposited is "+ str(damount)+ ".\nNew balance is " +str(self.__bal)
            else:
                return "Amount must be greater than zero"
        except ValueError:
            return "Please enter valid amount"

        
    def withdraw(self,wamount):
        try:
            wamount=int(wamount)
            if wamount<=0:
                return "Amount should be greater than zero"
            elif wamount<=self.__bal:
                self.__bal -= wamount
                return "Amount withdrawn is "+ str(wamount)+ "\nNew balance is " +str(self.__bal)
            else:
                return "Insufficient balance"
        except ValueError:
            return "Invalid withdrawal amount"
    


    def details(self):
        print("Name:",self.name)
        print("Account Number:", self.get_acc())
        print("Balance:",self.get_balance())



B1=BankAccount("Alice",1000,1234)
print(B1.details())
print(B1.deposit(1000))   #performs deposit operation
print(B1.withdraw(300))    #performs withdrawal operations
