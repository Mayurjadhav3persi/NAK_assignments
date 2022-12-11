from pytest_bdd import scenario, given, when, then, parsers
import pytest


def pytest_configure():
    pytest.AMT = 0


# Feature: Bank Transactions
@scenario('features/first.feature', 'Withdrawal of money')
def test_withdrawal():
    print("Withdrawal of money scenario is covered successfully")
    pass


@given('the account balance is 1000')
def current_balance():
    pytest.AMT = 1000


@when('the account holder withdraws 200')
def withdraw_amount():
    pytest.AMT = pytest.AMT - 200


@when('the account holder withdraws 500')
def withdraw_amount():
    pytest.AMT = pytest.AMT - 500


@then('the account balance should be 300')
def final_balance():
    assert pytest.AMT == 300


@scenario('features/first.feature', 'Withdrawal and deposit of money')
def test_withdrawal_deposit():
    print("Withdrawal and deposit of money scenario is covered successfully")
    pass


@given('the account balance is 4000')
def current_balance():
    pytest.AMT = 4000


@when('the account holder withdraws 1000')
def withdraw_amount():
    pytest.AMT = pytest.AMT - 1000


@when('the account holder deposits 2000')
def withdraw_amount():
    pytest.AMT = pytest.AMT + 2000


@then('the account balance should be 5000')
def final_balance():
    assert pytest.AMT == 5000


# Feature: Check My wallet balance
@scenario('features/second.feature', "My wallet balance")
def test_wallet_balance():
    print("My wallet balance scenario is covered successfully")
    pass


@given(parsers.parse("there are {initial:d} rupees"), target_fixture="rupees")
def existing_rupees(initial):
    return dict(initial=initial)


@when(parsers.parse("I deposit {deposit:d} rupees"))
def deposit_rupees(rupees, deposit):
    rupees["deposit"] = deposit
    print('deposit_rupees', rupees)


@when(parsers.parse("I withdraw {withdraw:d} rupees"))
def withdraw_rupees(rupees, withdraw):
    rupees["withdraw"] = withdraw
    print('withdraw_rupees', rupees)


@then(parsers.parse("I should have {final:d} rupees"))
def final_rupees(rupees, final):
    assert rupees['initial'] + rupees['deposit'] - rupees['withdraw'] == final
