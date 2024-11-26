def calculator():
    """A simple calculator function."""

    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero")
            else:
                result = num1 / num2
        else:
            print("Invalid operator")
            continue

        print("Result:", result)

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    calculator()