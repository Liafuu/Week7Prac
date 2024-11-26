Feature: Calculator
    Validate all arithmetic operations.

    Scenario: Addition
        Given Calculator initialized
        When Add 10 and 5
        Then result is 15

    Scenario: Subtraction
        Given Calculator initialized
        When Subtract 10 from 20
        Then result is 10

    Scenario: Multiplication
        Given Calculator initialized
        When Multiply 6 and 7
        Then result is 42

    Scenario: Division
        Given Calculator initialized
        When Divide 10 by 2
        Then result is 5