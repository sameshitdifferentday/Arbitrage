from brownie import config, network, FlashLoanArbitrage

from scripts.utils import ALLOWED_NETWORKS, PROD_NETWORKS, get_account


def deploy(verify_contract: bool = False):
    return FlashLoanArbitrage.deploy(
        {"from": get_account()},
        publish_source=verify_contract
    )


def main():
    if network.show_active() not in ALLOWED_NETWORKS:
        print(f"Invalid network '{network.show_active()}'. The allowed networks are: {ALLOWED_NETWORKS}")
        return

    if network.show_active() in PROD_NETWORKS and input("Running on a production network will use real money. "
                                                        "Are you sure you want to proceed (y/n)? ") != "y":
        exit()

    flash_loan_arbitrage = deploy(config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to address '{flash_loan_arbitrage.address}' on the {network.show_active()} network")
