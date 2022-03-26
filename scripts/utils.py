from brownie import accounts, config, network

DEV_NETWORKS = ["development", "polygon-test"]
PROD_NETWORKS = ["polygon-main"]
ALLOWED_NETWORKS = DEV_NETWORKS + PROD_NETWORKS


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
