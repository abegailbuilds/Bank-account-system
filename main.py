# create account
# deposit,withdraw,check balance
# basic validation
# multiple account types
# write a unit test for important functionality



class BankAccount:

    def __init__(self,accountNo,amount,balance,bankName):

        self.accountNo=accountNo
        self.amount=amount
        self.balance=balance
        self.bankName=bankName


    def withdraw(self,amount):

        if amount>self.balance:
            raise ValueError("Insufficient funds!!Try a lower amount")

        self.balance-=amount

        print(f"You have withdrawn sh{amount} from {self.bankName} account for Account No: {self.accountNo}")
        print(f"You're left with "
              f"kSH: {self.amount}")
        return self.balance


    def deposit(self,amount):

        self.balance+=amount
        print(f"You have deposited sh: {amount} to {self.bankName} account for Account No: {self.accountNo}")
        print(f"You're left with ksh{self.amount}")
        return self.balance

    def checkBalance(self):


        print(f"Your new account balance is: {self.balance}")
        withDrawState=self.balance >0

        return withDrawState


class Card(BankAccount):

    def __init__(self,accountNo,amount,balance,bankName):
        super(). __init__(accountNo,amount,balance,bankName)
        self.bankName=bankName




class MobileMoney(BankAccount):

    def __init__(self,accountNo,amount,balance,bankName):
        super(). __init__(accountNo,amount,balance,bankName)
        self.bankName=bankName






equity=Card(12342566,200,400,bankName="Equity")
equity.deposit(150)
equity.checkBalance()


mpesa=MobileMoney(745567656,800,200,bankName="Mpesa")
mpesa.withdraw(150)
mpesa.checkBalance()