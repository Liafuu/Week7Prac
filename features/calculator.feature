Feature: Calculator
    Validate all arithmetic operations.

    Scenario: Addition
        Given Calculator initialized
        When Add 10 and 5
        Then result is 15