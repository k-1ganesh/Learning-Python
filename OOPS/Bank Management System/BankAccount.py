class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,InitialAmount , AccountName):
        self.balance = InitialAmount
        self.name = AccountName
        print("Account Created !")
        print(f"Name : '{self.name}' , Balance : '{self.balance:.2f}'\n")

    def getBalance(self):
        print(f"Name : '{self.name}' , Balance : '{self.balance:.2f}'\n")
    
    def Deposite(self , amount):
        self.balance = self.balance + amount
        print("Money Successfully Deposited !")
    
    def vulnerableTransaction(self,amount):
        if (amount > self.balance):
            raise BalanceException(f"Sorry Account has Insufficient Balance.")
        else:
            return
    
    def Withdraw(self , amount):
        try:
            self.vulnerableTransaction(amount)
            self.balance = self.balance - amount
            print("Withdraw is succefully done !")
        except BalanceException as e:
            print("Withdraw Interupted !")
            print(e)

    def TransferMoney(self,amount ,destination):
        try:
            self.vulnerableTransaction(amount)
            self.Withdraw(amount)
            destination.Deposite(amount)
        except BalanceException as error:
            print(error)

class InterestRewardAccount(BankAccount):
    def Deposite(self , Amount):
        self.balance = self.balance + (Amount * 1.05)  # On deposite gets 5% extra money.
        print("Money Successfully Deposited !") 
         
class SavingAccount(InterestRewardAccount):
    def __init__(self,InitialAmount , Name):
        super().__init__(InitialAmount , Name)
        self.fee = 5
    
    def Withdraw(self,Amount):
        try: 
            self.vulnerableTransaction(Amount + self.fee)
            self.balance = self.balance - (Amount + self.fee)
            print("Withdraw is succefully done !")
        except BalanceException as e:
            print("Withdraw Interupted !")
            print(e)
            # raise BalanceException("Insufficient Balance !")
    def TransferMoney(self,Amount,Destination):
        try:
            self.vulnerableTransaction(Amount + self.fee)
            self.Withdraw(Amount)
            Destination.Deposite(Amount)
            print("Transfer Succefully")
        except BalanceException as error:
            print(error)

        


