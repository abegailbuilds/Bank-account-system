import pytest

from main import Card,MobileMoney

@pytest.fixture
def account():
    return Card(1234455,amount=600,balance=200,bankName="equity")


@pytest.fixture()
def new_account():
    return MobileMoney(466757,amount=200,balance=100,bankName="mpesa")


def test_card(account):
    with pytest.raises(ValueError, match="Insufficient funds!!Try a lower amount"):
        account.withdraw(200)


    assert account.withdraw(200) == 100



def test_mobile(new_account):
    assert new_account.withdraw(20) !=100


