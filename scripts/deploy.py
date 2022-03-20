from brownie import accounts, config, network, FlashLoanArbitrage


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    FlashLoanArbitrage.deploy({"from": get_account()})
