from BankAccount import *

# Creating Account
Tushar = BankAccount(400 , "Tushar")
Ganesh = BankAccount(600 , 'Ganesh')
##############################################

# Transfering Money From one account to OTher
print("Balance Before Transaction")
Tushar.getBalance()
Ganesh.getBalance()

Tushar.TransferMoney(200 , Ganesh)
print("Balance After Transaction")
Tushar.getBalance()
Ganesh.getBalance()
######################################

# Creating InterestRewardAccount 
Saru = InterestRewardAccount(2000,"Saru")
Saru.Deposite(300)
Saru.getBalance()
#########################################

# Creating Saving Account . (In saving account Withdraw has 5 rs fee)
Papa = SavingAccount(5000 , "Papa")
Papa.Deposite(1000)
Papa.getBalance()
Papa.TransferMoney(1000, Ganesh)
Ganesh.getBalance()
Papa.getBalance()
Tushar.getBalance()
Papa.TransferMoney(5000 , Tushar)
Tushar.getBalance()
Papa.getBalance()
Saru.getBalance()
Papa.TransferMoney(20, Saru)
Saru.getBalance()
Papa.getBalance()