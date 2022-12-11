Feature: Bank Transactions
  Tests pertaining to banking transactions like withdrawal, deposit
  Scenario: Withdrawal of money
    Given the account balance is 1000
    When the account holder withdraws 200
    When the account holder withdraws 500
    Then the account balance should be 300

  Scenario: Withdrawal and deposit of money
    Given the account balance is 4000
    When the account holder withdraws 1000
    And the account holder deposits 2000
    Then the account balance should be 5000





