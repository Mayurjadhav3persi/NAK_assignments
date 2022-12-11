Feature: Check My wallet balance

  Scenario Outline: My wallet balance
    Given there are <initial> rupees
    When I deposit <deposit> rupees
    And I withdraw <withdraw> rupees
    Then I should have <final> rupees

    Examples: Values
      | initial | deposit | withdraw | final  |
      | 100     | 50       | 20      | 130    |
      | 200     | 30       | 40      | 190    |
      | 300     | 70       | 50      | 320    |
      | 400     | 10       | 30      | 380    |