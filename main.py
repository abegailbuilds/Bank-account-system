# create account
# deposit,withdraw,check balance
# basic validation
# multiple account types
# write a unit test for important functionality
from abc import ABC, abstractmethod




class BankAccount:

    def __init__(self,accountNo,amount,balance):

        self.accountNo=accountNo
        self.amount=amount
        self.balance=balance


    def withdraw(self,amount):

        if amount>self.balance:
            raise ValueError("Insufficient funds!!Try a lower amount")

        self.balance-=amount
        self.amount -= amount
        print(f"You have withdrawn sh{amount} from {self.bankName} account for Account No: {self.accountNo}")
        print(f"You're left with ksh{self.amount}")
        return self.balance


    def deposit(self,amount):

        self.balance+=amount
        self.amount-=amount
        print(f"You have deposited sh{amount} to {self.bankName} account for Account No: {self.accountNo}")
        print(f"You're left with ksh{self.amount}")
        return self.balance

    @abstractmethod
    def checkBalance(self):

        pass


class Card(BankAccount):

    def __init__(self,accountNo,amount,balance,bankName):
        super(). __init__(accountNo,amount,balance)
        self.bankName=bankName


    def checkBalance(self):

        print(f"Your account balance is: {self.balance}")



class MobileMoney(BankAccount):

    def __init__(self,accountNo,amount,balance,bankName):
        super(). __init__(accountNo,amount,balance)
        self.bankName=bankName


    def checkBalance(self):

        print(f"Your account balance is: {self.balance}")




equity=Card(12342566,200,400,"Equity")
equity.deposit(150)
equity.checkBalance()


mpesa=MobileMoney(745567656,800,200,"Mpesa")
mpesa.withdraw(150)
mpesa.checkBalance()