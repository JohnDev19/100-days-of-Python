def perform_arithmetic_operations(num1, num2):
    # Addition
    addition = num1 + num2
    print(f"Addition: {num1} + {num2} = {addition}")

    # Subtraction
    subtraction = num1 - num2
    print(f"Subtraction: {num1} - {num2} = {subtraction}")

    # Multiplication
    multiplication = num1 * num2
    print(f"Multiplication: {num1} * {num2} = {multiplication}")

    # Division / error handling
    try:
        division = num1 / num2
        print(f"Division: {num1} / {num2} = {division}")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

    # Floor Division / error handling
    try:
        floor_division = num1 // num2
        print(f"Floor Division: {num1} // {num2} = {floor_division}")
    except ZeroDivisionError:
        print("Floor division by zero is not allowed.")

    # Modulus / error handling
    try:
        modulus = num1 % num2
        print(f"Modulus: {num1} % {num2} = {modulus}")
    except ZeroDivisionError:
        print("Modulus operation by zero is not allowed.")

    # Exponentiation
    exponentiation = num1 ** num2
    print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")

    # Complex operation
    complex_operation = (num1 + num2) * (num1 - num2) / (num1 + 1)
    print(f"Complex Operation: ({num1} + {num2}) * ({num1} - {num2}) / ({num1} + 1) = {complex_operation}")

if __name__ == "__main__":
    # Test / two numbers
    number1 = 12
    number2 = 5

    print(f"Performing arithmetic operations on {number1} and {number2}:\n")
    perform_arithmetic_operations(number1, number2)

    # Edge case: division by zero
    number1 = 12
    number2 = 0

    print(f"\nPerforming arithmetic operations on {number1} and {number2} (edge case - division by zero):\n")
    perform_arithmetic_operations(number1, number2)
