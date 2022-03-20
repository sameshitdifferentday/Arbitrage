def test_updating_storage(account, flash_loan_arbitrage):
    assert flash_loan_arbitrage.retrieve() == 0

    new_value = 15
    txn = flash_loan_arbitrage.store(new_value, {"from": account})
    txn.wait(1)
    assert flash_loan_arbitrage.retrieve() == new_value
