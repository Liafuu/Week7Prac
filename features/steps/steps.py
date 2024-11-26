from behave import *
from calculator import add, subtract, multiply, divide

@given('Calculator initialized')
def step_calculator_initialized(context):
    context.result = None

@when('Add {x:d} and {y:d}')
def step_add(context, x, y):
    context.result = add(x, y)

@when('Subtract {y:d} from {x:d}')
def step_subtract(context, x, y):
    context.result = subtract(x, y)

@when('Multiply {x:d} and {y:d}')
def step_multiply(context, x, y):
    context.result = multiply(x, y)

@when('Divide {x:d} by {y:d}')
def step_division(context, x, y):
    context.result = divide(x, y)


@then('Result is {expected_result}')
def step_expected_result(context, expected_result):
    expected_result = int(expected_result)
    assert context.result == expected_result, \
        f"Expected {expected_result}, but got {context.result}."