from brownie import FlashLoanArbitrage


def read_contract():
    if len(FlashLoanArbitrage) == 0:
        print("No deployed contracts")
        return

    flash_loan_arbitrage = FlashLoanArbitrage[-1]
    print(flash_loan_arbitrage.retrieve())


def main():
    read_contract()
