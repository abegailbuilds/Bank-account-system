import pytest
from main import BankAccount


@pytest.fixture
def demo_bank():
    return BankAccount(accountNo="12345678",amount=1000,balance=1000,bankName="Equity")

@pytest.fixture()
def demo_bank2():
    return BankAccount(accountNo="12345668",amount=1500,balance=1500,bankName="DTB Bank")

def test_deposit_bank1(demo_bank):
    assert demo_bank.deposit(1000)==2000

def test_withdraw_bank2(demo_bank2):
    with pytest.raises(ValueError,match="Insufficient funds!!Try a lower amount"):
        assert demo_bank2.withdraw(2000)!=1000
def test_demo(demo_bank):
    with pytest.raises(ValueError, match="Insufficient funds!!Try a lower amount"):
        demo_bank.withdraw(100000)

def test_demo1_balance(demo_bank):
    assert demo_bank.checkBalance()==True