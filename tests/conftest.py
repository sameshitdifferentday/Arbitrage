import pytest
from brownie import network, FlashLoanArbitrage

from scripts.deploy import deploy
from scripts.utils import DEV_NETWORKS, get_account


@pytest.fixture
def account():
    if network.show_active() not in DEV_NETWORKS:
        raise ValueError(f"Invalid network for testing: {network.show_active()}")

    return get_account()


@pytest.fixture
def flash_loan_arbitrage(account):
    if len(FlashLoanArbitrage) != 0:
        return FlashLoanArbitrage[-1]
    else:
        print("No existing contract. Deploying new one...")
        return deploy()
