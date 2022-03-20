import pytest
from brownie import accounts, FlashLoanArbitrage


@pytest.fixture
def account():
    return accounts[0]


@pytest.fixture
def flash_loan_arbitrage(account):
    return FlashLoanArbitrage.deploy({"from": account})
